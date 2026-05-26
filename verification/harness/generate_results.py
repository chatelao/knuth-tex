import yaml
import json
import sys
from pathlib import Path

def load_yaml(filepath):
    if not filepath.exists():
        return {}
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def load_json(filepath):
    if not filepath.exists():
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def main():
    root_dir = Path(__file__).parent.parent.parent
    results_dir = root_dir / 'verification/results'
    report_json_path = results_dir / 'all_tests_report.json'
    matrix_path = root_dir / 'verification/trace/matrix.yaml'
    hlr_path = root_dir / 'verification/reqs/hlr.yaml'
    summary_md_path = results_dir / 'test_results_summary.md'

    results_data = load_json(report_json_path)
    if not results_data:
        print(f"Error: {report_json_path} not found or empty.")
        sys.exit(1)

    matrix = load_yaml(matrix_path)
    hlrs = load_yaml(hlr_path)

    # All tests outcomes, indexed by full nodeid
    all_tests = results_data.get('tests', [])
    test_outcomes = {t['nodeid']: t['outcome'] for t in all_tests}

    with open(summary_md_path, 'w') as f:
        f.write("# Verification Results Report\n\n")

        # Overall Stats
        summary = results_data.get('summary', {})
        total = summary.get('total', 0)
        passed = summary.get('passed', 0)
        failed = summary.get('failed', 0)
        skipped = summary.get('skipped', 0)
        duration = results_data.get('duration', 0)

        f.write("## Overall Execution Statistics\n\n")
        f.write(f"- **Total Tests:** {total}\n")
        f.write(f"- **Passed:** {passed}\n")
        f.write(f"- **Failed:** {failed}\n")
        f.write(f"- **Skipped:** {skipped}\n")
        f.write(f"- **Total Duration:** {duration:.2f}s\n\n")

        # Detailed Test Results
        f.write("## Detailed Test Results\n\n")
        f.write("| Test ID | Outcome | Duration (s) |\n")
        f.write("| --- | --- | --- |\n")
        for test in sorted(all_tests, key=lambda x: x['nodeid']):
            nodeid = test['nodeid']
            outcome = test['outcome'].upper()
            test_duration = test.get('setup', {}).get('duration', 0) + \
                            test.get('call', {}).get('duration', 0) + \
                            test.get('teardown', {}).get('duration', 0)
            f.write(f"| {nodeid} | {outcome} | {test_duration:.4f} |\n")
        f.write("\n")

        # Requirement-Based Results
        f.write("## Requirement-Based Results\n\n")
        f.write("| HLR ID | Description | Status | Evidence (Test Cases) |\n")
        f.write("| --- | --- | --- | --- |\n")

        hlr_dict = {h['id']: h for h in hlrs}
        matrix_dict = {m['hlr_id']: m for m in matrix}

        for h_id in sorted(hlr_dict.keys()):
            hlr = hlr_dict[h_id]
            m_entry = matrix_dict.get(h_id, {})
            tc_ids = m_entry.get('test_case_ids', [])

            status = "PASSED"
            if not tc_ids:
                status = "NOT TESTED"
            else:
                tc_results = {} # tc_id -> list of nodeids
                for tc_id in tc_ids:
                    tc_results[tc_id] = [nid for nid in test_outcomes if tc_id in nid]

                all_passed = True
                some_executed = False

                for tc_id, nodeids in tc_results.items():
                    if not nodeids:
                        all_passed = False
                    else:
                        some_executed = True
                        for nid in nodeids:
                            if test_outcomes[nid] != 'passed':
                                all_passed = False
                                break
                    if not all_passed:
                        break

                if not all_passed:
                    if some_executed:
                        # At least one test failed or some required test cases weren't found
                        status = "FAILED"
                    else:
                        status = "NOT EXECUTED"
                elif not some_executed:
                    status = "NOT EXECUTED"

            f.write(f"| {h_id} | {hlr['description']} | {status} | {', '.join(tc_ids)} |\n")
        f.write("\n")

        # Failure Logs (if any)
        failed_tests = [t for t in all_tests if t['outcome'] == 'failed']
        if failed_tests:
            f.write("## Execution Logs for Failed Test Cases\n\n")
            for t in failed_tests:
                f.write(f"### {t['nodeid']}\n")
                f.write("```\n")
                # Get longrepr or use crash message
                log = t.get('call', {}).get('longrepr', t.get('call', {}).get('crash', {}).get('message', 'No details available'))
                f.write(log)
                f.write("\n```\n\n")

    print(f"Results summary generated at: {summary_md_path}")

if __name__ == "__main__":
    main()
