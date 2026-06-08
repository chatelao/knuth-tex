import pytest
import os
from verification.harness.verify_module_sequence import verify_module_sequence

def test_tangle_module_sequence():
    web_file = 'dist/web/tangle.web'
    pascal_file = 'local/web/tangle.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    assert verify_module_sequence(web_file, pascal_file)

def test_weave_module_sequence():
    web_file = 'dist/web/weave.web'
    pascal_file = 'local/web/weave.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    assert verify_module_sequence(web_file, pascal_file)

def test_dvitype_module_sequence():
    web_file = 'dist/texware/dvitype.web'
    pascal_file = 'local/texware/dvitype.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    assert verify_module_sequence(web_file, pascal_file)
