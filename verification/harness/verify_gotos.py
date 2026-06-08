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
        g['target'] = g['target'].lower()
    for l in web_labels:
        l['label'] = l['label'].lower()
    for g in pascal_gotos:
        g['target'] = g['target'].lower()
    for l in pascal_labels:
        l['label'] = l['label'].lower()

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

    for pg in pascal_gotos:
        module = pg['module']
        target = pg['target']

        # In Pascal, numeric labels are preserved, but identifiers might be changed.
        # However, TANGLE usually preserves labels unless they are macros.
        # If it's a macro in WEB, we already resolved it in identify_gotos.

        key = (module, target)
        if key in web_grouped:
            matches += 1
            used_web_keys.add(key)
            # print(f"  OK: Module {module:4}, Target {target:10} (Pascal line {pg['line']})")
        else:
            # Try to see if it targets a label that is declared in the same module in WEB
            # sometimes the target name might be slightly different?
            # Actually TANGLE is quite consistent with labels.
            print(f"  MISMATCH: Module {module:4}, Target {target:10} (Pascal line {pg['line']}) NOT found in WEB module {module}")
            mismatches += 1

    print(f"\nVerification Summary:")
    print(f"  Total Pascal GOTOs: {len(pascal_gotos)}")
    print(f"  Matches:            {matches}")
    print(f"  Mismatches:         {mismatches}")

    # Check for WEB gotos NOT found in Pascal
    # This might happen if they are in dead code or handled differently by TANGLE (e.g. constant folding if possible, but unlikely for gotos)
    missing_in_pascal = 0
    for key, gotos in web_grouped.items():
        if key not in used_web_keys:
            for g in gotos:
                # Some modules might be skipped by TANGLE or macros might not be expanded if not used.
                # print(f"  INFO: WEB GOTO in Module {g['module']:4}, Target {g['target']:10} (Line {g['line']:5}) not found in Pascal.")
                missing_in_pascal += 1

    if missing_in_pascal > 0:
        print(f"  WEB GOTOs not in Pascal: {missing_in_pascal} (often due to macros or conditional code)")

    return mismatches == 0

def main():
    parser = argparse.ArgumentParser(description="Compare GOTO transitions between WEB and Pascal.")
    parser.get_default("web_file")
    parser.add_argument("web_file", help="Path to the WEB file")
    parser.add_argument("pascal_file", help="Path to the Pascal file")

    args = parser.parse_args()

    success = verify_gotos(args.web_file, args.pascal_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
