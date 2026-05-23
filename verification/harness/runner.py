#!/usr/bin/env python3
import argparse
import sys
import yaml
import os
import logging
from pathlib import Path
from verification.harness.tangle import TangleWrapper

class VerificationTestRunner:
    """Orchestrates the execution of a single verification test."""

    def __init__(self, harness_config, test_config_path):
        """
        Initialize the TestRunner.

        :param harness_config: Parsed harness configuration (dict).
        :param test_config_path: Path to the test's test_config.yaml.
        """
        self.harness_config = harness_config
        self.test_config_path = Path(test_config_path)
        self.test_dir = self.test_config_path.parent
        self.test_config = self.load_test_config()
        self.test_id = self.test_config.get('test_id', self.test_dir.name)

        # Setup output directory for this specific test
        base_output_dir = Path(harness_config.get('output_dir', 'verification/results'))
        self.output_dir = base_output_dir / self.test_id
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_test_config(self):
        """Loads the test-specific configuration."""
        with open(self.test_config_path, 'r') as f:
            return yaml.safe_load(f)

    def run_tangle(self):
        """Executes the Tangle step for the test."""
        logging.info(f"[{self.test_id}] Starting Tangle step...")

        tangle_exe = self.harness_config.get('tangle_path')
        if not tangle_exe:
            raise ValueError("tangle_path not specified in harness configuration.")

        wrapper = TangleWrapper(tangle_exe)

        source_web = self.test_config.get('source_web')
        change_file = self.test_config.get('change_file')

        if not source_web:
            raise ValueError(f"source_web not specified in test config: {self.test_config_path}")

        pascal_file = self.output_dir / f"{self.test_id}.p"
        pool_file = self.output_dir / f"{self.test_id}.pool"

        return wrapper.run(
            web_file=source_web,
            change_file=change_file,
            pascal_file=str(pascal_file),
            pool_file=str(pool_file)
        )

    def run(self):
        """Runs the full verification workflow for this test."""
        logging.info(f"--- Running Test: {self.test_id} ---")
        try:
            pascal_file, pool_file = self.run_tangle()
            logging.info(f"[{self.test_id}] Tangle step completed: {pascal_file}, {pool_file}")
            # Other steps (Compile, Execute, Compare) will be added here later
            return True
        except Exception as e:
            logging.error(f"[{self.test_id}] Test failed: {e}")
            return False

def discover_tests(tests_base_dir):
    """Discovers all tests by looking for test_config.yaml files."""
    test_configs = list(Path(tests_base_dir).rglob("test_config.yaml"))
    logging.info(f"Discovered {len(test_configs)} tests in {tests_base_dir}")
    return test_configs

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

    # Discover tests
    tests_base_dir = config.get('tests_dir', 'verification/tests')
    test_config_paths = discover_tests(tests_base_dir)

    if args.test_id:
        logging.info(f"Targeting specific tests: {', '.join(args.test_id)}")
        test_config_paths = [p for p in test_config_paths if any(tid in str(p) for tid in args.test_id)]
        logging.info(f"Filtered to {len(test_config_paths)} tests.")

    success_count = 0
    total_count = len(test_config_paths)

    for config_path in test_config_paths:
        runner = VerificationTestRunner(config, config_path)
        if runner.run():
            success_count += 1

    logging.info(f"Verification process completed. {success_count}/{total_count} tests passed.")

    if success_count < total_count:
        sys.exit(1)

if __name__ == "__main__":
    main()
