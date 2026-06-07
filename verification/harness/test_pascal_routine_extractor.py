import pytest
from verification.harness.pascal_routine_extractor import PascalRoutineExtractor

def test_extract_simple_procedure():
    code = "procedure simple; begin end;"
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 1
    assert sigs[0]['kind'] == 'procedure'
    assert sigs[0]['name'] == 'simple'
    assert sigs[0]['params'] == ''
    assert sigs[0]['return_type'] == ''

def test_extract_procedure_with_params():
    code = "procedure with_params(a: integer; b: boolean); begin end;"
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 1
    assert sigs[0]['name'] == 'with_params'
    assert sigs[0]['params'] == '(a: integer; b: boolean)'

def test_extract_function():
    code = "function add(a, b: integer): integer; begin end;"
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 1
    assert sigs[0]['kind'] == 'function'
    assert sigs[0]['name'] == 'add'
    assert sigs[0]['params'] == '(a, b: integer)'
    assert sigs[0]['return_type'] == 'integer'

def test_extract_forward_declaration():
    code = "procedure future; forward; procedure future; begin end;"
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 2
    assert sigs[0]['name'] == 'future'
    assert sigs[0]['directive'] == 'forward'
    assert sigs[1]['name'] == 'future'
    assert sigs[1]['directive'] is None

def test_extract_with_comments_and_strings():
    code = """
    { This is a comment }
    procedure real_proc(s: string); { another comment }
    begin
      writeln('This is not a procedure name');
    end;
    """
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 1
    assert sigs[0]['name'] == 'real_proc'
    assert sigs[0]['params'] == '(s: string)'

def test_multiple_routines():
    code = """
    procedure p1; forward;
    function f1(x: real): real; begin end;
    procedure p1; begin end;
    """
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 3
    assert sigs[0]['name'] == 'p1'
    assert sigs[1]['name'] == 'f1'
    assert sigs[2]['name'] == 'p1'

def test_external_directive():
    code = "procedure os_exit(n: integer); external;"
    extractor = PascalRoutineExtractor()
    sigs = extractor.extract_signatures(code)
    assert len(sigs) == 1
    assert sigs[0]['name'] == 'os_exit'
    assert sigs[0]['directive'] == 'external'
