import pytest
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch
from verification.harness.gftype import GFtypeWrapper

@pytest.fixture
def gftype_wrapper():
    return GFtypeWrapper("gftype")

def test_gftype_convert_stdout(gftype_wrapper, tmp_path):
    gf_file = tmp_path / "test.gf"
    gf_file.write_bytes(b"dummy gf")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="Symbolic GF output", stderr="")
        gftype_wrapper.convert(str(gf_file), str(output_file))
        assert output_file.exists()
        assert output_file.read_text() == "Symbolic GF output"

def test_gftype_convert_hardcoded_file(gftype_wrapper, tmp_path):
    gf_file = tmp_path / "test.gf"
    gf_file.write_bytes(b"dummy gf")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        def side_effect(*args, **kwargs):
            cwd = kwargs.get('cwd')
            (Path(cwd) / "gftype.out").write_text("Hardcoded GF file content")
            return MagicMock(returncode=0, stdout="", stderr="")
        mock_run.side_effect = side_effect

        gftype_wrapper.convert(str(gf_file), str(output_file))
        assert output_file.exists()
        assert output_file.read_text() == "Hardcoded GF file content"

def test_gftype_file_not_found(gftype_wrapper):
    with pytest.raises(FileNotFoundError):
        gftype_wrapper.convert("non_existent.gf", "out.typ")

def test_gftype_execution_failure(gftype_wrapper, tmp_path):
    gf_file = tmp_path / "test.gf"
    gf_file.write_bytes(b"dummy gf")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "gftype", stderr="Error processing GF")
        with pytest.raises(RuntimeError) as excinfo:
            gftype_wrapper.convert(str(gf_file), str(output_file))
        assert "GFtype execution failed: Error processing GF" in str(excinfo.value)
