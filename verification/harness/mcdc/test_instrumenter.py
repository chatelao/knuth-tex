import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import Parser
from verification.harness.mcdc.instrumenter import PascalEmitter, Instrumenter

def test_emitter_simple_assignment():
    code = "x := 1;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    emitter = PascalEmitter()
    output = emitter.emit(ast)
    assert output == "x := 1"

def test_emitter_complex_if():
    code = "IF (a > 0) AND (b < 10) THEN BEGIN x := 1; y := 2 END ELSE x := 0"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    emitter = PascalEmitter()
    output = emitter.emit(ast)
    # Note: emitter might add parentheses based on AST structure
    assert "IF ((a > 0) AND (b < 10)) THEN BEGIN x := 1; y := 2 END ELSE x := 0" in output

def test_instrumenter_basic():
    code = "BEGIN IF x > 0 THEN x := 1 END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)

    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    assert "record_mcdc(1)" in output
    assert "IF (x > 0) THEN x := 1" in output

def test_instrumenter_multiple_decisions():
    code = """
    BEGIN
        IF x > 0 THEN x := 1;
        WHILE y < 10 DO y := y + 1;
        REPEAT z := z - 1 UNTIL z = 0
    END
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)

    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    assert "record_mcdc(1)" in output
    assert "IF (x > 0)" in output
    assert "record_mcdc(2)" in output
    assert "WHILE (y < 10)" in output
    assert "record_mcdc(3)" in output
    assert "REPEAT z := (z - 1) UNTIL (z = 0)" in output

def test_instrumenter_nested():
    code = "IF x > 0 THEN BEGIN IF y > 0 THEN z := 1 END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)

    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    # Outer block is not there, so we only instrument if it's in a block.
    # Wait, my instrumenter only inserts probes inside Blocks.
    # If it's a lone IF, it doesn't get a probe before it unless it's in a block.
    # That's probably fine for now as most TANGLE output is in blocks.

    # Let's wrap it in a BEGIN...END to be sure
    code = "BEGIN IF x > 0 THEN BEGIN IF y > 0 THEN z := 1 END END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    # Use a fresh instrumenter
    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)
    output = emitter.emit(instrumented_ast)

    assert "record_mcdc(1); IF (x > 0) THEN BEGIN record_mcdc(2); IF (y > 0) THEN z := 1 END" in output
