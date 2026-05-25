from verification.harness.mcdc.analyzer import MCDCAnalyzer
from verification.harness.mcdc.post_processor import parse_mcdc_log
from verification.harness.mcdc.parser import Probe, BinaryOp, Identifier

def test_mcdc_integration(tmp_path):
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
    )

    # Decision 1: A OR B
    # Instrumented as: (mcdc_cond(1, 1, A) OR mcdc_cond(1, 2, B))
    ast = BinaryOp(Probe(1, 1, Identifier('A')), 'OR', Probe(1, 2, Identifier('B')))

    # 1. Parse log
    vectors_dict = parse_mcdc_log(str(log_file))
    vectors = vectors_dict[1]

    # 2. Analyze
    analyzer = MCDCAnalyzer(ast)
    results = analyzer.analyze(vectors)

    assert results['covered_conditions'] == 2
    assert results['mcdc_percentage'] == 100.0
    assert results['conditions'][1]['covered'] is True
    assert results['conditions'][2]['covered'] is True
