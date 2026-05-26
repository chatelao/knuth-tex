import yaml
from pathlib import Path

def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def main():
    # Define paths
    root_dir = Path(__file__).parent.parent.parent
    matrix_path = root_dir / 'verification/trace/matrix.yaml'
    hlr_path = root_dir / 'verification/reqs/hlr.yaml'
    llr_tex_path = root_dir / 'verification/reqs/llr_tex.yaml'
    llr_mf_path = root_dir / 'verification/reqs/llr_mf.yaml'
    report_path = root_dir / 'verification/results/traceability_report.md'

    # Load data
    matrix = load_yaml(matrix_path)
    hlrs = load_yaml(hlr_path)
    llrs_tex = load_yaml(llr_tex_path)
    llrs_mf = load_yaml(llr_mf_path)

    # Index data for easy lookup
    hlr_dict = {h['id']: h for h in hlrs}
    llr_dict = {l['id']: l for l in llrs_tex}
    llr_dict.update({l['id']: l for l in llrs_mf})

    # Traceability Matrix lookup
    matrix_dict = {m['hlr_id']: m for m in matrix}

    # Ensure output directory exists
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate report
    with open(report_path, 'w') as f:
        f.write("# Traceability Report\n\n")

        f.write("## HLR to LLR to Test Case Traceability\n\n")
        f.write("| HLR ID | Description | LLR IDs | Test Case IDs |\n")
        f.write("| --- | --- | --- | --- |\n")

        covered_hlrs = 0
        total_hlrs = len(hlrs)

        for hlr_id in sorted(hlr_dict.keys()):
            hlr = hlr_dict[hlr_id]
            m_entry = matrix_dict.get(hlr_id, {})
            llr_ids = ", ".join(m_entry.get('llr_ids', []))
            tc_ids = ", ".join(m_entry.get('test_case_ids', []))

            f.write(f"| {hlr_id} | {hlr['description']} | {llr_ids} | {tc_ids} |\n")

            if m_entry.get('test_case_ids'):
                covered_hlrs += 1

        f.write("\n")

        # Statistics
        f.write("## Coverage Statistics\n\n")
        coverage_pct = (covered_hlrs / total_hlrs) * 100 if total_hlrs > 0 else 0
        f.write(f"- **Total HLRs:** {total_hlrs}\n")
        f.write(f"- **Covered HLRs:** {covered_hlrs}\n")
        f.write(f"- **HLR Coverage:** {coverage_pct:.2f}%\n\n")

        # Analysis
        f.write("## Analysis\n\n")

        # Orphan HLRs (no tests)
        orphan_hlrs = [h_id for h_id in hlr_dict if not matrix_dict.get(h_id, {}).get('test_case_ids')]
        if orphan_hlrs:
            f.write("### HLRs without Test Cases (Orphans)\n")
            for h_id in orphan_hlrs:
                f.write(f"- {h_id}\n")
            f.write("\n")
        else:
            f.write("### HLRs without Test Cases (Orphans)\n*None*\n\n")

        # LLRs without HLR parents (check LLR files)
        orphan_llrs = []
        for l_id, llr in llr_dict.items():
            if not llr.get('parent_hlr'):
                orphan_llrs.append(l_id)

        if orphan_llrs:
            f.write("### LLRs without Parent HLRs (Orphans)\n")
            for l_id in sorted(orphan_llrs):
                f.write(f"- {l_id}\n")
            f.write("\n")
        else:
            f.write("### LLRs without Parent HLRs (Orphans)\n*None*\n\n")

    print(f"Report generated at: {report_path}")

if __name__ == "__main__":
    main()
