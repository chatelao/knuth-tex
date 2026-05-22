#!/usr/bin/env python3
import argparse
import sys
import yaml
import os
import logging
from pathlib import Path

def setup_logging(output_dir):
    """Configures logging to both console and a file."""
    log_dir = Path(output_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "harness.log"

    # Configure the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Clear existing handlers if any (useful for re-initialization)
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file)
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logging.info(f"Logging initialized. Log file: {log_file}")

def load_config(config_path):
    """Loads and parses the YAML configuration file."""
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found at {config_path}")
        sys.exit(1)

    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        logging.error(f"Failed to parse YAML configuration: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading config: {e}")
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
        # Before logging is setup, we use print/stderr for CLI errors
        print("Error: Configuration file is required.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    config = load_config(args.config)

    # Initialize logging using output_dir from config
    output_dir = config.get('output_dir', 'verification/results')
    setup_logging(output_dir)

    logging.info(f"Harness initialized with config from: {args.config}")

    if args.test_id:
        logging.info(f"Targeting specific tests: {', '.join(args.test_id)}")
    else:
        logging.info("No specific tests specified; running all applicable tests.")

if __name__ == "__main__":
    main()
