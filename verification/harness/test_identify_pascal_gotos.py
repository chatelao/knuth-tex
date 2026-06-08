import pytest
from verification.harness.identify_pascal_gotos import PascalGOTOExtractor
import os

def test_identify_pascal_gotos_basic(tmp_path):
    pascal_content = """
{1:}program test;
label 9999, exit;
begin
  {2:}
  goto 9999;
  {:2}
  {3:}
  goto exit;
  {:3}
end.
{:1}
"""
    p_file = tmp_path / "test.p"
    p_file.write_text(pascal_content)

    extractor = PascalGOTOExtractor()
    gotos, labels = extractor.identify_gotos(str(p_file))

    # Verify labels
    assert len(labels) == 2
    assert labels[0]['label'] == '9999'
    assert labels[0]['module'] == 1
    assert labels[1]['label'] == 'exit'
    assert labels[1]['module'] == 1

    # Verify gotos
    assert len(gotos) == 2
    assert gotos[0]['target'] == '9999'
    assert gotos[0]['module'] == 2
    assert gotos[1]['target'] == 'exit'
    assert gotos[1]['module'] == 3

def test_identify_pascal_gotos_nested_comments(tmp_path):
    pascal_content = """
{1:}
begin
  { goto in comment }
  { {nested} goto ignored }
  goto actual; { comment after }
  (* (*nested*) goto ignored *)
  'goto in string'
end.
{:1}
"""
    p_file = tmp_path / "test.p"
    p_file.write_text(pascal_content)

    extractor = PascalGOTOExtractor()
    gotos, labels = extractor.identify_gotos(str(p_file))

    assert len(gotos) == 1
    assert gotos[0]['target'] == 'actual'
    assert gotos[0]['module'] == 1

def test_identify_pascal_gotos_overlapping_markers(tmp_path):
    # Testing more complex marker sequence
    pascal_content = """
{1:}
{2:}
goto 10;
{:2}
{3:}
goto 20;
{:3}
{:1}
"""
    p_file = tmp_path / "test.p"
    p_file.write_text(pascal_content)

    extractor = PascalGOTOExtractor()
    gotos, labels = extractor.identify_gotos(str(p_file))

    assert len(gotos) == 2
    assert gotos[0]['target'] == '10'
    assert gotos[0]['module'] == 2
    assert gotos[1]['target'] == '20'
    assert gotos[1]['module'] == 3

def test_strip_comments_and_strings_markers():
    extractor = PascalGOTOExtractor()
    code = "{1:}goto 10;{:1}{comment}"

    # Without preserving markers
    stripped = extractor.strip_comments_and_strings(code, preserve_markers=False)
    assert "{1:}" not in stripped
    assert "{:1}" not in stripped
    assert "goto 10;" in stripped
    assert "comment" not in stripped

    # With preserving markers
    stripped_m = extractor.strip_comments_and_strings(code, preserve_markers=True)
    assert "{1:}" in stripped_m
    assert "{:1}" in stripped_m
    assert "goto 10;" in stripped_m
    assert "comment" not in stripped_m
