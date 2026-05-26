import yaml
from pathlib import Path

def test_validate_hlr_yaml():
    hlr_path = Path("verification/reqs/hlr.yaml")
    with open(hlr_path, 'r') as f:
        data = yaml.safe_load(f)
    assert isinstance(data, list)
    for item in data:
        assert 'id' in item
        assert 'description' in item
        assert 'category' in item
        assert 'source' in item

def test_validate_llr_tex_yaml():
    llr_path = Path("verification/reqs/llr_tex.yaml")
    with open(llr_path, 'r') as f:
        data = yaml.safe_load(f)
    assert isinstance(data, list)
    for item in data:
        assert 'id' in item
        assert 'web_section' in item
        assert 'description' in item
        assert 'parent_hlr' in item

def test_validate_llr_mf_yaml():
    llr_path = Path("verification/reqs/llr_mf.yaml")
    with open(llr_path, 'r') as f:
        data = yaml.safe_load(f)
    assert isinstance(data, list)
    for item in data:
        assert 'id' in item
        assert 'web_section' in item
        assert 'description' in item
        assert 'parent_hlr' in item

def test_validate_matrix_yaml():
    matrix_path = Path("verification/trace/matrix.yaml")
    with open(matrix_path, 'r') as f:
        data = yaml.safe_load(f)
    assert isinstance(data, list)
    for item in data:
        assert 'hlr_id' in item
        assert 'llr_ids' in item
        assert 'test_case_ids' in item

def test_validate_tor_harness_yaml():
    tor_path = Path("verification/reqs/tor_harness.yaml")
    with open(tor_path, 'r') as f:
        data = yaml.safe_load(f)
    assert isinstance(data, list)
    for item in data:
        assert 'id' in item
        assert 'description' in item
        assert 'category' in item
