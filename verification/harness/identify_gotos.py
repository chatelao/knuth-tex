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

    # Extract macros (@d)
    macros = {}
    macro_regex = re.compile(r'^@d\s+([a-zA-Z0-9_]+)\s*==?\s*(.*)$', re.MULTILINE)
    for match in macro_regex.finditer(content):
        name = match.group(1)
        value = match.group(2).strip()
        # Strip comments from value
        value = re.sub(r'\{.*?\}', '', value).strip()
        macros[name] = value

    # Split into modules
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

        # Find Pascal parts
        pascal_starts = [m.start() for m in re.finditer(r'(?:@p|@<[^@]*@>=)', module_content)]
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
                        labels.append({
                            'module': module_num,
                            'line': line_no,
                            'label': l
                        })

            # Find goto statements
            for match in goto_regex.finditer(clean_block):
                target = match.group(1)
                line_no = content.count('\n', 0, start + p_start + match.start()) + 1
                gotos.append({
                    'module': module_num,
                    'line': line_no,
                    'target': target
                })

            # Also identify usages of macros that contain 'goto'
            for macro_name, macro_val in macros.items():
                if 'goto' in macro_val.lower():
                    macro_use_regex = re.compile(rf'\b{re.escape(macro_name)}\b')
                    for match in macro_use_regex.finditer(clean_block):
                        line_no = content.count('\n', 0, start + p_start + match.start()) + 1
                        target_match = goto_regex.search(macro_val)
                        if target_match:
                            target = target_match.group(1)
                            gotos.append({
                                'module': module_num,
                                'line': line_no,
                                'target': target,
                                'macro': macro_name
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
            print(f"  Module {l['module']:4} (Line {l['line']:5}): label {l['label']}")

        print(f"\nFound {len(gotos)} GOTO statements:")
        for g in gotos:
            target = g['target']
            macro_info = f" (via macro {g['macro']})" if 'macro' in g else ""
            print(f"  Module {g['module']:4} (Line {g['line']:5}): goto {target}{macro_info}")

if __name__ == "__main__":
    main()
