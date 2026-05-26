import pytest
from verification.harness.mcdc.lexer import Lexer
from verification.harness.mcdc.parser import (
    Parser, Assignment, ProcedureCall, Block, IfStatement, EmptyStatement, ParserError,
    WhileStatement, RepeatStatement, ForStatement, CaseStatement, CaseItem,
    Program, LabelDeclaration, ConstDeclaration, TypeDeclaration, VarDeclaration,
    ProcedureDeclaration, FunctionDeclaration, GotoStatement, LabeledStatement
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
    # New repr format: Expr(buffer[Expr(i)])
    assert "buffer[Expr(i)]" in repr(stmt.expr)

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
    # New repr format: Expr(xchr[Expr(buffer[Expr((k - 1))])])
    assert "xchr[Expr(buffer[Expr((k - 1))])]" in repr(stmt.args[1])

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

    assert isinstance(stmt, LabeledStatement)
    assert stmt.label == "31"
    assert isinstance(stmt.statement, Assignment)
    assert stmt.statement.target.name == "p"

def test_parse_nested_expressions():
    code = "h := (h + h + buffer[i]) mod hashsize;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    assert stmt.target.name == "h"
    # New tree structure: (((h + h) + buffer[Expr(i)]) mod hashsize)
    assert "MOD HASHSIZE" in repr(stmt.expr).upper()

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

def test_complex_boolean_expression():
    code = "IF (a > 0) AND (b < 10) OR NOT c THEN x := 1;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, IfStatement)
    # Check tree structure roughly via repr
    # OR has lower precedence than AND
    # ((a > 0) AND (b < 10)) OR (NOT c)
    repr_str = repr(stmt.condition)
    assert "OR" in repr_str
    assert "AND" in repr_str
    assert "NOT" in repr_str
    assert "((a > 0) AND (b < 10))" in repr_str or "Expr(((a > 0) AND (b < 10)))" in repr_str

def test_parse_case_statement():
    code = """
    CASE x OF
        1: y := 1;
        2, 3: BEGIN y := 2; z := 3 END;
        OTHERWISE y := 0
    END
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, CaseStatement)
    assert "x" in repr(stmt.expression)
    assert len(stmt.items) == 2
    assert "1" in repr(stmt.items[0].labels[0])
    assert "2" in repr(stmt.items[1].labels[0])
    assert "3" in repr(stmt.items[1].labels[1])
    assert isinstance(stmt.items[1].statement, Block)
    assert stmt.otherwise is not None
    assert stmt.otherwise.target.name == "y"

def test_operator_precedence():
    code = "x := a + b * c = d OR e AND f;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    # Precedence in Pascal:
    # 1. NOT (Highest)
    # 2. *, /, DIV, MOD, AND (Multiplying operators)
    # 3. +, -, OR (Adding operators)
    # 4. =, <>, <, <=, >, >=, IN (Relational operators) (Lowest)

    # x := ( (a + (b * c)) = (d OR (e AND f)) )
    # Wait, d OR (e AND f) is parsed because OR and AND have higher precedence than =.
    # In Pascal, 1 + 2 = 3 is (1+2)=3.
    # a + b * c = d OR e AND f
    # term1: a + (b * c)
    # term2: d OR (e AND f)
    # result: (term1 = term2)

    repr_str = repr(stmt.expr)
    assert "((a + (b * c)) = (d OR (e AND f)))" in repr_str

def test_parse_full_program():
    code = """
    PROGRAM test(input, output);
    LABEL 1, 2;
    CONST c = 10;
    VAR x, y: integer;
    PROCEDURE p(a: integer);
    BEGIN
        x := a
    END;
    BEGIN
        p(c);
        GOTO 1;
        1: x := 0
    END.
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    prog = parser.parse_program()

    assert isinstance(prog, Program)
    assert prog.name == "test"
    assert prog.args == ["input", "output"]
    assert len(prog.declarations) == 4
    assert isinstance(prog.declarations[0], LabelDeclaration)
    assert isinstance(prog.declarations[1], ConstDeclaration)
    assert isinstance(prog.declarations[2], VarDeclaration)
    assert isinstance(prog.declarations[3], ProcedureDeclaration)
    assert isinstance(prog.block, Block)

def test_parse_function_declaration():
    code = """
    FUNCTION f(a, b: integer): boolean;
    VAR x: integer;
    BEGIN
        f := a > b
    END;
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    func = parser.parse_routine_declaration()

    assert isinstance(func, FunctionDeclaration)
    assert func.name == "f"
    # Lexer adds spaces around operators and punctuation
    assert "a , b : integer" in func.params
    assert func.return_type == "boolean"
    assert len(func.declarations) == 1
    assert isinstance(func.declarations[0], VarDeclaration)
    assert isinstance(func.block, Block)

def test_parse_nested_case():
    code = """
    CASE x OF
        1: CASE y OF
            1: z := 1;
            2: z := 2
           END;
        2: z := 3
    END
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, CaseStatement)
    assert len(stmt.items) == 2
    assert isinstance(stmt.items[0].statement, CaseStatement)
    assert len(stmt.items[0].statement.items) == 2

def test_parse_complex_record_access():
    code = "a[i].b^.c[j] := 1;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    stmt = parser.parse_statement()

    assert isinstance(stmt, Assignment)
    target = stmt.target
    assert target.name == "a"
    # a[i].b^.c[j] has 5 modifiers: subscript, dot, pointer, dot, subscript
    assert len(target.modifiers) == 5
    assert target.modifiers[0][0] == 'subscript'
    assert target.modifiers[1] == ('dot', 'b')
    assert target.modifiers[2] == ('pointer', None)
    assert target.modifiers[3] == ('dot', 'c')
    assert target.modifiers[4][0] == 'subscript'

def test_parse_type_declaration():
    code = """
    TYPE
        byte = 0..255;
        word = record l, r: byte end;
    VAR w: word;
    """
    # We can use parse_declarations by providing a mock parser state if we want,
    # but easier to just wrap in a dummy program or just test the declarations part.
    # Actually, parse_program is the main entry point for declarations.
    code = "PROGRAM t; " + code + " BEGIN END."
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    prog = parser.parse_program()

    type_decl = next(d for d in prog.declarations if isinstance(d, TypeDeclaration))
    assert len(type_decl.types) == 2
    assert type_decl.types[0] == ("byte", "0 .. 255")
    assert type_decl.types[1][0] == "word"
    assert type_decl.types[1][1].lower() == "record l , r : byte end"
