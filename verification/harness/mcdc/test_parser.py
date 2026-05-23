import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import (
    Parser, Assignment, ProcedureCall, Block, IfStatement, EmptyStatement, ParserError,
    WhileStatement, RepeatStatement, ForStatement
)

def test_parse_simple_assignment():
    code = "x := 1;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "x"
    assert "1" in repr(stmt.expr)

def test_parse_complex_assignment():
    code = "bytemem[w, k] := buffer[i];"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "bytemem"
    assert len(stmt.target.modifiers) == 1
    assert stmt.target.modifiers[0][0] == 'subscript'
    assert "buffer [ i ]" in repr(stmt.expr)

def test_parse_procedure_call_no_args():
    code = "initialize;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, ProcedureCall)
    assert stmt.name.name == "initialize"
    assert len(stmt.args) == 0

def test_parse_procedure_call_with_args():
    code = "write(output, xchr[buffer[k-1]]);"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, ProcedureCall)
    assert stmt.name.name == "write"
    assert len(stmt.args) == 2
    assert "output" in repr(stmt.args[0])
    assert "xchr [ buffer [ k - 1 ] ]" in repr(stmt.args[1])

def test_parse_dotted_identifier():
    code = "curstate.namefield := p;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "curstate"
    assert stmt.target.modifiers[0] == ('dot', 'namefield')

def test_parse_with_label():
    code = "31: p := hash[h];"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "p"

def test_parse_nested_expressions():
    code = "h := (h + h + buffer[i]) mod hashsize;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "h"
    assert "mod hashsize" in repr(stmt.expr)

def test_parse_pointer_deref():
    code = "p^.link := 0;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "p"
    assert stmt.target.modifiers[0] == ('pointer', None)
    assert stmt.target.modifiers[1] == ('dot', 'link')
    assert repr(stmt.target) == "p^.link"

def test_parse_block():
    code = "BEGIN x := 1; y := 2 END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Block)
    assert len(stmt.statements) == 2
    assert stmt.statements[0].target.name == "x"
    assert stmt.statements[1].target.name == "y"

def test_parse_if_then():
    code = "IF x > 0 THEN x := 1;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, IfStatement)
    assert "x > 0" in repr(stmt.condition)
    assert stmt.then_branch.target.name == "x"
    assert stmt.else_branch is None

def test_parse_if_then_else():
    code = "IF x > 0 THEN x := 1 ELSE x := 0;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, IfStatement)
    assert stmt.then_branch.target.name == "x"
    assert stmt.else_branch.target.name == "x"

def test_parse_nested_if():
    code = "IF x > 0 THEN IF y > 0 THEN z := 1 ELSE z := 0;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, IfStatement)
    assert isinstance(stmt.then_branch, IfStatement)
    assert stmt.then_branch.else_branch.target.name == "z"

def test_parse_block_with_semicolons():
    code = "BEGIN ; ; END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Block)
    # Empty statements might or might not be counted depending on how parse_block handles them
    # Current implementation: while peek != END: parse_statement; if peek == ';': consume
    # BEGIN ; (EmptyStmt) ; (EmptyStmt) END
    assert len(stmt.statements) >= 2

def test_parse_block_infinite_loop_prevention():
    # 'ELSE' outside of IF is not handled by parse_statement except as EmptyStatement,
    # but in a block it needs to progress.
    code = "BEGIN ELSE END"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)

    # In the current implementation, ELSE in a block returns EmptyStatement.
    # So it should progress. Let's try something that truly doesn't progress.
    # Actually, almost everything in parse_statement either consumes or returns EmptyStatement.
    # EmptyStatement is returned for END, ELSE, UNTIL, and ';'.
    # If it is END, the loop in parse_block terminates.
    # If it is ELSE, UNTIL or ';', the loop continues.
    # If it is ';', it is consumed in parse_block.
    # If it is ELSE or UNTIL, it is NOT consumed in parse_block and WOULD loop
    # if not for the progress check.

    with pytest.raises(ParserError, match="Parser failed to progress"):
        parser.parse_statement()

def test_parse_while():
    code = "WHILE x > 0 DO x := x - 1;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, WhileStatement)
    assert "x > 0" in repr(stmt.condition)
    assert isinstance(stmt.body, Assignment)
    assert stmt.body.target.name == "x"

def test_parse_repeat():
    code = "REPEAT x := x + 1; y := y - 1 UNTIL x > 10;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, RepeatStatement)
    assert len(stmt.statements) == 2
    assert "x > 10" in repr(stmt.condition)

def test_parse_for_to():
    code = "FOR i := 1 TO 10 DO write(i);"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, ForStatement)
    assert stmt.variable.name == "i"
    assert "1" in repr(stmt.start_expr)
    assert stmt.direction == "TO"
    assert "10" in repr(stmt.end_expr)
    assert isinstance(stmt.body, ProcedureCall)

def test_parse_for_downto():
    code = "FOR i := 10 DOWNTO 1 DO write(i);"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, ForStatement)
    assert stmt.direction == "DOWNTO"

def test_nested_loops():
    code = """
    FOR i := 1 TO 10 DO
        WHILE j < 5 DO
            REPEAT
                j := j + 1
            UNTIL j = 5;
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, ForStatement)
    assert isinstance(stmt.body, WhileStatement)
    assert isinstance(stmt.body.body, RepeatStatement)
