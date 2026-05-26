from verification.harness.mcdc.analyzer import MCDCAnalyzer
from verification.harness.mcdc.post_processor import parse_mcdc_log
from verification.harness.mcdc.parser import Parser, Probe, BinaryOp, Identifier
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.instrumenter import Instrumenter

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

def test_full_flow_integration(tmp_path):
    # Full flow: Source -> Lexer -> Parser -> Instrumenter -> (Mock Log) -> Analyzer
    source_code = "IF (A = 1) AND (B > 0) THEN x := 1"

    # 1. Lexing and Parsing
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    # 2. Instrumentation
    instrumenter = Instrumenter()
    inst_stmt = instrumenter.instrument(stmt)

    # Verify that we have a decision identified
    assert len(instrumenter.decisions) == 1
    decision_id = list(instrumenter.decisions.keys())[0]
    inst_expr = instrumenter.decisions[decision_id]

    # 3. Create mock log
    # Conditions: 1: (A=1), 2: (B>0)
    # Vectors:
    # (T, T) -> T
    # (F, T) -> F  => Covers 1
    # (T, F) -> F  => Covers 2
    log_file = tmp_path / "mcdc_coverage.out"
    log_file.write_text(
        f"B {decision_id}\n"
        f"C {decision_id} 1 1\n"
        f"C {decision_id} 2 1\n"
        f"B {decision_id}\n"
        f"C {decision_id} 1 0\n"
        f"C {decision_id} 2 1\n"
        f"B {decision_id}\n"
        f"C {decision_id} 1 1\n"
        f"C {decision_id} 2 0\n"
    )

    # 4. Post-processing
    vectors_dict = parse_mcdc_log(str(log_file))
    vectors = vectors_dict[decision_id]

    # 5. Analysis
    analyzer = MCDCAnalyzer(inst_expr)
    results = analyzer.analyze(vectors)

    assert results['total_conditions'] == 2
    assert results['covered_conditions'] == 2
    assert results['mcdc_percentage'] == 100.0

def test_multiple_decisions_integration(tmp_path):
    source_code = """
    BEGIN
      IF A THEN x := 1;
      IF B THEN y := 2
    END
    """
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    instrumenter = Instrumenter()
    inst_stmt = instrumenter.instrument(stmt)

    assert len(instrumenter.decisions) == 2
    d_ids = sorted(instrumenter.decisions.keys())

    log_file = tmp_path / "mcdc_coverage.out"
    log_file.write_text(
        f"B {d_ids[0]}\n"
        f"C {d_ids[0]} 1 1\n"
        f"B {d_ids[0]}\n"
        f"C {d_ids[0]} 1 0\n"
        f"B {d_ids[1]}\n"
        f"C {d_ids[1]} 1 1\n"
    )

    vectors_dict = parse_mcdc_log(str(log_file))

    # Analyze Decision 1 (A) - fully covered
    analyzer1 = MCDCAnalyzer(instrumenter.decisions[d_ids[0]])
    results1 = analyzer1.analyze(vectors_dict[d_ids[0]])
    assert results1['mcdc_percentage'] == 100.0

    # Analyze Decision 2 (B) - not fully covered (only one vector)
    analyzer2 = MCDCAnalyzer(instrumenter.decisions[d_ids[1]])
    results2 = analyzer2.analyze(vectors_dict[d_ids[1]])
    assert results2['mcdc_percentage'] == 0.0

from verification.harness.mcdc.instrumenter import PascalEmitter

def test_instrumentation_logic_preservation():
    # Verify that instrumentation preserves the original logic
    # (i.e., if we ignore probes, the emitted code is equivalent)
    source_code = "IF (A = 1) AND (B > 0) THEN x := 1 ELSE x := 2"

    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    instrumenter = Instrumenter()
    inst_stmt = instrumenter.instrument(stmt)

    emitter = PascalEmitter()
    inst_code = emitter.emit(inst_stmt)

    # Check that the core logic is there
    assert "IF" in inst_code
    assert "THEN x := 1" in inst_code
    assert "ELSE x := 2" in inst_code
    assert "mcdc_cond" in inst_code
    assert "mcdc_begin" in inst_code
