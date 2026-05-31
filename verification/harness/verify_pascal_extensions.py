import re
import os
from pathlib import Path

class PascalExtensionValidator:
    """Validator for Pascal system extensions (argc, argv, etc.) in source and headers."""

    def __init__(self, pascal_file, header_file=None):
        self.pascal_file = Path(pascal_file)
        self.header_file = Path(header_file) if header_file else None

        with open(self.pascal_file, 'r') as f:
            self.pascal_code = f.read()

        self.header_code = ""
        if not self.header_file:
            # Try to find header in #include
            match = re.search(r'#include\s+"([^"]+)"', self.pascal_code)
            if match:
                header_name = match.group(1)
                potential_header = self.pascal_file.parent / header_name
                if potential_header.exists():
                    self.header_file = potential_header

        if self.header_file and self.header_file.exists():
            with open(self.header_file, 'r') as f:
                self.header_code = f.read()

    def check_declaration(self, identifier):
        """Checks if an identifier is declared in the header or pascal file (as external)."""
        # Look for identifier:asmname or procedure/function identifier ... external
        patterns = [
            rf'\b{identifier}\s*:\s*asmname',
            rf'\bprocedure\s+{identifier}\b.*?\bexternal\b',
            rf'\bfunction\s+{identifier}\b.*?\bexternal\b',
            rf'\b{identifier}\s*:\s*external\b'
        ]

        for pattern in patterns:
            if re.search(pattern, self.header_code, re.IGNORECASE | re.DOTALL):
                return True
            if re.search(pattern, self.pascal_code, re.IGNORECASE | re.DOTALL):
                return True
        return False

    def check_usage(self, identifier):
        """Checks if an identifier is used in the Pascal code (outside of declarations)."""
        # This is a bit simplified; we just look for the word itself.
        # To avoid catching declarations, we could be more specific, but for these
        # system extensions, any occurrence after 'begin' is likely usage.

        # Find the first 'begin' of the main program or any procedure
        usage_code = self.pascal_code

        # Simple check: is it present?
        # We use word boundaries to avoid matching identifiers that contain the target.
        if re.search(rf'\b{identifier}\b', usage_code, re.IGNORECASE):
            # Try to see if it's used in a context that isn't a declaration
            # Declarations usually have 'external', 'asmname', or are followed by ':' in a var/type section.

            # If it's used in an expression or as a procedure call:
            use_patterns = [
                rf':=\s*{identifier}\b',           # Assignment source
                rf'\b{identifier}\s*\(',            # Procedure call with args
                rf'\b{identifier}\s*;',             # Standalone procedure call
                rf'\b{identifier}\s+then\b',        # If condition
                rf'\b{identifier}\s*[<>]=?',       # Comparison operators
                rf'\b{identifier}\s*[-+*/]',        # Arithmetic
                rf'=\s*{identifier}\b',            # Comparison
                rf'\b{identifier}\s*=',            # Comparison
                rf'to\s+{identifier}\s+do',        # For loop limit
                rf'\[{identifier}\]',              # Array index
            ]
            for pattern in use_patterns:
                if re.search(pattern, usage_code, re.IGNORECASE):
                    return True

            # Special case for argc in for loop
            if re.search(rf'for\s+\w+\s*:=\s*\d+\s+to\s+{identifier}\b', usage_code, re.IGNORECASE):
                return True

        return False

    def verify_extension(self, identifier):
        """Verifies both declaration and usage of an extension."""
        declared = self.check_declaration(identifier)
        used = self.check_usage(identifier)
        return declared, used

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Pascal extension validator")
    parser.add_argument("pascal_file", help="Path to the Pascal file")
    parser.add_argument("--header", help="Path to the header file (optional)")
    parser.add_argument("--extensions", nargs="+", default=["argc", "argv"], help="Extensions to check")

    args = parser.parse_args()

    validator = PascalExtensionValidator(args.pascal_file, args.header)
    all_ok = True

    for ext in args.extensions:
        declared, used = validator.verify_extension(ext)
        status_dec = "OK" if declared else "MISSING"
        status_use = "OK" if used else "NOT USED"
        print(f"Extension {ext}: Declaration={status_dec}, Usage={status_use}")
        if not declared:
            all_ok = False
        # Usage is not strictly required for all extensions in all files, but usually expected for argc/argv
        if ext in ["argc", "argv"] and not used:
            # Some files might not use them if they don't take arguments, but tangle/weave do.
            pass

    if not all_ok:
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
