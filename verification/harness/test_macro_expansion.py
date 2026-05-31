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
        'maxtoks': 50000,
        'maxnames': 4000,
        'maxtexts': 2000,
        'hashsize': 353,
        'longestname': 400,
        'linelength': 72,
        'outbufsize': 144,
        'stacksize': 50,
        'maxidlength': 50,
        'unambiglength': 7
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
        'longbufsize': 500,
        'linelength': 80,
        'maxrefs': 30000,
        'maxtoks': 30000,
        'maxtexts': 2000,
        'maxscraps': 1000,
        'stacksize': 400
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

def test_pltotf_macros():
    """Verify constants in PLtoTF's generated Pascal code."""
    # Values extracted from local/texware/pltotf.p
    expected = {
        'bufsize': 60,
        'maxheaderbytes': 100,
        'maxparamwords': 30,
        'maxligsteps': 5000,
        'maxkerns': 500,
        'hashsize': 5003
    }
    verify_file_macros('local/texware/pltotf.p', expected)

def test_tftopl_macros():
    """Verify constants in TFtoPL's generated Pascal code."""
    # Values extracted from local/texware/tftopl.p
    expected = {
        'tfmsize': 30000,
        'ligsize': 5000,
        'hashsize': 5003
    }
    verify_file_macros('local/texware/tftopl.p', expected)

def test_dvitype_macros():
    """Verify constants in DVItype's generated Pascal code."""
    # Values extracted from local/texware/dvitype.p
    expected = {
        'maxfonts': 100,
        'maxwidths': 10000,
        'linelength': 79,
        'terminallinelength': 150,
        'stacksize': 100,
        'namesize': 1000,
        'namelength': 100
    }
    verify_file_macros('local/texware/dvitype.p', expected)

def test_gftodvi_macros():
    """Verify constants in GFtoDVI's generated Pascal code."""
    # Values extracted from local/mfware/gftodvi.p
    expected = {
        'maxlabels': 2000,
        'poolsize': 10000,
        'maxstrings': 1100,
        'terminallinelength': 150,
        'filenamesize': 1024,
        'fontmemsize': 2000,
        'dvibufsize': 800,
        'widestrow': 8192,
        'liglookahead': 20
    }
    verify_file_macros('local/mfware/gftodvi.p', expected)
