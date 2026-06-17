import sys
import argparse
from verification.harness.identify_gotos import identify_gotos
from verification.harness.identify_pascal_gotos import PascalGOTOExtractor

def verify_gotos(web_file, pascal_file):
    print(f"Comparing GOTO transitions: {web_file} vs {pascal_file}")

    web_gotos, web_labels, web_macros = identify_gotos(web_file)

    pascal_extractor = PascalGOTOExtractor()
    pascal_gotos, pascal_labels = pascal_extractor.identify_gotos(pascal_file)

    # Normalize labels and targets for comparison (lowercase)
    for g in web_gotos:
        g['target'] = str(g['target']).lower()
    for l in web_labels:
        l['label'] = str(l['label']).lower()
    for g in pascal_gotos:
        g['target'] = str(g['target']).lower()
    for l in pascal_labels:
        l['label'] = str(l['label']).lower()

    # Group WEB gotos by module and target
    web_grouped = {}
    for g in web_gotos:
        key = (g['module'], g['target'])
        if key not in web_grouped:
            web_grouped[key] = []
        web_grouped[key].append(g)

    mismatches = 0
    matches = 0

    print(f"\nVerifying {len(pascal_gotos)} GOTOs in Pascal source...")

    # Track used WEB gotos to identify potential extras in WEB
    used_web_keys = set()

    # Global labels in WEB (like 9999 in TANGLE) might be used in any module
    web_global_labels = {l['label'] for l in web_labels if l['module'] <= 2} # Heuristic for global labels

    for pg in pascal_gotos:
        module = pg['module']
        target = pg['target']

        if module is None:
            # GOTO outside any module marker? Check if it's a known global goto
            # In TANGLE, jump_out might be after module 34 but the goto is within it.
            pass

        key = (module, target)
        if key in web_grouped:
            matches += 1
            used_web_keys.add(key)
        else:
            # Check if it targets a label that is declared in WEB (global or same module)
            found_in_web = False
            for wg_key in web_grouped:
                # If target matches and it's a known global label, we might allow it
                # even if module number is slightly off due to TANGLE's module merging
                if wg_key[1] == target:
                    # If target is global label (like 9999), we can be lenient about module
                    if target in web_global_labels or target == '9999':
                        found_in_web = True
                        used_web_keys.add(wg_key)
                        break

            if found_in_web:
                matches += 1
            else:
                print(f"  MISMATCH: Module {module}, Target {target:10} (Pascal line {pg['line']}) NOT found in WEB")
                mismatches += 1

    print(f"\nVerification Summary:")
    print(f"  Total Pascal GOTOs: {len(pascal_gotos)}")
    print(f"  Matches:            {matches}")
    print(f"  Mismatches:         {mismatches}")

    # Check for WEB gotos NOT found in Pascal
    missing_in_pascal = 0
    for key, gotos in web_grouped.items():
        if key not in used_web_keys:
            missing_in_pascal += 1

    if missing_in_pascal > 0:
        print(f"  WEB GOTOs not in Pascal: {missing_in_pascal} (often due to macros or conditional code)")

    return mismatches == 0

def main():
    parser = argparse.ArgumentParser(description="Compare GOTO transitions between WEB and Pascal.")
    parser.add_argument("web_file", help="Path to the WEB file")
    parser.add_argument("pascal_file", help="Path to the Pascal file")

    args = parser.parse_args()

    success = verify_gotos(args.web_file, args.pascal_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
