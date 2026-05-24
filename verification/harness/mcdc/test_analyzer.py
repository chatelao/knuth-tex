import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import Parser
from verification.harness.mcdc.instrumenter import Instrumenter
from verification.harness.mcdc.analyzer import MCDCAnalyzer

def get_instrumented_ast(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()
    instrumenter = Instrumenter()
    # For IF/WHILE/etc., instrumenter returns a Block [Probe(dec_id), Statement]
    # We want the instrumented condition
    instrumented_stmt = instrumenter.instrument(ast)
    # The instrumenter wraps control flow in a Block with a Probe.
    # We need to reach the instrumented condition.
    if hasattr(instrumented_stmt, 'statements'):
        # For IfStatement, it's Block([Probe, IfStatement])
        actual_stmt = instrumented_stmt.statements[1]
        return actual_stmt.condition
    return instrumented_stmt

def test_analyzer_and_gate():
    code = "IF A AND B THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    # Vectors: A, B
    # (T, T) -> T
    # (F, T) -> F
    # (T, F) -> F
    vectors = [
        {1: True, 2: True},
        {1: False, 2: True},
        {1: True, 2: False}
    ]

    results = analyzer.analyze(vectors)
    assert results['total_conditions'] == 2
    assert results['covered_conditions'] == 2
    assert results['mcdc_percentage'] == 100.0
    assert results['conditions'][1]['covered'] is True # A is independent via (T,T) and (F,T)
    assert results['conditions'][2]['covered'] is True # B is independent via (T,T) and (T,F)

def test_analyzer_or_gate():
    code = "IF A OR B THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    # Vectors: A, B
    # (F, F) -> F
    # (T, F) -> T
    # (F, T) -> T
    vectors = [
        {1: False, 2: False},
        {1: True, 2: False},
        {1: False, 2: True}
    ]

    results = analyzer.analyze(vectors)
    assert results['covered_conditions'] == 2
    assert results['mcdc_percentage'] == 100.0

def test_analyzer_not_gate():
    code = "IF NOT A THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    vectors = [
        {1: True},
        {1: False}
    ]

    results = analyzer.analyze(vectors)
    assert results['covered_conditions'] == 1
    assert results['mcdc_percentage'] == 100.0

def test_analyzer_complex_expression():
    # (A OR B) AND C
    # A=1, B=2, C=3
    code = "IF (A OR B) AND C THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    # To cover C: ( (A or B)=T, C=T ) and ( (A or B)=T, C=F )
    #   e.g., (T, F, T) -> T  and (T, F, F) -> F
    # To cover A: ( A=T, B=F, C=T ) and ( A=F, B=F, C=T )
    #   e.g., (T, F, T) -> T  and (F, F, T) -> F
    # To cover B: ( A=F, B=T, C=T ) and ( A=F, B=F, C=T )
    #   e.g., (F, T, T) -> T  and (F, F, T) -> F

    vectors = [
        {1: True, 2: False, 3: True},  # (T, F, T) -> T
        {1: True, 2: False, 3: False}, # (T, F, F) -> F  => Covers C (with 1st)
        {1: False, 2: False, 3: True}, # (F, F, T) -> F  => Covers A (with 1st)
        {1: False, 2: True, 3: True}   # (F, T, T) -> T  => Covers B (with 3rd)
    ]

    results = analyzer.analyze(vectors)
    assert results['covered_conditions'] == 3
    assert results['mcdc_percentage'] == 100.0

def test_analyzer_uncovered_condition():
    code = "IF A AND B THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    # Only (T, T) and (F, T) -> A is covered, but B is not
    vectors = [
        {1: True, 2: True},
        {1: False, 2: True}
    ]

    results = analyzer.analyze(vectors)
    assert results['conditions'][1]['covered'] is True
    assert results['conditions'][2]['covered'] is False
    assert results['covered_conditions'] == 1
    assert results['mcdc_percentage'] == 50.0

def test_analyzer_redundant_vectors():
    code = "IF A THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    vectors = [
        {1: True},
        {1: True},
        {1: False}
    ]

    results = analyzer.analyze(vectors)
    assert results['covered_conditions'] == 1
