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

        signatures = []

        # We need to find (procedure|function), then the name,
        # then possibly parameters in (), then possibly : type, then ;
        # The trick is that parameters can contain semicolons.

        pattern = re.compile(
            r'\b(procedure|function)\s+([a-zA-Z0-9_]+)',
            re.IGNORECASE
        )

        for match in pattern.finditer(clean_code):
            kind = match.group(1).lower()
            name = match.group(2).lower()

            # Now we need to find the semicolon that ends the declaration.
            # But we must be careful about nested parentheses.
            pos = match.end()
            rest = ""
            stack = 0
            found_semicolon = False
            for i in range(pos, len(clean_code)):
                char = clean_code[i]
                if char == '(':
                    stack += 1
                elif char == ')':
                    if stack > 0:
                        stack -= 1
                elif char == ';' and stack == 0:
                    rest = clean_code[pos:i].strip()
                    end_pos = i + 1
                    found_semicolon = True
                    break

            if not found_semicolon:
                continue

            # Parse 'rest' into params and return_type
            params = ""
            ret_type = ""

            if rest.startswith('('):
                # Find matching parenthesis in 'rest'
                p_stack = 0
                for i, char in enumerate(rest):
                    if char == '(':
                        p_stack += 1
                    elif char == ')':
                        p_stack -= 1
                        if p_stack == 0:
                            params = rest[:i+1]
                            after_params = rest[i+1:].strip()
                            if after_params.startswith(':'):
                                ret_type = after_params[1:].strip()
                            break
            elif rest.startswith(':'):
                ret_type = rest[1:].strip()

            # Check for forward or external immediately following
            remaining = clean_code[end_pos:].strip()
            directive = None
            first_word_match = re.match(r'^([a-zA-Z0-9_]+)', remaining)
            if first_word_match:
                first_word = first_word_match.group(1).lower()
                if first_word in ('forward', 'external'):
                    directive = first_word

            signatures.append({
                'kind': kind,
                'name': name,
                'params': self.normalizer.normalize_whitespace(params),
                'return_type': self.normalizer.normalize_whitespace(ret_type),
                'directive': directive,
                'full_signature': self.normalizer.normalize_whitespace(clean_code[match.start():end_pos])
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
