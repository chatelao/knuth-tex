import pytest
from verification.harness.mcdc.report_generator import MCDCReportGenerator
from verification.harness.mcdc.parser import Probe, BinaryOp, Identifier

def test_report_generator_basic(tmp_path):
    log_file = tmp_path / "mcdc_coverage.out"
    log_file.write_text(
        "B 1\n"
        "C 1 1 1\n"
        "C 1 2 0\n"
        "B 1\n"
        "C 1 1 0\n"
        "C 1 2 1\n"
        "B 1\n"
        "C 1 1 0\n"
        "C 1 2 0\n"
        "B 2\n"
        "C 2 1 1\n"
        "B 2\n"
        "C 2 1 0\n"
    )

    # Decision 1: A OR B
    ast1 = BinaryOp(Probe(1, 1, Identifier('A')), 'OR', Probe(1, 2, Identifier('B')))
    # Decision 2: C
    ast2 = Probe(2, 1, Identifier('C'))
    # Decision 3: D (not executed)
    ast3 = Probe(3, 1, Identifier('D'))

    decisions_map = {1: ast1, 2: ast2, 3: ast3}
    generator = MCDCReportGenerator(decisions_map)
    report = generator.generate_report(str(log_file))

    assert report['summary']['total_decisions'] == 3
    assert report['summary']['covered_decisions'] == 2 # 1 and 2
    # Decision 1 has 2, Decision 2 has 1, Decision 3 has 1. Total = 4.
    assert report['summary']['total_conditions'] == 4
    assert report['summary']['covered_conditions'] == 3 # 1,1 and 1,2 from D1, 2,1 from D2

    assert report['decisions'][1]['covered_conditions'] == 2
    assert report['decisions'][2]['covered_conditions'] == 1
    assert report['decisions'][3]['covered_conditions'] == 0
    assert report['decisions'][3]['executed'] is False

    summary_text = generator.format_summary(report)
    assert "Overall MC/DC Coverage: 75.00%" in summary_text
    assert "Decisions: 2/3 fully covered" in summary_text
    assert "Condition 1: PASSED" in summary_text
    assert "Decision 3: 0/1 conditions covered [INCOMPLETE]" in summary_text

def test_report_generator_no_conditions(tmp_path):
    log_file = tmp_path / "mcdc_coverage.out"
    log_file.write_text("B 1\n") # Executed

    # Decision 1: FOR variable (no boolean conditions)
    ast1 = Identifier('i')

    decisions_map = {1: ast1}
    generator = MCDCReportGenerator(decisions_map)
    report = generator.generate_report(str(log_file))

    assert report['summary']['total_decisions'] == 1
    assert report['summary']['covered_decisions'] == 1
    assert report['summary']['total_conditions'] == 0
    assert report['summary']['mcdc_percentage_overall'] == 100.0

    summary_text = generator.format_summary(report)
    assert "Decision 1: No conditions [EXECUTED]" in summary_text
