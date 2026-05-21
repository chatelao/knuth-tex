#!/usr/bin/env python3
import argparse
import sys
import yaml
import os

def load_config(config_path):
    """Loads and parses the YAML configuration file."""
    if not os.path.exists(config_path):
        print(f"Error: Configuration file not found at {config_path}")
        sys.exit(1)

    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML configuration: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading config: {e}")
        sys.exit(1)

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

    config = load_config(args.config)
    print(f"Harness initialized with config from: {args.config}")

    if args.test_id:
        print(f"Targeting specific tests: {', '.join(args.test_id)}")
    else:
        print("No specific tests specified; running all applicable tests.")

if __name__ == "__main__":
    main()
