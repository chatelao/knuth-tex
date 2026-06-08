import re
import sys
from pathlib import Path

def extract_pascal_module_sequence(pascal_file):
    """
    Extracts the sequence of WEB module markers {n:} and {:n} from a Pascal file.
    """
    try:
        with open(pascal_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {pascal_file}: {e}")
        return []

    # Regex for module markers: {n:} (start) and {:n} (end)
    # n is a decimal number.
    start_regex = re.compile(r'\{(\d+):\}')
    end_regex = re.compile(r'\{:(\d+)\}')

    sequence = []

    # Find all start markers
    for match in start_regex.finditer(content):
        sequence.append({
            'type': 'start',
            'module': int(match.group(1)),
            'pos': match.start()
        })

    # Find all end markers
    for match in end_regex.finditer(content):
        sequence.append({
            'type': 'end',
            'module': int(match.group(1)),
            'pos': match.start()
        })

    # Sort by position in the file, then by type (end before start if same pos)
    # This is important if we have something like {:178}{179:}
    # Actually, they usually have different pos if they are separate tokens.
    # If they are exactly at the same pos, we want the end of the previous one
    # to be processed before the start of the next one.

    def sort_key(item):
        # type 'end' should come before 'start' if position is the same
        type_priority = 0 if item['type'] == 'end' else 1
        return (item['pos'], type_priority)

    sequence.sort(key=sort_key)

    return sequence

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pascal_module_extractor.py <pascal_file1> [<pascal_file2> ...]")
        sys.exit(1)

    for pascal_file in sys.argv[1:]:
        print(f"--- Module sequence in {pascal_file} ---")
        sequence = extract_pascal_module_sequence(pascal_file)
        if not sequence:
            print("No module markers found.")
        else:
            for item in sequence:
                marker = f"{{{item['module']}:}}" if item['type'] == 'start' else f"{{:{item['module']}}}"
                print(f"Pos {item['pos']:8}: {marker}")
        print()

if __name__ == "__main__":
    main()
