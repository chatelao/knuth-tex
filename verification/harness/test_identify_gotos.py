import pytest
from verification.harness.identify_gotos import identify_gotos
import os

def test_identify_gotos_basic(tmp_path):
    web_content = """@
@d label1 == 10
@d goto_label1 == goto label1
@p
program test;
label label1;
begin
  goto label1;
end.

@
@<Other block@>=
begin
  goto 20;
end
"""
    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    gotos, labels, macros = identify_gotos(str(web_file))

    assert len(labels) == 1
    assert labels[0]['label'] == 'label1'
    assert labels[0]['module'] == 1

    assert len(gotos) == 2
    assert gotos[0]['target'] == 'label1'
    assert gotos[0]['module'] == 1
    assert gotos[1]['target'] == '20'
    assert gotos[1]['module'] == 2

    assert macros['label1'] == '10'
    assert macros['goto_label1'] == 'goto label1'

def test_identify_gotos_comments(tmp_path):
    web_content = """@
@p
begin
  { goto in comment }
  goto actual; { comment after }
end.
"""
    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    gotos, labels, macros = identify_gotos(str(web_file))

    assert len(gotos) == 1
    assert gotos[0]['target'] == 'actual'
