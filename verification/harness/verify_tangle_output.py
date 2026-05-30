import re
import sys

class PascalNormalizer:
    """Utility to normalize Pascal source code by removing comments and normalizing whitespace."""

    def strip_comments(self, code):
        """
        Removes Pascal comments from the code.
        Pascal comments can be { ... } or (* ... *).
        Handles nested { ... } comments.
        """
        # Remove (* ... *) comments first (they don't typically nest)
        code = re.sub(r'\(\*.*?\*\)', '', code, flags=re.DOTALL)

        # Handle { } comments with a stack to support nesting
        result = []
        stack = 0
        i = 0
        while i < len(code):
            if code[i] == '{':
                stack += 1
            elif code[i] == '}':
                if stack > 0:
                    stack -= 1
                else:
                    # Unmatched closing brace, keep it?
                    # In standard Pascal this might be an error, but we'll just keep it.
                    result.append(code[i])
            elif stack == 0:
                result.append(code[i])
            i += 1

        return "".join(result)

    def normalize_whitespace(self, code):
        """Replaces multiple whitespace characters with a single space and strips leading/trailing whitespace."""
        return re.sub(r'\s+', ' ', code).strip()

class TangleValidator:
    """Validator for TANGLE output (Pascal source)."""

    def __init__(self, pascal_code):
        self.normalizer = PascalNormalizer()
        self.clean_code = self.normalizer.normalize_whitespace(
            self.normalizer.strip_comments(pascal_code)
        )

    def extract_constants(self):
        """
        Extracts constant definitions from the Pascal code.
        Looks for the 'const' section and parses 'name = value;' pairs.
        """
        constants = {}
        # Find the const section. In Pascal, it usually starts with 'const' and ends with 'type', 'var', or 'begin'.
        # We'll use a simpler approach: find all 'name = value;' patterns after 'const' but before 'type' or 'var'.
        const_match = re.search(r'\bconst\b(.*?)\b(type|var|begin)\b', self.clean_code, re.IGNORECASE)
        if const_match:
            const_section = const_match.group(1)
            # Find name = value; pairs.
            # Note: value could be numeric or a string literal or even an expression, but for TANGLE output
            # we mostly care about the numeric ones expanded from macros.
            matches = re.findall(r'(\w+)\s*=\s*(.*?);', const_section)
            for name, value in matches:
                constants[name.strip()] = value.strip()

        return constants

    def verify_macro_expansion(self, expected_macros):
        """
        Verifies that specific macros have been expanded to the expected values in the Pascal constants.

        :param expected_macros: A dictionary of {macro_name: expected_value}.
        :return: A list of (macro_name, actual_value, expected_value, success).
        """
        actual_constants = self.extract_constants()
        results = []
        for name, expected_value in expected_macros.items():
            actual_value = actual_constants.get(name)
            success = (actual_value == str(expected_value))
            results.append((name, actual_value, str(expected_value), success))

        return results

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 verify_tangle_output.py <pascal_file> <macro_name=value> [<macro_name=value> ...]")
        sys.exit(1)

    pascal_file = sys.argv[1]
    expected_macros = {}
    for arg in sys.argv[2:]:
        if '=' in arg:
            name, value = arg.split('=', 1)
            expected_macros[name] = value

    with open(pascal_file, 'r') as f:
        code = f.read()

    validator = TangleValidator(code)
    results = validator.verify_macro_expansion(expected_macros)

    all_ok = True
    for name, actual, expected, success in results:
        status = "OK" if success else "FAILED"
        print(f"Macro {name}: expected {expected}, got {actual} -> {status}")
        if not success:
            all_ok = False

    if not all_ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
