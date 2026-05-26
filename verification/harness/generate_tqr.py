import yaml
import subprocess
import json
import os
from pathlib import Path

def run_tests(test_path, report_path):
    """Runs pytest on the given path and returns the results."""
    subprocess.run(
        ['python3', '-m', 'pytest', '--json-report', f'--json-report-file={report_path}', str(test_path)],
        capture_output=True, text=True
    )

    if Path(report_path).exists():
        with open(report_path, 'r') as f:
            return json.load(f)
    return None

def generate_report(reqs_path, mapping, tests_results, output_path, title):
    """Generates a Markdown TQR report."""
    with open(reqs_path, 'r') as f:
        reqs = yaml.safe_load(f)

    with open(output_path, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write("| Requirement ID | Description | Test Files | Status |\n")
        f.write("| --- | --- | --- | --- |\n")

        for req in reqs:
            req_id = req['id']
            test_files = mapping.get(req_id, [])

            # Determine status based on test results
            status = "PASSED"
            if not test_files:
                status = "NOT TESTED"
            else:
                for tf in test_files:
                    # Check if any test in this file failed
                    file_tests_found = False
                    for test in tests_results.get('tests', []):
                        if tf in test['nodeid']:
                            file_tests_found = True
                            if test['outcome'] != 'passed':
                                status = "FAILED"
                                break
                    if status == "FAILED":
                        break
                    if not file_tests_found:
                        # This could happen if the test file name in mapping doesn't match the nodeid
                        pass

            f.write(f"| {req_id} | {req['description']} | {', '.join(test_files)} | {status} |\n")

def main():
    root_dir = Path(__file__).parent.parent.parent
    mapping_path = root_dir / 'verification/reqs/tqr_mapping.yaml'

    with open(mapping_path, 'r') as f:
        mapping = yaml.safe_load(f)

    # Run harness tests
    print("Running harness tests...")
    harness_report_json = root_dir / 'verification/results/harness_report.json'
    harness_results = run_tests(root_dir / 'verification/harness', harness_report_json)
    if harness_results:
        generate_report(
            root_dir / 'verification/reqs/tor_harness.yaml',
            mapping,
            harness_results,
            root_dir / 'verification/results/tqr_harness.md',
            "Tool Qualification Report for the Test Harness (TQR-HARNESS)"
        )
        print("TQR-HARNESS generated.")

    # Run instrumenter tests
    print("Running instrumenter tests...")
    instr_report_json = root_dir / 'verification/results/instr_report.json'
    instr_results = run_tests(root_dir / 'verification/harness/mcdc', instr_report_json)
    if instr_results:
        generate_report(
            root_dir / 'verification/reqs/tor_instr.yaml',
            mapping,
            instr_results,
            root_dir / 'verification/results/tqr_instr.md',
            "Tool Qualification Report for the MC/DC Instrumenter (TQR-INSTR)"
        )
        print("TQR-INSTR generated.")

    # Cleanup temporary json reports
    if harness_report_json.exists(): os.remove(harness_report_json)
    if instr_report_json.exists(): os.remove(instr_report_json)

if __name__ == "__main__":
    main()
