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

    assert "mcdc_begin(1)" in output
    # x > 0 should be instrumented as well
    assert "mcdc_cond(1, 1, (x > 0))" in output

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

    assert "mcdc_begin(1)" in output
    assert "IF mcdc_cond(1, 1, (x > 0))" in output
    assert "mcdc_begin(2)" in output
    assert "WHILE mcdc_cond(2, 1, (y < 10))" in output
    assert "mcdc_begin(3)" in output
    assert "REPEAT z := (z - 1) UNTIL mcdc_cond(3, 1, (z = 0))" in output

def test_instrumenter_nested():
    # Let's wrap it in a BEGIN...END to be sure
    code = "BEGIN IF x > 0 THEN BEGIN IF y > 0 THEN z := 1 END END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    # Use a fresh instrumenter
    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)
    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    assert "mcdc_begin(1); IF mcdc_cond(1, 1, (x > 0)) THEN BEGIN mcdc_begin(2); IF mcdc_cond(2, 1, (y > 0)) THEN z := 1 END" in output

def test_instrumenter_simple_condition():
    code = "IF a > 0 THEN x := 1"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)
    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    # Should be wrapped in BEGIN ... END because instrument returns a Block for IF
    assert "BEGIN mcdc_begin(1); IF mcdc_cond(1, 1, (a > 0)) THEN x := 1 END" == output

def test_instrumenter_complex_condition():
    code = "IF (a > 0) AND (NOT b OR c) THEN x := 1"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)
    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    # Decomposed: (a > 0) is 1, b is 2, c is 3
    assert "mcdc_cond(1, 1, (a > 0))" in output
    assert "NOT mcdc_cond(1, 2, b)" in output
    assert "mcdc_cond(1, 3, c)" in output

def test_instrumenter_case():
    code = "CASE x OF 1: y := 1; 2: y := 2 OTHERWISE y := 0 END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_statement()

    instrumenter = Instrumenter()
    instrumented_ast = instrumenter.instrument(ast)
    emitter = PascalEmitter()
    output = emitter.emit(instrumented_ast)

    assert "mcdc_begin(1); CASE mcdc_cond(1, 1, x) OF 1: y := 1; 2: y := 2; OTHERWISE y := 0 END" in output

def test_instrument_program_with_procedures():
    code = """
    PROGRAM test;
    VAR x: boolean;
    PROCEDURE p;
    BEGIN
        IF x THEN x := false
    END;
    BEGIN
        p
    END.
    """
    lexer = Lexer(code)
    parser = Parser(lexer.tokenize())
    ast = parser.parse_program()

    instrumenter = Instrumenter()
    instrumented = instrumenter.instrument(ast)

    emitter = PascalEmitter()
    output = emitter.emit(instrumented)

    # Check for two decisions (IF in p, but wait, PROCEDURE itself is not a decision, only IF inside it)
    # Decision IDs are global.
    # p's IF should have a decision ID.
    assert "mcdc_begin(1); IF mcdc_cond(1, 1, x) THEN x := false" in output
    assert "PROGRAM test;" in output

def test_instrumenter_nested_control_logic():
    code = """
    BEGIN
      IF A THEN
        WHILE B DO
          IF C OR D THEN x := 1
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

    # IF A -> decision 1
    # WHILE B -> decision 2
    # IF C OR D -> decision 3
    assert "mcdc_begin(1); IF mcdc_cond(1, 1, A)" in output
    assert "mcdc_begin(2); WHILE mcdc_cond(2, 1, B)" in output
    assert "mcdc_begin(3); IF (mcdc_cond(3, 1, C) OR mcdc_cond(3, 2, D))" in output
