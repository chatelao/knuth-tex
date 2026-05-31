import pytest
import os
from pathlib import Path
from verification.harness.verify_pascal_extensions import PascalExtensionValidator

def verify_extension_usage(pascal_file, extensions, required_usage=None, required_declaration=None):
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    if required_usage is None:
        required_usage = extensions
    if required_declaration is None:
        required_declaration = extensions

    validator = PascalExtensionValidator(pascal_file)
    for ext in extensions:
        declared, used = validator.verify_extension(ext)
        if ext in required_declaration:
            assert declared, f"Extension {ext} not declared for {pascal_file}"
        if ext in required_usage:
            assert used, f"Extension {ext} not used in {pascal_file}"

def test_tangle_extensions():
    verify_extension_usage('local/web/tangle.p', ['argc', 'argv', 'flushstdout', 'lineread', 'testeof', 'exit'])

def test_weave_extensions():
    verify_extension_usage('local/web/weave.p', ['argc', 'argv', 'flushstdout', 'lineread', 'testeof', 'exit'])

def test_tangle_sparc_extensions():
    verify_extension_usage(
        'local/web-sparc/tangle.p',
        ['argc', 'argv', 'lineread', 'linewrite', 'testeof', 'exit'],
        required_declaration=['lineread', 'linewrite', 'testeof', 'exit']
    )

def test_vftovp_extensions():
    verify_extension_usage('local/etc/vftovp.p', ['argc', 'argv', 'flushstdout', 'setpaths', 'testaccess'], required_usage=['argc', 'argv', 'setpaths', 'testaccess'])

def test_vptovf_extensions():
    verify_extension_usage('local/etc/vptovf.p', ['argc', 'argv'], required_usage=['argc', 'argv'])

def test_pltotf_extensions():
    # Use glob to find the correct path as it might vary (e.g., local/texware/ or local/texware-sparc/)
    paths = list(Path('local').rglob('pltotf.p'))
    if not paths:
        pytest.skip("pltotf.p not found")
    verify_extension_usage(str(paths[0]), ['argc', 'argv'], required_usage=['argc', 'argv'])

def test_tftopl_extensions():
    paths = list(Path('local').rglob('tftopl.p'))
    if not paths:
        pytest.skip("tftopl.p not found")
    verify_extension_usage(str(paths[0]), ['argc', 'argv'], required_usage=['argc', 'argv'])

def test_dvitype_extensions():
    paths = list(Path('local').rglob('dvitype.p'))
    if not paths:
        pytest.skip("dvitype.p not found")
    verify_extension_usage(str(paths[0]), ['argc', 'argv', 'flushstdout', 'setpaths', 'testaccess'])

def test_gftodvi_extensions():
    verify_extension_usage('local/mfware/gftodvi.p', ['argc', 'argv', 'flushstdout', 'setpaths', 'testaccess'])
