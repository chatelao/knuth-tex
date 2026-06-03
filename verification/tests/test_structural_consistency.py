import pytest
import os
from pathlib import Path
from verification.harness.verify_structural_consistency import StructuralConsistencyValidator

def test_tangle_structural_consistency():
    web_file = 'dist/web/tangle.web'
    pascal_file = 'local/web/tangle.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for TANGLE"

def test_weave_structural_consistency():
    web_file = 'dist/web/weave.web'
    pascal_file = 'local/web/weave.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for WEAVE"

def test_vftovp_structural_consistency():
    web_file = 'dist/etc/vftovp.web'
    pascal_file = 'local/etc/vftovp.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for VFtoVP"

def test_vptovf_structural_consistency():
    web_file = 'dist/etc/vptovf.web'
    pascal_file = 'local/etc/vptovf.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for VPtoVF"

def test_tftopl_structural_consistency():
    web_file = 'dist/texware/tftopl.web'
    pascal_file = 'local/texware/tftopl.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for TFtoPL"

def test_pltotf_structural_consistency():
    web_file = 'dist/texware/pltotf.web'
    pascal_file = 'local/texware/pltotf.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for PLtoTF"

def test_dvitype_structural_consistency():
    web_file = 'dist/texware/dvitype.web'
    pascal_file = 'local/texware/dvitype.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for DVItype"

def test_pooltype_structural_consistency():
    web_file = 'dist/texware/pooltype.web'
    pascal_file = 'local/texware/pooltype.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for pooltype"

def test_gftodvi_structural_consistency():
    web_file = 'dist/mfware/gftodvi.web'
    pascal_file = 'local/mfware/gftodvi.p'

    if not os.path.exists(web_file):
        pytest.skip(f"WEB file not found: {web_file}")
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    validator = StructuralConsistencyValidator(web_file, pascal_file)
    assert validator.verify(), "Structural consistency verification failed for GFtoDVI"
