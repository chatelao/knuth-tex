import pytest
from verification.harness.verify_tangle_output import PascalNormalizer, TangleValidator

def test_strip_comments():
    normalizer = PascalNormalizer()
    code = "program test; { comment } begin (* another *) end."
    assert normalizer.strip_comments(code) == "program test;  begin  end."

    code_nested = "code { { nested } } more code"
    # Note: Our simple regex might not handle nested comments perfectly if they are of the same type,
    # but standard Pascal doesn't really have nested comments of the same type.
    # {} and (* *) are different types and often used to 'nest' by compilers, but WEB/TANGLE output is usually simple.
    assert normalizer.strip_comments(code_nested) == "code  more code"

def test_normalize_whitespace():
    normalizer = PascalNormalizer()
    code = "  word1    word2\nword3  "
    assert normalizer.normalize_whitespace(code) == "word1 word2 word3"

def test_extract_constants():
    code = """
    program Test;
    const
      memmax = 30000;
      bufsize = 500;
      poolname = 'TeX.pool';
    type
      internalfontnumber = 0..fontmax;
    begin
    end.
    """
    validator = TangleValidator(code)
    constants = validator.extract_constants()
    assert constants['memmax'] == '30000'
    assert constants['bufsize'] == '500'
    assert constants['poolname'] == "'TeX.pool'"

def test_verify_macro_expansion():
    code = "const memmax = 30000; bufsize = 500; type"
    validator = TangleValidator(code)

    expected = {'memmax': 30000, 'bufsize': 500}
    results = validator.verify_macro_expansion(expected)
    assert all(r[3] for r in results) # all success

    expected_fail = {'memmax': 20000}
    results_fail = validator.verify_macro_expansion(expected_fail)
    assert results_fail[0][3] is False
    assert results_fail[0][1] == '30000'
    assert results_fail[0][2] == '20000'

def test_extract_constants_case_insensitive():
    code = "CONST MemMax = 30000; TYPE"
    validator = TangleValidator(code)
    constants = validator.extract_constants()
    # Note: extract_constants currently returns names as they appear in the source
    assert constants['MemMax'] == '30000'

def test_no_const_section():
    code = "program Test; var x: integer; begin end."
    validator = TangleValidator(code)
    assert validator.extract_constants() == {}
