import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import Parser, Block, IfStatement, Probe
from verification.harness.mcdc.instrumenter import Instrumenter

def get_ast(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse_statement()

def test_instrument_if():
    code = "IF x > 0 THEN x := 1 ELSE x := 0;"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    assert isinstance(new_ast, IfStatement)
    # Check THEN branch
    assert isinstance(new_ast.then_branch, Block)
    assert isinstance(new_ast.then_branch.statements[0], Probe)
    assert new_ast.then_branch.statements[0].probe_id == 1

    # Check ELSE branch
    assert isinstance(new_ast.else_branch, Block)
    assert isinstance(new_ast.else_branch.statements[0], Probe)
    assert new_ast.else_branch.statements[0].probe_id == 2

def test_instrument_if_no_else():
    code = "IF x > 0 THEN x := 1;"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    assert isinstance(new_ast, IfStatement)
    assert new_ast.else_branch is not None
    assert isinstance(new_ast.else_branch, Block)
    assert isinstance(new_ast.else_branch.statements[0], Probe)
    assert new_ast.else_branch.statements[0].probe_id == 2

def test_instrument_while():
    code = "WHILE x > 0 DO x := x - 1;"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    assert isinstance(new_ast.body, Block)
    assert isinstance(new_ast.body.statements[0], Probe)
    assert new_ast.body.statements[0].probe_id == 1

def test_instrument_for():
    code = "FOR i := 1 TO 10 DO write(i);"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    assert isinstance(new_ast.body, Block)
    assert isinstance(new_ast.body.statements[0], Probe)
    assert new_ast.body.statements[0].probe_id == 1

def test_instrument_repeat():
    code = "REPEAT x := x + 1 UNTIL x > 10;"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    # RepeatStatement body is a list of statements
    assert isinstance(new_ast.statements[0], Probe)
    assert new_ast.statements[0].probe_id == 1

def test_instrument_nested():
    code = "IF x > 0 THEN IF y > 0 THEN z := 1;"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    # Execution order of next_probe():
    # 1. wrap_in_block(outer_then) -> Probe 1
    # 2.   visit(inner_if)
    # 3.     wrap_in_block(inner_then) -> Probe 2
    # 4.     implicit else(inner_if) -> Probe 3
    # 5. implicit else(outer_if) -> Probe 4

    assert new_ast.then_branch.statements[0].probe_id == 1
    inner_if = new_ast.then_branch.statements[1]
    assert inner_if.then_branch.statements[0].probe_id == 2
    assert inner_if.else_branch.statements[0].probe_id == 3
    assert new_ast.else_branch.statements[0].probe_id == 4

def test_instrument_block():
    code = "BEGIN x := 1; IF y > 0 THEN y := 2 END"
    ast = get_ast(code)
    instrumenter = Instrumenter()
    new_ast = instrumenter.instrument(ast)

    assert isinstance(new_ast, Block)
    assert len(new_ast.statements) == 2
    assert isinstance(new_ast.statements[1], IfStatement)
    assert isinstance(new_ast.statements[1].then_branch.statements[0], Probe)
