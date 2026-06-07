import sys
import argparse
from pathlib import Path
import re

# Add current directory to path to import other harness modules
sys.path.append(str(Path(__file__).parent))

from web_module_extractor import extract_web_modules
from pascal_routine_extractor import PascalRoutineExtractor

def normalize_name(name):
    """Normalizes routine names by lowercasing and removing underscores."""
    return name.lower().replace('_', '')

def normalize_signature_component(comp):
    """Normalizes parameter lists or return types for comparison."""
    if not comp:
        return ""
    # Lowercase and normalize whitespace
    comp = comp.lower()
    comp = re.sub(r'\s+', '', comp).strip()
    # Remove underscores from identifiers inside the component
    comp = comp.replace('_', '')
    # Map common WEB-specific type aliases to standard Pascal types for comparison
    comp = comp.replace('textfile', 'text')
    # Remove @! and @+ and other WEB markers if they leaked in
    comp = re.sub(r'@[!+@\>\<\\]', '', comp)
    return comp

def verify_signatures(web_file, pascal_file):
    """Compares routine signatures between WEB and Pascal source."""
    web_routines = extract_web_modules(web_file)

    try:
        with open(pascal_file, 'r', encoding='utf-8', errors='ignore') as f:
            pascal_code = f.read()
    except Exception as e:
        print(f"Error reading {pascal_file}: {e}")
        return None

    pascal_extractor = PascalRoutineExtractor()
    pascal_routines = pascal_extractor.extract_signatures(pascal_code)

    # Normalize Pascal routines for easier lookup
    pascal_map = {}
    for p in pascal_routines:
        norm_name = normalize_name(p['name'])
        if norm_name not in pascal_map:
            pascal_map[norm_name] = []
        pascal_map[norm_name].append(p)

    results = {
        'matched': [],
        'missing': [],
        'mismatched_kind': [],
        'mismatched_params': [],
        'mismatched_return': [],
        'extra_pascal': []
    }

    matched_pascal_names = set()

    for w in web_routines:
        norm_name = normalize_name(w['name'])
        if norm_name in pascal_map:
            matched_pascal_names.add(norm_name)
            # Find an implementation (non-forward) if possible
            implementations = [p for p in pascal_map[norm_name] if p['directive'] != 'forward']
            if implementations:
                p = implementations[0]
            else:
                p = pascal_map[norm_name][0]

            w_params = normalize_signature_component(w['params'])
            p_params = normalize_signature_component(p['params'])
            w_ret = normalize_signature_component(w['return_type'])
            p_ret = normalize_signature_component(p['return_type'])

            if w['kind'] != p['kind']:
                results['mismatched_kind'].append((w, p))
            elif w_params != p_params:
                results['mismatched_params'].append((w, p))
            elif w_ret != p_ret:
                results['mismatched_return'].append((w, p))
            else:
                results['matched'].append((w, p))
        else:
            results['missing'].append(w)

    for norm_name, ps in pascal_map.items():
        if norm_name not in matched_pascal_names:
            results['extra_pascal'].append(ps[0])

    return results

def main():
    parser = argparse.ArgumentParser(description="Verify routine signatures between WEB and Pascal")
    parser.add_argument("web_file", help="Path to the .web file")
    parser.add_argument("pascal_file", help="Path to the .p file")

    args = parser.parse_args()

    results = verify_signatures(args.web_file, args.pascal_file)
    if results is None:
        sys.exit(1)

    print(f"--- Verification Results for {args.web_file} vs {args.pascal_file} ---")
    print(f"Matched: {len(results['matched'])}")

    if results['missing']:
        print(f"\nMissing in Pascal ({len(results['missing'])}):")
        for w in results['missing']:
            print(f"  Module {w['module']:4}: {w['kind'].capitalize():9} {w['name']}")

    if results['mismatched_kind']:
        print(f"\nKind Mismatch ({len(results['mismatched_kind'])}):")
        for w, p in results['mismatched_kind']:
            print(f"  {w['name']}: WEB={w['kind']}, Pascal={p['kind']}")

    if results['mismatched_params']:
        print(f"\nParameter Mismatch ({len(results['mismatched_params'])}):")
        for w, p in results['mismatched_params']:
            print(f"  {w['name']}:")
            print(f"    WEB:    {w['params']}")
            print(f"    Pascal: {p['params']}")

    if results['mismatched_return']:
        print(f"\nReturn Type Mismatch ({len(results['mismatched_return'])}):")
        for w, p in results['mismatched_return']:
            print(f"  {w['name']}:")
            print(f"    WEB:    {w['return_type']}")
            print(f"    Pascal: {p['return_type']}")

    if results['extra_pascal']:
        print(f"\nExtra in Pascal (potentially from change file) ({len(results['extra_pascal'])}):")
        for p in results['extra_pascal']:
            sig = f"{p['kind'].capitalize()} {p['name']}"
            if p['params']: sig += f" {p['params']}"
            if p['return_type']: sig += f": {p['return_type']}"
            print(f"  {sig}")

if __name__ == "__main__":
    main()
