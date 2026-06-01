import re
import sys
from pathlib import Path

def identify_io_routines(web_file):
    """Identifies system-dependent I/O routines in a WEB file."""
    try:
        with open(web_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {web_file}: {e}")
        return []

    # System-dependent I/O routines usually follow @p or @<...@>=
    # But there can be multiple routines in one block.
    # We'll look for routine declarations that match our target names.
    target_names = [
        'a_open_in', 'a_open_out',
        'b_open_in', 'b_open_out',
        'w_open_in', 'w_open_out',
        'a_close', 'b_close', 'w_close'
    ]

    # We want to find them in the Pascal parts of the WEB file.
    # Pascal parts start with @p or @<...@>= and end before the next @ or end of file.
    pascal_blocks = []
    # Simplified splitting: look for @p or @<...@>=
    block_starts = [m.start() for m in re.finditer(r'(?:@p|@<[^@]*@>=)', content)]
    for i, start in enumerate(block_starts):
        end = block_starts[i+1] if i+1 < len(block_starts) else len(content)
        # End also happens at next @ followed by space or newline (new module)
        next_mod = re.search(r'\n@[\s*]', content[start+1:end])
        if next_mod:
            end = start + 1 + next_mod.start()
        pascal_blocks.append((start, end))

    routines = []
    name_regex = r'\b(function|procedure)\s+(' + '|'.join(target_names) + r')\b'

    for start, end in pascal_blocks:
        block_content = content[start:end]
        for match in re.finditer(name_regex, block_content, re.IGNORECASE):
            kind = match.group(1).lower()
            name = match.group(2).lower()
            # Find line number
            line_no = content.count('\n', 0, start + match.start()) + 1

            routines.append({
                'name': name,
                'kind': kind,
                'line': line_no
            })

    return routines

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 identify_io_routines.py <web_file1> [<web_file2> ...]")
        sys.exit(1)

    for web_file in sys.argv[1:]:
        print(f"--- Routines in {web_file} ---")
        routines = identify_io_routines(web_file)
        if not routines:
            print("No routines found.")
        # Sort by line number
        routines.sort(key=lambda x: x['line'])
        for r in routines:
            print(f"{r['kind'].capitalize()}: {r['name']} (Line {r['line']})")
        print()

if __name__ == "__main__":
    main()
