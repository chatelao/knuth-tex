import pytest
from verification.harness.verify_tangle_output import TangleValidator

def verify_file_macros(pascal_file, expected_macros):
    with open(pascal_file, 'r') as f:
        code = f.read()
    validator = TangleValidator(code)
    results = validator.verify_macro_expansion(expected_macros)

    for name, actual, expected, success in results:
        assert success, f"Macro {name} in {pascal_file} failed: expected {expected}, got {actual}"

def test_tangle_macros():
    """Verify constants in TANGLE's generated Pascal code."""
    # Values extracted from local/web/tangle.p
    expected = {
        'bufsize': 100,
        'maxbytes': 45000,
        'maxnames': 4000,
        'maxtexts': 2000,
        'hashsize': 353,
        'longestname': 400
    }
    verify_file_macros('local/web/tangle.p', expected)

def test_weave_macros():
    """Verify constants in WEAVE's generated Pascal code."""
    # Values extracted from local/web/weave.p
    expected = {
        'maxbytes': 45000,
        'maxnames': 5000,
        'maxmodules': 2000,
        'hashsize': 353,
        'bufsize': 100,
        'longestname': 400,
        'maxrefs': 30000,
        'maxtoks': 30000,
        'maxtexts': 2000
    }
    verify_file_macros('local/web/weave.p', expected)

def test_vftovp_macros():
    """Verify constants in VFtoVP's generated Pascal code."""
    # Values extracted from local/etc/vftovp.p
    expected = {
        'tfmsize': 30000,
        'vfsize': 10000,
        'maxfonts': 300,
        'ligsize': 5000,
        'hashsize': 5003,
        'maxstack': 50
    }
    verify_file_macros('local/etc/vftovp.p', expected)

def test_vptovf_macros():
    """Verify constants in VPtoVF's generated Pascal code."""
    # Values extracted from local/etc/vptovf.p
    expected = {
        'bufsize': 60,
        'vfsize': 10000,
        'maxstack': 100,
        'hashsize': 5003
    }
    verify_file_macros('local/etc/vptovf.p', expected)
