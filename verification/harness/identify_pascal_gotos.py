import re
import sys
from pathlib import Path

# Try to reuse PascalNormalizer if possible, but let's define a specialized one here
# that can optionally preserve module markers.

class PascalGOTOExtractor:
    def __init__(self):
        # Regex for module markers: {n:} (start) and {:n} (end)
        self.start_regex = re.compile(r'\{(\d+):\}')
        self.end_regex = re.compile(r'\{:(\d+)\}')
        # Regex for label declaration: label 1, 2, exit;
        self.label_decl_regex = re.compile(r'\blabel\b\s*([^;]+);', re.IGNORECASE)
        # Regex for goto: goto 10;
        self.goto_regex = re.compile(r'\bgoto\b\s+([a-zA-Z0-9_]+)', re.IGNORECASE)

    def strip_comments_and_strings(self, code, preserve_markers=False):
        """
        Strips Pascal comments and strings.
        If preserve_markers is True, it keeps {n:} and {:n} markers.
        """
        result = []
        i = 0
        while i < len(code):
            # String literal
            if code[i] == "'":
                result.append("'")
                i += 1
                while i < len(code):
                    if code[i] == "'" and (i + 1 == len(code) or code[i+1] != "'"):
                        result.append("'")
                        i += 1
                        break
                    elif code[i] == "'" and i + 1 < len(code) and code[i+1] == "'":
                        result.append("''")
                        i += 2
                    else:
                        result.append(" ")
                        i += 1
                continue

            # Comment { ... }
            if code[i] == '{':
                if preserve_markers:
                    match = self.start_regex.match(code, i) or self.end_regex.match(code, i)
                    if match:
                        marker = match.group(0)
                        result.append(marker)
                        i += len(marker)
                        continue

                # Standard comment
                stack = 1
                result.append(" ")
                i += 1
                while i < len(code) and stack > 0:
                    if code[i] == '{':
                        stack += 1
                    elif code[i] == '}':
                        stack -= 1
                    result.append(" ")
                    i += 1
                continue

            # Comment (* ... *)
            if code[i:i+2] == '(*':
                stack = 1
                result.append("  ")
                i += 2
                while i < len(code) and stack > 0:
                    if code[i:i+2] == '(*':
                        stack += 1
                        result.append("  ")
                        i += 2
                    elif code[i:i+2] == '*)':
                        stack -= 1
                        result.append("  ")
                        i += 2
                    else:
                        result.append(" ")
                        i += 1
                continue

            result.append(code[i])
            i += 1

        return "".join(result)

    def identify_gotos(self, pascal_file):
        try:
            with open(pascal_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {pascal_file}: {e}")
            return [], []

        # We want to maintain position mapping.
        # Let's find all markers first.
        markers = []
        for match in self.start_regex.finditer(content):
            markers.append({'type': 'start', 'module': int(match.group(1)), 'pos': match.start()})
        for match in self.end_regex.finditer(content):
            markers.append({'type': 'end', 'module': int(match.group(1)), 'pos': match.start()})

        def sort_key(item):
            # type 'end' should come before 'start' if position is the same
            type_priority = 0 if item['type'] == 'end' else 1
            return (item['pos'], type_priority)
        markers.sort(key=sort_key)

        # Clean code but keep markers to find things within modules
        # Actually, it's better to clean EVERYTHING and then use the absolute positions
        # to find which module a goto belongs to.

        clean_content = self.strip_comments_and_strings(content, preserve_markers=False)

        labels = []
        for match in self.label_decl_regex.finditer(clean_content):
            decls = [l.strip() for l in match.group(1).split(',')]
            pos = match.start()
            line_no = content.count('\n', 0, pos) + 1
            module_num = self._get_module_at_pos(pos, markers)
            for l in decls:
                if l:
                    labels.append({
                        'module': module_num,
                        'line': line_no,
                        'label': l,
                        'pos': pos
                    })

        gotos = []
        for match in self.goto_regex.finditer(clean_content):
            target = match.group(1)
            pos = match.start()
            line_no = content.count('\n', 0, pos) + 1
            module_num = self._get_module_at_pos(pos, markers)
            gotos.append({
                'module': module_num,
                'line': line_no,
                'target': target,
                'pos': pos
            })

        return gotos, labels

    def _get_module_at_pos(self, pos, markers):
        """Returns the module number active at the given position."""
        current_module = None
        # We assume markers are sorted by pos.
        # We find the last 'start' marker that is before or at pos,
        # provided it hasn't been closed by an 'end' marker.
        # However, TANGLE output sometimes has nested or overlapping-looking markers if we are not careful.
        # But generally it is: {n:} ... {:n}

        active_stack = []
        for m in markers:
            if m['pos'] > pos:
                break
            if m['type'] == 'start':
                active_stack.append(m['module'])
            elif m['type'] == 'end':
                if active_stack and active_stack[-1] == m['module']:
                    active_stack.pop()
                elif m['module'] in active_stack:
                    # Handle cases where they might not be perfectly nested in the markers list
                    active_stack.remove(m['module'])

        return active_stack[-1] if active_stack else None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 identify_pascal_gotos.py <pascal_file1> [<pascal_file2> ...]")
        sys.exit(1)

    extractor = PascalGOTOExtractor()
    for pascal_file in sys.argv[1:]:
        print(f"--- GOTOs and Labels in {pascal_file} ---")
        gotos, labels = extractor.identify_gotos(pascal_file)

        print(f"Found {len(labels)} label declarations:")
        for l in labels:
            mod_str = f"Module {l['module']}" if l['module'] else "Global/Unknown"
            print(f"  {mod_str:12} (Line {l['line']:5}): label {l['label']}")

        print(f"\nFound {len(gotos)} GOTO statements:")
        for g in gotos:
            mod_str = f"Module {g['module']}" if g['module'] else "Global/Unknown"
            print(f"  {mod_str:12} (Line {g['line']:5}): goto {g['target']}")
        print()

if __name__ == "__main__":
    main()
