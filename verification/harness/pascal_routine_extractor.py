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
            # This version handles {} comments that might start with a { even if they are commented out by another {}
            # TANGLE output often has {n:} which are comments.
            # But sometimes we have { {n:} procedure ... }

            result = []
            stack = 0
            i = 0
            while i < len(code):
                if code[i] == '{':
                    stack += 1
                elif code[i] == '}':
                    if stack > 0: stack -= 1
                elif stack == 0:
                    # Also handle (* *) comments
                    if code[i:i+2] == '(*':
                        j = code.find('*)', i+2)
                        if j != -1:
                            i = j + 2
                            continue
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
        # IMPORTANT: We need to strip comments but TANGLE sometimes puts procedures INSIDE comments if they are @!debug
        # Wait, if they are @!debug, and debug is NOT defined, they are commented out in Pascal.
        # If we WANT to match them, we should maybe NOT strip comments, or strip them selectively.
        # But usually we only care about what's actually in the Pascal.

        # However, looking at tangle.p, the debug procedures ARE there but wrapped in {}.
        # If we want to verify they exist even if commented out, we should handle that.

        # Let's try to "uncomment" TANGLE module markers and debug blocks for signature extraction purposes.
        # Module markers are {n:} and {:n}.
        code = re.sub(r'\{(\d+):\}', ' ', code)
        code = re.sub(r'\{:(\d+)\}', ' ', code)

        # If we see {procedure ... } we might want to treat it as a procedure.
        # Let's just strip the outer {} if it contains procedure/function.
        def uncomment_routines(m):
            inner = m.group(1)
            if re.search(r'\b(procedure|function)\b', inner, re.IGNORECASE):
                return inner
            return ' '

        # This is a bit risky but let's try to match balanced {} that contain procedure/function
        # For simplicity, just replace '{' with ' ' and '}' with ' ' if they seem to wrap a routine.
        # Actually, let's just strip ALL {} but keep their content if it contains procedure/function.
        # Better: just treat { and } as whitespace for the purpose of signature extraction!
        # In Pascal, { and } are comments, so this is NOT standard.
        # But TANGLE uses them for both comments AND for "commenting out" code.

        # If we treat { and } as whitespace, we might pick up procedures in real comments.
        # But in TANGLE output, there aren't many real comments other than the ones we want.

        clean_code = self.normalizer.strip_strings(code)
        clean_code = clean_code.replace('{', ' ').replace('}', ' ')
        clean_code = re.sub(r'\(\*.*?\*\)', ' ', clean_code, flags=re.DOTALL)

        # Replace newlines and multiple spaces with a single space to simplify regex matching
        clean_code = re.sub(r'\s+', ' ', clean_code)

        signatures = []

        # Improved regex to handle parameter lists that may contain semicolons
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
