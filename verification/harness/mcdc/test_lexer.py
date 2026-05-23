import pytest
from verification.harness.mcdc.lexer import Lexer, LexerError

def test_basic_tokens():
    code = "PROGRAM TANGLE(input,output); BEGIN x := 123; END."
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    # PROGRAM, TANGLE, (, input, ,, output, ), ;, BEGIN, x, :=, 123, ;, END, .

    types = [t.type for t in tokens]
    assert 'PROGRAM' in types
    assert 'BEGIN' in types
    assert 'ASSIGN' in types
    assert 'NUMBER' in types
    assert 'END' in types

    # Check specific token values
    assert tokens[0].value == "PROGRAM"
    assert tokens[1].value == "TANGLE"
    assert tokens[2].value == "("
    assert tokens[8].type == "BEGIN"
    assert tokens[10].type == "ASSIGN"
    assert tokens[11].value == "123"

def test_strings():
    code = "s := 'Hello, ''World'''; "
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    assert tokens[2].type == "STRING"
    assert tokens[2].value == "'Hello, ''World'''"

def test_comments():
    code = "{ This is a \n multiline comment } BEGIN"
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    assert tokens[0].type == "COMMENT"
    assert tokens[1].type == "BEGIN"
    assert tokens[1].line == 2

def test_tangle_extensions():
    code = '#include "tangext.h" IF x THEN OTHERWISE'
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    assert tokens[0].type == "INCLUDE"
    assert tokens[1].type == "IF"
    assert tokens[3].type == "THEN"
    assert tokens[4].type == "OTHERWISE"

def test_case_insensitivity():
    code = "begin if x then end"
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "IF"
    assert tokens[3].type == "THEN"
    assert tokens[4].type == "END"

def test_error_handling():
    code = "x := 1 $ 2"
    lexer = Lexer(code)
    with pytest.raises(LexerError) as excinfo:
        lexer.tokenize()
    assert "Unexpected character '$'" in str(excinfo.value)
    assert excinfo.value.line == 1
    assert excinfo.value.column == 8

def test_tangle_snippet():
    # Snippet from local/web/tangle.p
    code = """
    {2:}{4:}{:4}program TANGLE(input,output);label 9999;const{8:}
    bufsize=100;maxbytes=45000;
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    # 0:{2:}, 1:{4:}, 2:{:4}, 3:program, 4:TANGLE, 5:(, 6:input, 7:,, 8:output, 9:), 10:;, 11:label, 12:9999, 13:;, 14:const, 15:{8:}

    assert tokens[0].type == "COMMENT"
    assert tokens[1].type == "COMMENT"
    assert tokens[2].type == "COMMENT"
    assert tokens[3].type == "PROGRAM"
    assert tokens[11].type == "LABEL"
    assert tokens[14].type == "CONST"
    assert tokens[15].type == "COMMENT"
