import yaml
import sys
import argparse
from pathlib import Path

def merge_reports(reports):
    """
    Merges multiple MC/DC reports into one.
    Conditions are considered covered if they are covered in AT LEAST one report.
    """
    if not reports:
        return {}

    merged = {
        'summary': {
            'total_decisions': 0,
            'covered_decisions': 0,
            'total_conditions': 0,
            'covered_conditions': 0,
            'mcdc_percentage_overall': 0.0
        },
        'decisions': {}
    }

    # Initialize from the first report to get the structure
    # Actually, better to iterate through all and merge into a master dict

    all_decision_ids = set()
    for r in reports:
        all_decision_ids.update(r.get('decisions', {}).keys())

    for d_id in all_decision_ids:
        # Find all instances of this decision across reports
        d_instances = [r['decisions'][d_id] for r in reports if d_id in r['decisions']]

        # Merge decision data
        first = d_instances[0]
        merged_d = {
            'decision_id': d_id,
            'executed': any(d['executed'] for d in d_instances),
            'total_conditions': first['total_conditions'],
            'covered_conditions': 0,
            'conditions': {}
        }

        if merged_d['total_conditions'] > 0:
            for c_id in first['conditions'].keys():
                merged_d['conditions'][c_id] = {
                    'covered': any(d['conditions'][c_id]['covered'] for d in d_instances if c_id in d['conditions'])
                }
            merged_d['covered_conditions'] = sum(1 for c in merged_d['conditions'].values() if c['covered'])

        merged['decisions'][d_id] = merged_d

    # Recompute summary
    total_cond = 0
    covered_cond = 0
    covered_decs = 0
    total_decs = len(merged['decisions'])

    for d_id, d in merged['decisions'].items():
        if d['total_conditions'] > 0:
            total_cond += d['total_conditions']
            covered_cond += d['covered_conditions']
            if d['covered_conditions'] == d['total_conditions']:
                covered_decs += 1
        else:
            if d['executed']:
                covered_decs += 1

    merged['summary']['total_decisions'] = total_decs
    merged['summary']['covered_decisions'] = covered_decs
    merged['summary']['total_conditions'] = total_cond
    merged['summary']['covered_conditions'] = covered_cond

    if total_cond > 0:
        merged['summary']['mcdc_percentage_overall'] = (covered_cond / total_cond) * 100
    elif total_decs > 0:
        merged['summary']['mcdc_percentage_overall'] = (covered_decs / total_decs) * 100

    return merged

def main():
    parser = argparse.ArgumentParser(description="Aggregate multiple MC/DC coverage reports.")
    parser.add_argument("inputs", nargs="+", help="Path to input YAML reports.")
    parser.add_argument("--output", "-o", required=True, help="Path to output aggregated YAML report.")

    args = parser.parse_args()

    reports = []
    for path_str in args.inputs:
        path = Path(path_str)
        if not path.exists():
            print(f"Warning: Input file not found: {path}")
            continue
        with open(path, 'r') as f:
            reports.append(yaml.safe_load(f))

    if not reports:
        print("Error: No valid input reports found.")
        sys.exit(1)

    merged = merge_reports(reports)

    with open(args.output, 'w') as f:
        yaml.dump(merged, f, default_flow_style=False)

    print(f"Aggregated report saved to {args.output}")
    print(f"Overall MC/DC Coverage: {merged['summary']['mcdc_percentage_overall']:.2f}%")

if __name__ == "__main__":
    main()
