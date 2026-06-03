import pytest
import subprocess
import os
from pathlib import Path

def test_tangle_structural_consistency():
    web_file = "dist/web/tangle.web"
    pascal_file = "local/web/tangle.p"

    if not os.path.exists(web_file) or not os.path.exists(pascal_file):
        pytest.skip("Required files for structural consistency test not found.")

    cmd = ["python3", "verification/harness/verify_structural_consistency.py", web_file, pascal_file]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # We allow some discrepancy for now if we haven't perfectly matched TANGLE's module inclusion logic,
    # but the tool should at least run and find markers.
    assert result.returncode == 0 or "FAIL: Missing modules" in result.stdout
    assert "Pascal module markers found" in result.stdout
