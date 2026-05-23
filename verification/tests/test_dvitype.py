import pytest
import subprocess
import os
from pathlib import Path
from unittest.mock import MagicMock, patch
from verification.harness.dvitype import DVItypeWrapper

@pytest.fixture
def dvitype_wrapper():
    return DVItypeWrapper("dvitype")

def test_dvitype_convert_stdout(dvitype_wrapper, tmp_path):
    # Setup mock files
    dvi_file = tmp_path / "test.dvi"
    dvi_file.write_bytes(b"dummy dvi")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        # Mocking DVItype writing to stdout (no dvitype.out created)
        mock_run.return_value = MagicMock(returncode=0, stdout="Symbolic DVI output", stderr="")

        dvitype_wrapper.convert(str(dvi_file), str(output_file))

        assert output_file.exists()
        assert output_file.read_text() == "Symbolic DVI output"

def test_dvitype_convert_hardcoded_file(dvitype_wrapper, tmp_path):
    # Setup mock files
    dvi_file = tmp_path / "test.dvi"
    dvi_file.write_bytes(b"dummy dvi")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        def side_effect(*args, **kwargs):
            # Simulate DVItype creating dvitype.out in its cwd
            cwd = kwargs.get('cwd')
            (Path(cwd) / "dvitype.out").write_text("Hardcoded file content")
            return MagicMock(returncode=0, stdout="", stderr="")

        mock_run.side_effect = side_effect

        dvitype_wrapper.convert(str(dvi_file), str(output_file))

        assert output_file.exists()
        assert output_file.read_text() == "Hardcoded file content"

def test_dvitype_file_not_found(dvitype_wrapper):
    with pytest.raises(FileNotFoundError):
        dvitype_wrapper.convert("non_existent.dvi", "out.typ")

def test_dvitype_execution_failure(dvitype_wrapper, tmp_path):
    dvi_file = tmp_path / "test.dvi"
    dvi_file.write_bytes(b"dummy dvi")
    output_file = tmp_path / "test.typ"

    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "dvitype", stderr="Error processing DVI")

        with pytest.raises(RuntimeError) as excinfo:
            dvitype_wrapper.convert(str(dvi_file), str(output_file))

        assert "DVItype execution failed: Error processing DVI" in str(excinfo.value)

def test_dvitype_callable_interface(dvitype_wrapper, tmp_path):
    dvi_file = tmp_path / "test.dvi"
    dvi_file.write_bytes(b"dummy dvi")
    output_file = tmp_path / "test.typ"

    with patch.object(DVItypeWrapper, 'convert') as mock_convert:
        dvitype_wrapper(str(dvi_file), str(output_file))
        mock_convert.assert_called_once_with(str(dvi_file), str(output_file))
