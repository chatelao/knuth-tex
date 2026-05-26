import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import Parser, BinaryOp, UnaryOp, Literal
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

def test_analyzer_evaluate_operators():
    # Test arithmetic and relational operators in MCDCAnalyzer.evaluate
    # We can pass any AST node to evaluate.
    analyzer = MCDCAnalyzer(Literal(True, 'BOOLEAN'))

    # Relational
    assert analyzer.evaluate(BinaryOp(Literal(1, 'NUMBER'), '=', Literal(1, 'NUMBER')), {}) is True
    assert analyzer.evaluate(BinaryOp(Literal(1, 'NUMBER'), '<>', Literal(2, 'NUMBER')), {}) is True
    assert analyzer.evaluate(BinaryOp(Literal(1, 'NUMBER'), '<', Literal(2, 'NUMBER')), {}) is True
    assert analyzer.evaluate(BinaryOp(Literal(2, 'NUMBER'), '<=', Literal(2, 'NUMBER')), {}) is True
    assert analyzer.evaluate(BinaryOp(Literal(2, 'NUMBER'), '>', Literal(1, 'NUMBER')), {}) is True
    assert analyzer.evaluate(BinaryOp(Literal(2, 'NUMBER'), '>=', Literal(2, 'NUMBER')), {}) is True

    # Arithmetic
    assert analyzer.evaluate(BinaryOp(Literal(5, 'NUMBER'), '+', Literal(3, 'NUMBER')), {}) == 8
    assert analyzer.evaluate(BinaryOp(Literal(5, 'NUMBER'), '-', Literal(3, 'NUMBER')), {}) == 2
    assert analyzer.evaluate(BinaryOp(Literal(5, 'NUMBER'), '*', Literal(3, 'NUMBER')), {}) == 15
    assert analyzer.evaluate(BinaryOp(Literal(6, 'NUMBER'), '/', Literal(2, 'NUMBER')), {}) == 3.0
    assert analyzer.evaluate(BinaryOp(Literal(7, 'NUMBER'), 'DIV', Literal(2, 'NUMBER')), {}) == 3
    assert analyzer.evaluate(BinaryOp(Literal(7, 'NUMBER'), 'MOD', Literal(2, 'NUMBER')), {}) == 1

    # Unary
    assert analyzer.evaluate(UnaryOp('+', Literal(5, 'NUMBER')), {}) == 5
    assert analyzer.evaluate(UnaryOp('-', Literal(5, 'NUMBER')), {}) == -5
    assert analyzer.evaluate(UnaryOp('NOT', Literal(True, 'BOOLEAN')), {}) is False

def test_analyzer_independence_pair_verification():
    # Test that MCDCAnalyzer correctly identifies independence pairs
    # IF A AND B THEN ...
    code = "IF A AND B THEN x := 1"
    ast = get_instrumented_ast(code)
    analyzer = MCDCAnalyzer(ast)

    # (T, T) -> T
    # (F, T) -> F
    # (T, F) -> F
    v1 = {1: True, 2: True}
    v2 = {1: False, 2: True}
    v3 = {1: True, 2: False}
    vectors = [v1, v2, v3]

    results = analyzer.analyze(vectors)

    # Condition 1 (A) independence pair should be (v1, v2)
    pair1 = results['conditions'][1]['independence_pair']
    assert pair1 is not None
    assert (pair1[0] == v1 and pair1[1] == v2) or (pair1[0] == v2 and pair1[1] == v1)

    # Condition 2 (B) independence pair should be (v1, v3)
    pair2 = results['conditions'][2]['independence_pair']
    assert pair2 is not None
    assert (pair2[0] == v1 and pair2[1] == v3) or (pair2[0] == v3 and pair2[1] == v1)
