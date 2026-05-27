import pytest
from verification.harness.verify_mf_margins import verify_mf_margins, extract_web_definition
import os

def test_extract_web_definition():
    content = """
@d move_increment=11 {number of items pushed by |make_moves|}
@!bistack_size=785; {size of stack for bisection algorithms;
@d int_packets=20 {number of words to represent $U_k$, $V_k$, $X_k$, and $Y_k$}
@d int_increment=int_packets+int_packets+5 {number of stack words per level}
"""
    assert extract_web_definition(content, "move_increment") == "11"
    assert extract_web_definition(content, "bistack_size") == "785"
    assert extract_web_definition(content, "int_packets") == "20"
    assert extract_web_definition(content, "int_increment") == "int_packets+int_packets+5"

def test_verify_mf_margins_success(tmp_path):
    web_file = tmp_path / "mf.web"
    content = """
@d move_increment=11
@!bistack_size=785;
@d int_packets=20
@d int_increment=int_packets+int_packets+5
"""
    web_file.write_text(content)
    success, message = verify_mf_margins(str(web_file))
    assert success is True
    assert "maintained" in message

def test_verify_mf_margins_failure_bad31(tmp_path):
    web_file = tmp_path / "mf.web"
    content = """
@d move_increment=100
@!bistack_size=785;
@d int_packets=20
@d int_increment=int_packets+int_packets+5
"""
    web_file.write_text(content)
    success, message = verify_mf_margins(str(web_file))
    assert success is False
    assert "bad=31" in message

def test_verify_mf_margins_failure_bad32(tmp_path):
    web_file = tmp_path / "mf.web"
    content = """
@d move_increment=11
@!bistack_size=100;
@d int_packets=20
@d int_increment=int_packets+int_packets+5
"""
    web_file.write_text(content)
    success, message = verify_mf_margins(str(web_file))
    assert success is False
    assert "bad=32" in message

def test_verify_mf_margins_real_file():
    # Verify it works on the actual file in the repo
    if os.path.exists("dist/mf/mf.web"):
        success, message = verify_mf_margins("dist/mf/mf.web")
        assert success is True
    else:
        pytest.skip("dist/mf/mf.web not found")
