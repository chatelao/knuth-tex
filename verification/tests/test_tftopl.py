import pytest
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch
from verification.harness.tftopl import TFtoPLWrapper

@pytest.fixture
def tftopl_wrapper():
    return TFtoPLWrapper("tftopl")

def test_tftopl_convert(tftopl_wrapper, tmp_path):
    tfm_file = tmp_path / "test.tfm"
    tfm_file.write_bytes(b"dummy tfm")
    output_file = tmp_path / "test.pl"

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        tftopl_wrapper.convert(str(tfm_file), str(output_file))

        # Verify call arguments
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        cmd = args[0]
        assert cmd[0] == "tftopl"
        assert cmd[1] == str(tfm_file.resolve())
        assert cmd[2] == str(output_file.resolve())

def test_tftopl_file_not_found(tftopl_wrapper):
    with pytest.raises(FileNotFoundError):
        tftopl_wrapper.convert("non_existent.tfm", "out.pl")

def test_tftopl_execution_failure(tftopl_wrapper, tmp_path):
    tfm_file = tmp_path / "test.tfm"
    tfm_file.write_bytes(b"dummy tfm")
    output_file = tmp_path / "test.pl"

    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "tftopl", stderr="Error processing TFM")
        with pytest.raises(RuntimeError) as excinfo:
            tftopl_wrapper.convert(str(tfm_file), str(output_file))
        assert "TFtoPL execution failed: Error processing TFM" in str(excinfo.value)
