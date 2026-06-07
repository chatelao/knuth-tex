import re
import sys
from pathlib import Path

# Add the current directory to sys.path to allow importing verify_tangle_output if run from here
sys.path.append(str(Path(__file__).parent))

try:
    from verify_tangle_output import PascalNormalizer
except ImportError:
    # Fallback for different execution environments
    class PascalNormalizer:
        def strip_comments(self, code):
            code = re.sub(r'\(\*.*?\*\)', ' ', code, flags=re.DOTALL)
            result = []
            stack = 0
            i = 0
            while i < len(code):
                if code[i] == '{':
                    if stack == 0: result.append(' ')
                    stack += 1
                elif code[i] == '}':
                    if stack > 0: stack -= 1
                    else: result.append(code[i])
                elif stack == 0:
                    result.append(code[i])
                i += 1
            return "".join(result)
        def strip_strings(self, code):
            return re.sub(r"'([^']|'')*'", "''", code)
        def normalize_whitespace(self, code):
            return re.sub(r'\s+', ' ', code).strip()

class PascalRoutineExtractor:
    """Utility to extract procedure and function signatures from Pascal source."""

    def __init__(self):
        self.normalizer = PascalNormalizer()

    def extract_signatures(self, code):
        """
        Extracts routine signatures from Pascal code.
        Returns a list of dictionaries with routine details.
        """
        # Strip comments and strings
        clean_code = self.normalizer.strip_strings(self.normalizer.strip_comments(code))
        # Replace newlines and multiple spaces with a single space to simplify regex matching
        clean_code = re.sub(r'\s+', ' ', clean_code)

        signatures = []

        # Regex to match: (procedure|function) name [(parameters)] [: return_type] ;
        # Using [^;]*? for parameters to handle everything until the first semicolon of the declaration.
        # But wait, parameters can contain semicolons: (a: integer; b: boolean)
        # So we should look for balanced parentheses or at least until the closing paren if present.

        # Improved regex to handle parameter lists that may contain semicolons
        # It looks for (procedure|function), name, then optionally a parenthesized group,
        # then optionally a colon and type, then a semicolon.
        pattern = re.compile(
            r'\b(procedure|function)\s+([a-zA-Z0-9_]+)\s*(\(.*?\))?\s*(:\s*[a-zA-Z0-9_]+)?\s*;',
            re.IGNORECASE
        )

        for match in pattern.finditer(clean_code):
            kind = match.group(1).lower()
            name = match.group(2).lower()
            params = match.group(3) if match.group(3) else ""
            ret_type = match.group(4) if match.group(4) else ""

            # Check for forward or external immediately following
            # Look ahead in clean_code after the match
            remaining = clean_code[match.end():].strip()
            directive = None
            if remaining.lower().startswith('forward'):
                directive = 'forward'
            elif remaining.lower().startswith('external'):
                directive = 'external'

            signatures.append({
                'kind': kind,
                'name': name,
                'params': params.strip(),
                'return_type': ret_type.lstrip(':').strip(),
                'directive': directive,
                'full_signature': match.group(0).strip()
            })

        return signatures

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pascal_routine_extractor.py <pascal_file>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    extractor = PascalRoutineExtractor()
    signatures = extractor.extract_signatures(code)

    if not signatures:
        print("No routine signatures found.")
    else:
        for sig in signatures:
            line = f"{sig['kind'].capitalize()} {sig['name']}"
            if sig['params']:
                line += f" {sig['params']}"
            if sig['return_type']:
                line += f": {sig['return_type']}"
            if sig['directive']:
                line += f" {sig['directive']}"
            print(line)

if __name__ == "__main__":
    main()
