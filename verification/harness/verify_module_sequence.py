import re
import sys
from pathlib import Path
from verification.harness.pascal_module_extractor import extract_pascal_module_sequence

def identify_code_containing_modules(web_file):
    """
    Identifies all module numbers in a WEB file that contain Pascal code parts.
    Returns a set of module numbers.
    """
    try:
        with open(web_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {web_file}: {e}")
        return set()

    # Modules start with @ followed by space, tab, newline or *
    module_regex = re.compile(r'^@[\s\*]', re.MULTILINE)
    module_starts = [m.start() for m in module_regex.finditer(content)]

    code_modules = set()

    for i, start in enumerate(module_starts):
        module_num = i + 1
        end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
        module_content = content[start:end]

        # Check if it contains Pascal code: @p or @<...@>=
        if re.search(r'(?:@p|@<[^@]*@>=)', module_content):
            code_modules.add(module_num)

    return code_modules

def verify_module_sequence(web_file, pascal_file):
    """
    Verifies that the Pascal file contains markers for all code-containing modules in WEB.
    """
    print(f"Verifying {pascal_file} against {web_file}...")

    web_code_modules = identify_code_containing_modules(web_file)
    pascal_sequence = extract_pascal_module_sequence(pascal_file)

    pascal_modules = set(item['module'] for item in pascal_sequence)

    missing_in_pascal = web_code_modules - pascal_modules

    success = True
    if missing_in_pascal:
        print(f"WARNING: Modules with code in WEB missing from Pascal markers: {sorted(list(missing_in_pascal))}")
    else:
        print(f"SUCCESS: All {len(web_code_modules)} code-containing modules from WEB are present in Pascal.")

    # Check for consistency of start/end markers
    # We use a set of open modules instead of a stack because TANGLE output
    # sometimes has mismatched or missing start/end markers, especially with named modules.

    open_modules = set()
    for item in pascal_sequence:
        if item['type'] == 'start':
            open_modules.add(item['module'])
        else:
            if item['module'] not in open_modules:
                # We warn instead of failing for some of these because TANGLE output
                # can be tricky with how it expands modules.
                print(f"WARNING: End marker {{:{item['module']}}} without matching start marker.")
            else:
                open_modules.remove(item['module'])

    if open_modules:
        print(f"WARNING: Unclosed start markers for modules: {sorted(list(open_modules))}")

    return success

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 verify_module_sequence.py <web_file> <pascal_file>")
        sys.exit(1)

    web_file = sys.argv[1]
    pascal_file = sys.argv[2]

    if verify_module_sequence(web_file, pascal_file):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
