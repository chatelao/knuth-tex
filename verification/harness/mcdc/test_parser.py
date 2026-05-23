import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import Parser, Assignment, ProcedureCall

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
