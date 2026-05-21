#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="TeX and Metafont Verification Test Harness")

    parser.add_argument(
        "--config",
        type=str,
        help="Path to the harness configuration file (YAML)"
    )

    parser.add_argument(
        "--test-id",
        action="append",
        help="Specific test ID(s) to run. Can be specified multiple times."
    )

    args = parser.parse_args()

    if not args.config:
        print("Error: Configuration file is required.")
        parser.print_help()
        sys.exit(1)

    print(f"Harness initialized with config: {args.config}")
    if args.test_id:
        print(f"Targeting specific tests: {', '.join(args.test_id)}")
    else:
        print("No specific tests specified; running all applicable tests.")

if __name__ == "__main__":
    main()
