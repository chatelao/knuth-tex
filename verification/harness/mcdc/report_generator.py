import yaml
from verification.harness.mcdc.post_processor import parse_mcdc_log
from verification.harness.mcdc.analyzer import MCDCAnalyzer

class MCDCReportGenerator:
    """Generates MC/DC coverage reports from coverage logs and instrumented ASTs."""

    def __init__(self, decisions_ast_map):
        """
        Initialize with a map of decision_id to instrumented AST nodes.
        :param decisions_ast_map: dict mapping int to AST nodes.
        """
        self.decisions_ast_map = decisions_ast_map

    def generate_report(self, log_filepath):
        """
        Generates a structured report from the coverage log.
        :param log_filepath: Path to mcdc_coverage.out.
        :return: A dictionary containing the coverage report.
        """
        vectors_by_decision = parse_mcdc_log(log_filepath)
        report = {
            'summary': {
                'total_decisions': len(self.decisions_ast_map),
                'covered_decisions': 0,
                'total_conditions': 0,
                'covered_conditions': 0,
                'mcdc_percentage_overall': 0.0
            },
            'decisions': {}
        }

        total_cond = 0
        covered_cond = 0

        for d_id, ast in self.decisions_ast_map.items():
            vectors = vectors_by_decision.get(d_id, [])
            # Wrap raw AST in Expression if it's just a Probe or Identifier
            # MCDCAnalyzer handles Expression root
            analyzer = MCDCAnalyzer(ast)
            analysis = analyzer.analyze(vectors)
            analysis['decision_id'] = d_id
            analysis['executed'] = len(vectors) > 0

            report['decisions'][d_id] = analysis

            if analysis['total_conditions'] > 0:
                if analysis['covered_conditions'] == analysis['total_conditions']:
                    report['summary']['covered_decisions'] += 1
                total_cond += analysis['total_conditions']
                covered_cond += analysis['covered_conditions']
            else:
                # If there are no conditions (e.g. ForStatement), we consider it "covered"
                # if there is at least one vector (meaning mcdc_begin was called)
                if vectors:
                    report['summary']['covered_decisions'] += 1

        report['summary']['total_conditions'] = total_cond
        report['summary']['covered_conditions'] = covered_cond
        if total_cond > 0:
            report['summary']['mcdc_percentage_overall'] = (covered_cond / total_cond) * 100
        elif report['summary']['total_decisions'] > 0:
            # If there are only condition-less decisions
            report['summary']['mcdc_percentage_overall'] = (report['summary']['covered_decisions'] / report['summary']['total_decisions']) * 100

        return report

    def format_summary(self, report):
        """
        Formats the report as a human-readable summary.
        """
        summary = report['summary']
        lines = [
            "MC/DC Coverage Summary",
            "======================",
            f"Overall MC/DC Coverage: {summary['mcdc_percentage_overall']:.2f}%",
            f"Decisions: {summary['covered_decisions']}/{summary['total_decisions']} fully covered",
            f"Conditions: {summary['covered_conditions']}/{summary['total_conditions']} met independence criteria",
            "",
            "Detailed Decision Report:",
            "-------------------------"
        ]

        for d_id, analysis in sorted(report['decisions'].items()):
            if analysis['total_conditions'] > 0:
                status = "OK" if analysis['covered_conditions'] == analysis['total_conditions'] else "INCOMPLETE"
                lines.append(f"Decision {d_id}: {analysis['covered_conditions']}/{analysis['total_conditions']} conditions covered [{status}]")
                for c_id, c_data in sorted(analysis['conditions'].items()):
                    c_status = "PASSED" if c_data['covered'] else "FAILED"
                    lines.append(f"  Condition {c_id}: {c_status}")
            else:
                # Decision without boolean conditions (e.g. FOR)
                status = "EXECUTED" if analysis['executed'] else "NOT EXECUTED"
                lines.append(f"Decision {d_id}: No conditions [{status}]")

        return "\n".join(lines)

    def save_report_yaml(self, report, output_path):
        """Saves the report to a YAML file."""
        with open(output_path, 'w') as f:
            yaml.dump(report, f, default_flow_style=False)
