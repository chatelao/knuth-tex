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
    # Modules start with @ followed by space, tab, newline or *
    module_regex = re.compile(r'^@[\s\*]', re.MULTILINE)

    module_starts = [m.start() for m in module_regex.finditer(content)]

    # Standard WEB module numbering starts with the first @ in the file.
    # Anything before that is ignored in terms of module numbering.

    mapping = []
    routine_regex = re.compile(r'\b(function|procedure)\s+([a-zA-Z0-9_]+)\b', re.IGNORECASE)

    for i, start in enumerate(module_starts):
        module_num = i + 1
        end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
        module_content = content[start:end]

        # We only care about Pascal routines defined in this module.
        # Pascal parts usually start with @p or @<...@>=
        pascal_blocks = []
        pascal_starts = [m.start() for m in re.finditer(r'(?:@p|@<[^@]*@>=)', module_content)]
        for j, p_start in enumerate(pascal_starts):
            p_end = pascal_starts[j+1] if j+1 < len(pascal_starts) else len(module_content)
            # Pascal block ends at next @ (not in string/comment)
            # Heuristic: next @ followed by space/newline/p/< is next part.
            next_web = re.search(r'\n@[\s\*p<]', module_content[p_start+1:p_end])
            if next_web:
                p_end = p_start + 1 + next_web.start()
            pascal_blocks.append(module_content[p_start:p_end])

        for block in pascal_blocks:
            for match in routine_regex.finditer(block):
                kind = match.group(1).lower()
                name = match.group(2).lower()
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
