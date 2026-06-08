import sys
import os
from pathlib import Path

# Add the current directory to sys.path to allow importing extractors
sys.path.append(str(Path(__file__).parent))

from web_module_extractor import extract_web_modules
from pascal_routine_extractor import PascalRoutineExtractor

def normalize_name(name):
    """Removes underscores and converts to lowercase for matching."""
    return name.lower().replace('_', '')

def compare_signatures(web_file, pascal_file):
    """
    Compares routine signatures between a WEB file and its generated Pascal file.
    Returns a list of mismatches.
    """
    web_routines = extract_web_modules(web_file)

    extractor = PascalRoutineExtractor()
    with open(pascal_file, 'r', encoding='utf-8', errors='ignore') as f:
        pascal_content = f.read()
    pascal_signatures = extractor.extract_signatures(pascal_content)

    # Index Pascal signatures by normalized name
    pascal_map = {}
    for sig in pascal_signatures:
        norm_name = normalize_name(sig['name'])
        if norm_name not in pascal_map:
            pascal_map[norm_name] = []
        pascal_map[norm_name].append(sig)

    mismatches = []
    matches = []

    for web_rt in web_routines:
        norm_name = normalize_name(web_rt['name'])
        if norm_name not in pascal_map:
            mismatches.append({
                'type': 'missing_in_pascal',
                'name': web_rt['name'],
                'module': web_rt['module'],
                'kind': web_rt['kind']
            })
        else:
            # Find a match by kind
            found_match = False
            for p_sig in pascal_map[norm_name]:
                if p_sig['kind'] == web_rt['kind']:
                    matches.append((web_rt, p_sig))
                    found_match = True
                    # Remove from map or mark as used if we want to find extra Pascal routines
                    break

            if not found_match:
                mismatches.append({
                    'type': 'kind_mismatch',
                    'name': web_rt['name'],
                    'module': web_rt['module'],
                    'web_kind': web_rt['kind'],
                    'pascal_kind': pascal_map[norm_name][0]['kind'] # Just take the first one
                })

    # Optional: Find routines in Pascal that are not in WEB (not strictly required by roadmap but useful)
    # web_norm_names = {normalize_name(rt['name']) for rt in web_routines}
    # for p_name, p_sigs in pascal_map.items():
    #     if p_name not in web_norm_names:
    #         for p_sig in p_sigs:
    #             mismatches.append({
    #                 'type': 'extra_in_pascal',
    #                 'name': p_sig['name'],
    #                 'kind': p_sig['kind']
    #             })

    return matches, mismatches

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 compare_signatures.py <web_file> <pascal_file>")
        sys.exit(1)

    web_file = sys.argv[1]
    pascal_file = sys.argv[2]

    print(f"Comparing {web_file} and {pascal_file}...")
    matches, mismatches = compare_signatures(web_file, pascal_file)

    print(f"Found {len(matches)} matches.")
    if not mismatches:
        print("No signature mismatches found!")
    else:
        print(f"Found {len(mismatches)} mismatches:")
        for m in mismatches:
            if m['type'] == 'missing_in_pascal':
                print(f"  [MISSING] {m['kind'].capitalize()} '{m['name']}' (Module {m['module']}) not found in Pascal.")
            elif m['type'] == 'kind_mismatch':
                print(f"  [MISMATCH] '{m['name']}' (Module {m['module']}) is {m['web_kind']} in WEB but {m['pascal_kind']} in Pascal.")
            elif m['type'] == 'extra_in_pascal':
                print(f"  [EXTRA] {m['kind'].capitalize()} '{m['name']}' found in Pascal but not in WEB.")

if __name__ == "__main__":
    main()
