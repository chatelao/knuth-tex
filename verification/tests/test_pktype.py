import pytest
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch
from verification.harness.pktype import PKtypeWrapper

@pytest.fixture
def pktype_wrapper():
    return PKtypeWrapper("pktype")

def test_pktype_convert_stdout(pktype_wrapper, tmp_path):
    pk_file = tmp_path / "test.pk"
    pk_file.write_bytes(b"dummy pk")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="Symbolic PK output", stderr="")
        pktype_wrapper.convert(str(pk_file), str(output_file))
        assert output_file.exists()
        assert output_file.read_text() == "Symbolic PK output"

def test_pktype_convert_hardcoded_file(pktype_wrapper, tmp_path):
    pk_file = tmp_path / "test.pk"
    pk_file.write_bytes(b"dummy pk")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        def side_effect(*args, **kwargs):
            cwd = kwargs.get('cwd')
            (Path(cwd) / "pktype.out").write_text("Hardcoded PK file content")
            return MagicMock(returncode=0, stdout="", stderr="")
        mock_run.side_effect = side_effect

        pktype_wrapper.convert(str(pk_file), str(output_file))
        assert output_file.exists()
        assert output_file.read_text() == "Hardcoded PK file content"

def test_pktype_file_not_found(pktype_wrapper):
    with pytest.raises(FileNotFoundError):
        pktype_wrapper.convert("non_existent.pk", "out.typ")

def test_pktype_execution_failure(pktype_wrapper, tmp_path):
    pk_file = tmp_path / "test.pk"
    pk_file.write_bytes(b"dummy pk")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "pktype", stderr="Error processing PK")
        with pytest.raises(RuntimeError) as excinfo:
            pktype_wrapper.convert(str(pk_file), str(output_file))
        assert "PKtype execution failed: Error processing PK" in str(excinfo.value)
