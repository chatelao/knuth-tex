#!/usr/bin/env python3
import argparse
import sys
import yaml
import os
import shutil
import logging
from pathlib import Path
from verification.harness.tangle import TangleWrapper
from verification.harness.compiler import CompileWrapper
from verification.harness.executor import ExecuteWrapper
from verification.harness.comparer import Comparer
from verification.harness.normalizer import Normalizer
from verification.harness.dvitype import DVItypeWrapper
from verification.harness.gftype import GFtypeWrapper
from verification.harness.pktype import PKtypeWrapper
from verification.harness.tftopl import TFtoPLWrapper
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import Parser
from verification.harness.mcdc.instrumenter import Instrumenter, PascalEmitter
from verification.harness.mcdc.report_generator import MCDCReportGenerator

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
        self.mcdc_enabled = harness_config.get('mcdc', False)
        self.mcdc_decisions = {}

        # Setup output directory for this specific test
        base_output_dir = Path(harness_config.get('output_dir', 'verification/results'))
        self.output_dir = base_output_dir / self.test_id
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize core utilities
        self.comparer = Comparer()
        self.normalizer = Normalizer()

        # Initialize symbolic comparators from harness config
        self.symbolic_comparators = {}
        if 'dvitype_path' in harness_config:
            self.symbolic_comparators['dvi'] = DVItypeWrapper(harness_config['dvitype_path'])
        if 'gftype_path' in harness_config:
            self.symbolic_comparators['gf'] = GFtypeWrapper(harness_config['gftype_path'])
        if 'pktype_path' in harness_config:
            self.symbolic_comparators['pk'] = PKtypeWrapper(harness_config['pktype_path'])
        if 'tftopl_path' in harness_config:
            self.symbolic_comparators['tfm'] = TFtoPLWrapper(harness_config['tftopl_path'])

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

    def run_instrumentation(self, pascal_file):
        """Instruments the Pascal file for MC/DC coverage."""
        logging.info(f"[{self.test_id}] Starting MC/DC instrumentation...")

        with open(pascal_file, 'r') as f:
            code = f.read()

        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse_program()

        instrumenter = Instrumenter()
        instrumented_ast = instrumenter.instrument(ast)
        self.mcdc_decisions = instrumenter.decisions

        emitter = PascalEmitter()
        instrumented_code = emitter.emit(instrumented_ast)

        # Prepend include for runtime
        instrumented_code = '#include "runtime.p"\n' + instrumented_code

        instrumented_pascal = Path(pascal_file).with_suffix('.mcdc.p')
        with open(instrumented_pascal, 'w') as f:
            f.write(instrumented_code)

        return str(instrumented_pascal)

    def generate_mcdc_report(self):
        """Generates the MC/DC coverage report."""
        logging.info(f"[{self.test_id}] Generating MC/DC coverage report...")
        log_file = self.output_dir / "mcdc_coverage.out"
        if not log_file.exists():
            logging.warning(f"[{self.test_id}] MC/DC log file not found: {log_file}")
            return

        generator = MCDCReportGenerator(self.mcdc_decisions)
        report = generator.generate_report(str(log_file))

        # Save YAML report
        report_yaml = self.output_dir / "mcdc_report.yaml"
        generator.save_report_yaml(report, str(report_yaml))

        # Save text summary
        report_txt = self.output_dir / "mcdc_report.txt"
        with open(report_txt, 'w') as f:
            f.write(generator.format_summary(report))

        logging.info(f"[{self.test_id}] MC/DC report generated: {report_txt}")

    def run_compile(self, pascal_file):
        """Executes the Compile step for the test."""
        logging.info(f"[{self.test_id}] Starting Compile step...")

        compiler_exe = self.harness_config.get('pascal_compiler')
        if not compiler_exe:
            raise ValueError("pascal_compiler not specified in harness configuration.")

        wrapper = CompileWrapper(compiler_exe)
        output_exe = self.output_dir / self.test_id

        return wrapper.run(
            pascal_file=pascal_file,
            output_exe=str(output_exe)
        )

    def run_setup(self):
        """Copies required files to the test execution directory."""
        setup_files = self.test_config.get('setup_files', [])
        if self.mcdc_enabled:
            setup_files.append('verification/harness/mcdc/runtime.p')

        if not setup_files:
            return

        logging.info(f"[{self.test_id}] Running setup step (copying files)...")
        for src in setup_files:
            src_path = Path(src)
            if not src_path.exists():
                logging.warning(f"[{self.test_id}] Setup file not found: {src}")
                continue
            dest_path = self.output_dir / src_path.name
            logging.info(f"[{self.test_id}] Copying {src} to {dest_path}")
            shutil.copy2(src, dest_path)

    def run_execute(self, exe_file, stage_config=None):
        """Executes the compiled program."""
        config = stage_config if stage_config else self.test_config
        logging.info(f"[{self.test_id}] Starting Execute step...")

        wrapper = ExecuteWrapper(exe_file)

        args = config.get('test_args', [])
        input_data = config.get('test_input_data', "")

        # If test_input is a path to a file, read it
        test_input_file = config.get('test_input')
        if test_input_file:
            # Check if it exists relative to root or test directory
            input_path = Path(test_input_file)
            if not input_path.exists():
                input_path = self.test_dir / test_input_file

            if input_path.exists():
                with open(input_path, 'r') as f:
                    input_data = f.read()
            else:
                logging.warning(f"[{self.test_id}] Test input file not found: {test_input_file}")

        return wrapper.run(
            args=args,
            input_data=input_data,
            cwd=str(self.output_dir)
        )

    def run_compare(self, execution_result, stage_config=None):
        """Compares the actual outputs with the expected ones."""
        config = stage_config if stage_config else self.test_config
        logging.info(f"[{self.test_id}] Starting Compare step...")

        expected_outputs = config.get('expected_outputs', {})
        if not expected_outputs:
            logging.warning(f"[{self.test_id}] No expected outputs specified.")
            return True

        # Capture terminal/log output if requested
        if 'terminal' in expected_outputs:
            terminal_output_path = self.output_dir / "terminal.out"
            with open(terminal_output_path, "w") as f:
                f.write(execution_result.stdout)
                f.write(execution_result.stderr)

        all_match = True
        tolerance = self.test_config.get('settings', {}).get('tolerance')

        for output_type, expected_path in expected_outputs.items():
            if output_type == 'terminal':
                actual_path = self.output_dir / "terminal.out"
            else:
                actual_path = self.output_dir / Path(expected_path).name

            logging.info(f"[{self.test_id}] Comparing {output_type}: {actual_path} vs {expected_path}")

            match = False
            diff = ""

            if output_type in self.symbolic_comparators:
                # Binary comparison using symbolic converter
                converter = self.symbolic_comparators[output_type]
                match, diff = self.comparer.compare_binary_files(
                    expected_path, actual_path, converter,
                    normalizer=self.normalizer, tolerance=tolerance
                )
            else:
                # Direct text comparison
                match, diff = self.comparer.compare_text_files(
                    expected_path, actual_path,
                    normalizer=self.normalizer, tolerance=tolerance
                )

            if match:
                logging.info(f"[{self.test_id}] {output_type} match: OK")
            else:
                logging.error(f"[{self.test_id}] {output_type} mismatch!")
                if diff:
                    logging.error(f"Diff:\n{diff}")
                all_match = False

        return all_match

    def run(self):
        """Runs the full verification workflow for this test."""
        logging.info(f"--- Running Test: {self.test_id} ---")
        try:
            self.run_setup()

            pascal_file, pool_file = self.run_tangle()
            logging.info(f"[{self.test_id}] Tangle step completed: {pascal_file}, {pool_file}")

            if self.mcdc_enabled:
                pascal_file = self.run_instrumentation(pascal_file)
                logging.info(f"[{self.test_id}] Instrumentation step completed: {pascal_file}")

            exe_file = self.run_compile(pascal_file)
            logging.info(f"[{self.test_id}] Compile step completed: {exe_file}")

            success = True
            stages = self.test_config.get('stages')
            if stages:
                for stage in stages:
                    stage_id = stage.get('id', 'unnamed stage')
                    logging.info(f"[{self.test_id}] Executing stage: {stage_id}")
                    result = self.run_execute(exe_file, stage_config=stage)
                    if not self.run_compare(result, stage_config=stage):
                        success = False
                        break
            else:
                result = self.run_execute(exe_file)
                logging.info(f"[{self.test_id}] Execute step completed with exit code {result.returncode}")

                if not self.run_compare(result):
                    logging.error(f"[{self.test_id}] Compare step failed.")
                    success = False

            if success and self.mcdc_enabled:
                self.generate_mcdc_report()

            if success:
                logging.info(f"[{self.test_id}] Test completed successfully.")
            return success
        except Exception as e:
            logging.error(f"[{self.test_id}] Test failed: {e}")
            import traceback
            logging.error(traceback.format_exc())
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

    parser.add_argument(
        "--mcdc",
        action="store_true",
        help="Enable MC/DC instrumentation and coverage analysis."
    )

    args = parser.parse_args()

    if not args.config:
        # Before logging is setup, we use print/stderr for CLI errors
        print("Error: Configuration file is required.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    config = load_config(args.config)

    if args.mcdc:
        config['mcdc'] = True

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
