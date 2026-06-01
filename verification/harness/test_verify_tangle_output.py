import pytest
from verification.harness.verify_tangle_output import PascalNormalizer, TangleValidator

def test_strip_comments():
    normalizer = PascalNormalizer()
    code = "program test; { comment } begin (* another *) end."
    # Strip comments now replaces comments with a space to ensure token separation
    assert normalizer.strip_comments(code).split() == ["program", "test;", "begin", "end."]

    code_nested = "code { { nested } } more code"
    # Note: Our simple regex might not handle nested comments perfectly if they are of the same type,
    # but standard Pascal doesn't really have nested comments of the same type.
    # {} and (* *) are different types and often used to 'nest' by compilers, but WEB/TANGLE output is usually simple.
    assert normalizer.strip_comments(code_nested).split() == ["code", "more", "code"]

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

def test_extract_pool_checksum():
    validator = TangleValidator("")
    pool_content = "00string1\n00string2\n*123456789\n"
    assert validator.extract_pool_checksum(pool_content) == "123456789"

    pool_no_checksum = "00string1\n"
    assert validator.extract_pool_checksum(pool_no_checksum) is None

def test_extract_pascal_checksum():
    # TeX-style checksum comparison
    code = "if a <> 123456789 then bad_pool('! TEX.POOL doesn''t match; TANGLE me again.');"
    validator = TangleValidator(code)
    assert validator.extract_pascal_checksum() == "123456789"

    # Metafont-style checksum comparison (lowercase tangle)
    code_mf = "if a <> 987654321 then bad_pool('! MF.POOL doesn''t match; tangle me again.');"
    validator_mf = TangleValidator(code_mf)
    assert validator_mf.extract_pascal_checksum() == "987654321"

    # Fallback pattern
    code_fallback = "a := 0; if a <> 111222333 then halt;"
    validator_fb = TangleValidator(code_fallback)
    assert validator_fb.extract_pascal_checksum() == "111222333"

    # No checksum found
    validator_none = TangleValidator("program Test; begin end.")
    assert validator_none.extract_pascal_checksum() is None

def test_verify_program_header():
    code = "program TANGLE(input,output); begin end."
    validator = TangleValidator(code)
    assert validator.verify_program_header("TANGLE") is True
    assert validator.verify_program_header("WEAVE") is False

    # Case insensitivity and whitespace
    code_ws = "  PROGRAM  Tex ( input , output ) ; "
    validator_ws = TangleValidator(code_ws)
    assert validator_ws.verify_program_header("Tex") is True

def test_verify_label_declaration():
    code = "program Test; label 9999; begin end."
    validator = TangleValidator(code)
    assert validator.verify_label_declaration("9999") is True
    assert validator.verify_label_declaration("1234") is False

    # Multiple labels
    code_multi = "label 10, 9999, 20;"
    validator_multi = TangleValidator(code_multi)
    assert validator_multi.verify_label_declaration("9999") is True
    assert validator_multi.verify_label_declaration("10") is True
    assert validator_multi.verify_label_declaration("30") is False
