import re
import sys
from pathlib import Path

def strip_web_comments(code):
    """Simplified stripping of WEB comments {@ ... @} and Pascal comments { ... } or (* ... *)."""
    # This is tricky in WEB because { } can be Pascal comments or part of TeX.
    # But usually in Pascal parts, they are comments.

    # Strip Pascal comments
    code = re.sub(r'\(\*.*?\*\)', ' ', code, flags=re.DOTALL)
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

def extract_web_modules(web_file):
    """Maps Pascal routines to WEB module numbers."""
    try:
        with open(web_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {web_file}: {e}")
        return []

    # Split into modules
    # Modules start with @ followed by space, tab, newline or *
    module_regex = re.compile(r'^@[\s\*]', re.MULTILINE)

    module_starts = [m.start() for m in module_regex.finditer(content)]

    mapping = []
    # Routine regex: (procedure|function) followed by name.
    # We ignore @! (underline for index) and @t...@> (typesetting instructions)
    routine_regex = re.compile(r'\b(function|procedure)\b(?:\s*@\![^@]*@)?(?:\s*@t[^@]*@>)?\s*([a-zA-Z0-9_]+)', re.IGNORECASE)

    for i, start in enumerate(module_starts):
        module_num = i + 1
        end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
        module_content = content[start:end]

        # Pascal parts usually start with @p or @<...@>=
        pascal_starts = [m.start() for m in re.finditer(r'(?:@p|@<[^@]*@>=)', module_content)]
        for j, p_start in enumerate(pascal_starts):
            p_end = pascal_starts[j+1] if j+1 < len(pascal_starts) else len(module_content)

            # Extract the block
            block = module_content[p_start:p_end]

            # Strip comments to avoid matching "procedure" in comments
            # But be careful: WEB documentation is NOT in @p blocks.
            # Only code is in @p or @<...@>= blocks.
            clean_block = strip_web_comments(block)

            for match in routine_regex.finditer(clean_block):
                kind = match.group(1).lower()
                name = match.group(2).lower()
                # If name is 'called', it's likely a false positive from "@<Declare the procedure called |...|@>="
                if name == 'called':
                    # Try to find the name after 'called |'
                    m2 = re.search(r'called\s+\|([a-zA-Z0-9_]+)\|', block[match.start():])
                    if m2:
                        name = m2.group(1).lower()
                    else:
                        continue # Skip false positive

                mapping.append({
                    'module': module_num,
                    'name': name,
                    'kind': kind
                })

    return mapping

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 web_module_extractor.py <web_file1> [<web_file2> ...]")
        sys.exit(1)

    for web_file in sys.argv[1:]:
        print(f"--- Routines in {web_file} ---")
        mapping = extract_web_modules(web_file)
        if not mapping:
            print("No routines found.")
        else:
            for item in mapping:
                print(f"Module {item['module']:4}: {item['kind'].capitalize():9} {item['name']}")
        print()

if __name__ == "__main__":
    main()
