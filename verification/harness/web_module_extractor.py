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
    # Improved routine regex to handle underscores and @p
    # Now correctly handles 'forward;' by not matching it as a primary definition if it's just 'procedure name; forward;'
    # We look for routine definitions in any part of the module content.
    routine_regex = re.compile(r'(?:@p|@<[^@]*@>=).*?\b(function|procedure)\s+([a-zA-Z0-9_]+)(?:\s*;\s*forward\s*;)?', re.IGNORECASE | re.DOTALL)

    for i, start in enumerate(module_starts):
        module_num = i + 1
        end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
        module_content = content[start:end]

        # Scan for routines within this module's Pascal blocks
        for match in routine_regex.finditer(module_content):
            kind = match.group(1).lower()
            name = match.group(2).lower().replace('_', '')

            # Check for 'forward' in the full match
            is_forward = 'forward' in match.group(0).lower()

            mapping.append({
                'module': module_num,
                'name': name,
                'kind': kind,
                'forward': is_forward
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
                fwd = " [FORWARD]" if item.get('forward') else ""
                print(f"Module {item['module']:4}: {item['kind'].capitalize():9} {item['name']}{fwd}")
        print()

if __name__ == "__main__":
    main()
