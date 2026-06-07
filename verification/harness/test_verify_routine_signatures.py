import pytest
import os
from verification.harness.verify_routine_signatures import verify_signatures, normalize_name

def test_normalize_name():
    assert normalize_name("open_input") == "openinput"
    assert normalize_name("Open_Input") == "openinput"
    assert normalize_name("OpenInput") == "openinput"

def test_verify_signatures_basic(tmp_path):
    web_content = "@ @p procedure open_input; begin end;"
    pascal_content = "procedure openinput; begin end;"

    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    pascal_file = tmp_path / "test.p"
    pascal_file.write_text(pascal_content)

    results = verify_signatures(str(web_file), str(pascal_file))

    assert len(results['matched']) == 1
    assert results['matched'][0][0]['name'] == 'open_input'
    assert results['matched'][0][1]['name'] == 'openinput'
    assert len(results['missing']) == 0
    assert len(results['extra_pascal']) == 0

def test_verify_signatures_mismatch_kind(tmp_path):
    web_content = "@ @p function input_ln: boolean; begin end;"
    pascal_content = "procedure inputln; begin end;"

    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    pascal_file = tmp_path / "test.p"
    pascal_file.write_text(pascal_content)

    results = verify_signatures(str(web_file), str(pascal_file))

    assert len(results['matched']) == 0
    assert len(results['mismatched_kind']) == 1
    assert results['mismatched_kind'][0][0]['name'] == 'input_ln'
    assert results['mismatched_kind'][0][1]['kind'] == 'procedure'

def test_verify_signatures_mismatch_params(tmp_path):
    web_content = "@ @p procedure p(a: integer); begin end;"
    pascal_content = "procedure p(b: integer); begin end;"

    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    pascal_file = tmp_path / "test.p"
    pascal_file.write_text(pascal_content)

    results = verify_signatures(str(web_file), str(pascal_file))

    assert len(results['matched']) == 0
    assert len(results['mismatched_params']) == 1

def test_verify_signatures_mismatch_return(tmp_path):
    web_content = "@ @p function f: integer; begin end;"
    pascal_content = "function f: boolean; begin end;"

    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    pascal_file = tmp_path / "test.p"
    pascal_file.write_text(pascal_content)

    results = verify_signatures(str(web_file), str(pascal_file))

    assert len(results['matched']) == 0
    assert len(results['mismatched_return']) == 1

def test_verify_signatures_forward(tmp_path):
    web_content = "@ @p procedure p; begin end;"
    pascal_content = "procedure p; forward; procedure p; begin end;"

    web_file = tmp_path / "test.web"
    web_file.write_text(web_content)

    pascal_file = tmp_path / "test.p"
    pascal_file.write_text(pascal_content)

    results = verify_signatures(str(web_file), str(pascal_file))

    assert len(results['matched']) == 1
    assert results['matched'][0][1]['directive'] is None # Should match implementation, not forward
