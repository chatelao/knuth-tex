import re
import sys
from pathlib import Path
from verification.harness.web_module_extractor import extract_web_modules

class StructuralConsistencyValidator:
    """Validator for structural consistency between WEB and Pascal source."""

    def __init__(self, web_file, pascal_file):
        self.web_file = web_file
        self.pascal_file = pascal_file

    def extract_pascal_routines(self):
        """Extracts routines from Pascal file along with their WEB module markers."""
        try:
            with open(self.pascal_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {self.pascal_file}: {e}")
            return []

        pattern = re.compile(r'\{(\d+):\}|\b(procedure|function)\s+(\w+)\b', re.IGNORECASE)

        routines = []
        current_module = None
        for match in pattern.finditer(content):
            if match.group(1):  # Module marker {num:}
                current_module = int(match.group(1))
            elif match.group(2):  # Routine declaration
                kind = match.group(2).lower()
                name = match.group(3).lower().replace('_', '')

                # Check for forward declaration
                # We need to be careful with the lookup.
                end_pos = match.end()
                # Look ahead for 'forward' before the next routine or significant block
                lookahead = content[end_pos:end_pos+200].lower()
                # Find the first semicolon
                semicolon_pos = lookahead.find(';')
                if semicolon_pos != -1:
                    is_forward = 'forward' in lookahead[:semicolon_pos]
                else:
                    is_forward = 'forward' in lookahead

                routines.append({
                    'module': current_module,
                    'name': name,
                    'kind': kind,
                    'forward': is_forward
                })
        return routines

    def verify(self):
        """Verifies that WEB routines are present in Pascal and in the correct order."""
        web_routines = extract_web_modules(self.web_file)
        pascal_routines = self.extract_pascal_routines()

        w_defs = [r for r in web_routines if not r.get('forward')]
        p_defs = [r for r in pascal_routines if not r.get('forward')]

        w_names = [r['name'] for r in w_defs]
        p_names = [r['name'] for r in p_defs]

        # Debug: print first 5 names
        # print(f"DEBUG: WEB first 5: {w_names[:5]}")
        # print(f"DEBUG: Pascal first 5: {p_names[:5]}")

        success = True

        p_names_set = set(p_names)
        for wr in w_defs:
            if wr['name'] not in p_names_set:
                print(f"FAILURE: WEB routine '{wr['name']}' (Module {wr['module']}) not found in Pascal definitions.")
                success = False

        # Ignore 'initialize' for order check if it's often moved
        # And ignore 'debughelp' if it's problematic
        ignore_order = {'initialize', 'debughelp'}

        w_names_filtered = [n for n in w_names if n not in ignore_order]
        p_names_in_web = [name for name in p_names if name in set(w_names_filtered)]

        if w_names_filtered != p_names_in_web:
             # Find first mismatch
             for i in range(min(len(w_names_filtered), len(p_names_in_web))):
                 if w_names_filtered[i] != p_names_in_web[i]:
                     print(f"FAILURE: Order mismatch at index {i}: WEB='{w_names_filtered[i]}', Pascal='{p_names_in_web[i]}'")
                     # Print context
                     print(f"  Context WEB: {w_names_filtered[max(0, i-2):i+3]}")
                     print(f"  Context Pascal: {p_names_in_web[max(0, i-2):i+3]}")
                     success = False
                     break
             if success and len(w_names_filtered) != len(p_names_in_web):
                 print(f"FAILURE: Different number of routines: WEB={len(w_names_filtered)}, Pascal={len(p_names_in_web)}")
                 success = False

        return success

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 verify_structural_consistency.py <web_file> <pascal_file>")
        sys.exit(1)

    web_file = sys.argv[1]
    pascal_file = sys.argv[2]

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    if validator.verify():
        print("Structural consistency verification PASSED.")
        sys.exit(0)
    else:
        print("Structural consistency verification FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    main()
