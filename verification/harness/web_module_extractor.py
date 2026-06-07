import re
import sys
from pathlib import Path

def extract_web_modules(web_file):
    """Maps Pascal routines to WEB module numbers."""
    try:
        with open(web_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {web_file}: {e}")
        return []

    # Split into modules
    module_regex = re.compile(r'^@[\s\*]', re.MULTILINE)
    module_starts = [m.start() for m in module_regex.finditer(content)]

    mapping = []
    # Simplified Pascal routine regex for WEB
    # We want to capture the header up to the semicolon
    routine_regex = re.compile(r'\b(function|procedure)\s+([a-zA-Z0-9_]+)\b', re.IGNORECASE)

    for i, start in enumerate(module_starts):
        module_num = i + 1
        end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
        module_content = content[start:end]

        pascal_blocks = []
        pascal_starts = [m.start() for m in re.finditer(r'(?:@p|@<[^@]*@>=)', module_content)]
        for j, p_start in enumerate(pascal_starts):
            p_end = pascal_starts[j+1] if j+1 < len(pascal_starts) else len(module_content)
            next_web = re.search(r'\n@[\s\*p<]', module_content[p_start+1:p_end])
            if next_web:
                p_end = p_start + 1 + next_web.start()
            pascal_blocks.append(module_content[p_start:p_end])

        for block in pascal_blocks:
            for match in routine_regex.finditer(block):
                kind = match.group(1).lower()
                name = match.group(2).lower()

                # Extract the rest of the signature until the semicolon
                pos = match.end()
                rest = ""
                stack = 0
                for k in range(pos, len(block)):
                    char = block[k]
                    if char == '(':
                        stack += 1
                    elif char == ')':
                        if stack > 0: stack -= 1
                    elif char == ';' and stack == 0:
                        rest = block[pos:k].strip()
                        break

                params = ""
                ret_type = ""
                if rest.startswith('('):
                    p_stack = 0
                    for k, char in enumerate(rest):
                        if char == '(': p_stack += 1
                        elif char == ')':
                            p_stack -= 1
                            if p_stack == 0:
                                params = rest[:k+1]
                                after_params = rest[k+1:].strip()
                                if after_params.startswith(':'):
                                    ret_type = after_params[1:].strip()
                                break
                elif rest.startswith(':'):
                    ret_type = rest[1:].strip()

                mapping.append({
                    'module': module_num,
                    'name': name,
                    'kind': kind,
                    'params': params,
                    'return_type': ret_type
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
                sig = f"Module {item['module']:4}: {item['kind'].capitalize():9} {item['name']}"
                if item['params']: sig += f" {item['params']}"
                if item['return_type']: sig += f": {item['return_type']}"
                print(sig)
        print()

if __name__ == "__main__":
    main()
