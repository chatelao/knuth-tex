import re
import sys
from pathlib import Path

def strip_web_comments(code):
    """Strips WEB comments {@ ... @} and Pascal comments { ... }."""
    # Strip Pascal comments
    # Handle nested { } for Pascal comments - simplified
    result = []
    stack = 0
    i = 0
    while i < len(code):
        if code[i:i+2] == '@{' or code[i:i+2] == '@}':
            # WEB meta-comments for debug/stat blocks, treat as spaces
            result.append('  ')
            i += 2
            continue
        if code[i] == '{':
            stack += 1
            result.append(' ')
        elif code[i] == '}':
            if stack > 0:
                stack -= 1
            else:
                result.append(code[i])
        elif stack == 0:
            result.append(code[i])
        else:
            result.append(' ')
        i += 1
    return "".join(result)

def identify_gotos(web_file):
    """Identifies GOTO statements and labels in a WEB file."""
    try:
        with open(web_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {web_file}: {e}")
        return [], [], {}

    # Extract macros (@d) - improved to handle multi-line and better matching
    macros = {}
    # Macros start with @d and end at the next @ or end of file
    macro_blocks = re.split(r'^@d\s+', content, flags=re.MULTILINE)
    for block in macro_blocks[1:]:
        # Name is the first word
        match = re.match(r'([a-zA-Z0-9_]+)(?:\(#\))?\s*==?\s*(.*)', block, re.DOTALL)
        if match:
            name = match.group(1)
            value_part = match.group(2)
            # Find the end of the definition (next @ at start of line)
            end_match = re.search(r'^@', value_part, re.MULTILINE)
            if end_match:
                value = value_part[:end_match.start()].strip()
            else:
                value = value_part.strip()

            # Strip comments from value
            value = re.sub(r'\{.*?\}', '', value, flags=re.DOTALL).strip()
            macros[name] = value

    # Split into modules
    # A module starts with @<space> or @* at the beginning of a line
    module_regex = re.compile(r'^@[\s\*]', re.MULTILINE)
    module_starts = [m.start() for m in module_regex.finditer(content)]

    gotos = []
    labels = []

    # Regex for label declaration: label 1, 2, exit;
    label_decl_regex = re.compile(r'\blabel\b\s*([^;]+);', re.IGNORECASE)
    # Regex for goto: goto 10;
    goto_regex = re.compile(r'\bgoto\b\s+([a-zA-Z0-9_]+)', re.IGNORECASE)

    for i, start in enumerate(module_starts):
        module_num = i + 1
        end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
        module_content = content[start:end]

        # Find Pascal parts: @p or @<module name@>=
        # Note: @<module name@>= can be split over lines
        pascal_starts = [m.start() for m in re.finditer(r'(?:@p|@<[^@]*@>=)', module_content, re.DOTALL)]
        if not pascal_starts:
            continue

        for j, p_start in enumerate(pascal_starts):
            p_end = pascal_starts[j+1] if j+1 < len(pascal_starts) else len(module_content)

            block = module_content[p_start:p_end]
            clean_block = strip_web_comments(block)

            # Find label declarations
            for match in label_decl_regex.finditer(clean_block):
                decls = [l.strip() for l in match.group(1).split(',')]
                line_no = content.count('\n', 0, start + p_start + match.start()) + 1
                for l in decls:
                    if l:
                        # Resolve label if it's a macro
                        resolved_l = macros.get(l, l)
                        labels.append({
                            'module': module_num,
                            'line': line_no,
                            'label': resolved_l,
                            'original_label': l
                        })

            # Find goto statements
            for match in goto_regex.finditer(clean_block):
                target = match.group(1)
                line_no = content.count('\n', 0, start + p_start + match.start()) + 1

                # Resolve target if it's a macro
                resolved_target = target
                if target in macros:
                    val = macros[target]
                    # If macro is just a number, it's a label
                    if val.isdigit():
                        resolved_target = val

                gotos.append({
                    'module': module_num,
                    'line': line_no,
                    'target': resolved_target,
                    'original_target': target
                })

            # Also identify usages of macros that contain 'goto'
            for macro_name, macro_val in macros.items():
                if 'goto' in macro_val.lower():
                    # Simplified matching for macro usage
                    macro_use_regex = re.compile(rf'\b{re.escape(macro_name)}\b')
                    for match in macro_use_regex.finditer(clean_block):
                        line_no = content.count('\n', 0, start + p_start + match.start()) + 1
                        target_match = goto_regex.search(macro_val)
                        if target_match:
                            target = target_match.group(1)
                            # Resolve macro's target too if it's a macro
                            resolved_target = macros.get(target, target)
                            gotos.append({
                                'module': module_num,
                                'line': line_no,
                                'target': resolved_target,
                                'macro': macro_name,
                                'original_target': target
                            })

    return gotos, labels, macros

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 identify_gotos.py <web_file1> [<web_file2> ...]")
        sys.exit(1)

    for web_file in sys.argv[1:]:
        print(f"--- GOTOs and Labels in {web_file} ---")
        gotos, labels, macros = identify_gotos(web_file)

        print(f"Found {len(labels)} label declarations:")
        for l in labels:
            orig = f" ({l['original_label']})" if l['label'] != l['original_label'] else ""
            print(f"  Module {l['module']:4} (Line {l['line']:5}): label {l['label']}{orig}")

        print(f"\nFound {len(gotos)} GOTO statements:")
        for g in gotos:
            target = g['target']
            orig_target = f" ({g['original_target']})" if target != g['original_target'] else ""
            macro_info = f" via macro {g['macro']}" if 'macro' in g else ""
            print(f"  Module {g['module']:4} (Line {g['line']:5}): goto {target}{orig_target}{macro_info}")

if __name__ == "__main__":
    main()
