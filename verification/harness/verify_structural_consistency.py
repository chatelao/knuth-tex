import re
import sys
from pathlib import Path

class StructuralConsistencyValidator:
    """Validator for structural consistency between WEB and TANGLE-generated Pascal."""

    def __init__(self, web_file, pascal_file):
        self.web_file = Path(web_file)
        self.pascal_file = Path(pascal_file)

    def identify_web_code_modules(self):
        """Identifies modules in the WEB file that contain Pascal code."""
        try:
            with open(self.web_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {self.web_file}: {e}")
            return set()

        # Modules start with @ followed by space, tab, newline or *
        module_regex = re.compile(r'^@[\s\*]', re.MULTILINE)
        module_starts = [m.start() for m in module_regex.finditer(content)]

        code_modules = set()
        for i, start in enumerate(module_starts):
            module_num = i + 1
            end = module_starts[i+1] if i+1 < len(module_starts) else len(content)
            module_content = content[start:end]

            # Check if this module contains a Pascal block: @p or @<Named module@>=
            # We look for @p or @<Name@>=
            # They usually start a line, but sometimes they follow @d or @f in the same module.
            # In TANGLE output, modules containing @p or @<...@>= are marked.
            if re.search(r'\n@p|^@p', module_content):
                code_modules.add(module_num)
            elif re.search(r'\n@<[^@]*@>=|^@<[^@]*@>=', module_content):
                code_modules.add(module_num)

        return code_modules

    def extract_pascal_module_markers(self):
        """Extracts module start {n:} and end {:n} markers from the Pascal file."""
        try:
            with open(self.pascal_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {self.pascal_file}: {e}")
            return [], []

        # Find all {n:} markers
        starts = re.findall(r'{(\d+):}', content)
        # Find all {:n} markers
        ends = re.findall(r'{:(\d+)}', content)

        return [int(n) for n in starts], [int(n) for n in ends]

    def verify_consistency(self):
        """Verifies that all code-bearing WEB modules are represented in Pascal."""
        web_modules = self.identify_web_code_modules()
        p_starts, p_ends = self.extract_pascal_module_markers()
        p_modules = set(p_starts)

        missing = web_modules - p_modules
        extra = p_modules - web_modules

        # Check for balancing
        from collections import Counter
        start_counts = Counter(p_starts)
        end_counts = Counter(p_ends)

        unbalanced = []
        all_p_modules = set(p_starts) | set(p_ends)
        for m in sorted(all_p_modules):
            if start_counts[m] != end_counts[m]:
                unbalanced.append((m, start_counts[m], end_counts[m]))

        return {
            'web_count': len(web_modules),
            'pascal_count': len(p_modules),
            'missing': sorted(list(missing)),
            'extra': sorted(list(extra)),
            'unbalanced': unbalanced,
            'success': len(missing) == 0 and len(unbalanced) == 0
        }

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 verify_structural_consistency.py <web_file> <pascal_file>")
        sys.exit(1)

    web_file = sys.argv[1]
    pascal_file = sys.argv[2]

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    results = validator.verify_consistency()

    print(f"WEB code modules identified: {results['web_count']}")
    print(f"Pascal module markers found: {results['pascal_count']}")

    if results['missing']:
        print(f"FAIL: Missing modules in Pascal: {results['missing']}")

    if results['unbalanced']:
        print("FAIL: Unbalanced module markers (Start vs End):")
        for m, s, e in results['unbalanced']:
            print(f"  Module {m}: {s} starts, {e} ends")

    if results['success']:
        print("SUCCESS: Structural consistency verified.")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
