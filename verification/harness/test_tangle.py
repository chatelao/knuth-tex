import pytest
import subprocess
import os
from unittest.mock import MagicMock, patch
from verification.harness.tangle import TangleWrapper

@pytest.fixture
def tangle_wrapper():
    return TangleWrapper("tangle")

def test_tangle_run_success(tangle_wrapper, tmp_path):
    # Setup mock files
    web_file = tmp_path / "test.web"
    web_file.write_text("@* Hello World.")

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

        pascal, pool = tangle_wrapper.run(str(web_file))

        assert pascal == str(web_file.with_suffix('.p'))
        assert pool == str(web_file.with_suffix('.pool'))

        mock_run.assert_called_once_with(
            ["tangle", str(web_file), os.devnull, pascal, pool],
            capture_output=True,
            text=True,
            check=True
        )

def test_tangle_run_with_change_file(tangle_wrapper, tmp_path):
    web_file = tmp_path / "test.web"
    web_file.write_text("@* Hello.")
    change_file = tmp_path / "test.ch"
    change_file.write_text("@x Change.")

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

        pascal, pool = tangle_wrapper.run(str(web_file), change_file=str(change_file))

        mock_run.assert_called_once_with(
            ["tangle", str(web_file), str(change_file), pascal, pool],
            capture_output=True,
            text=True,
            check=True
        )

def test_tangle_file_not_found(tangle_wrapper):
    with pytest.raises(FileNotFoundError):
        tangle_wrapper.run("non_existent.web")

def test_tangle_run_failure(tangle_wrapper, tmp_path):
    web_file = tmp_path / "test.web"
    web_file.write_text("@* Hello.")

    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "tangle", stderr="Syntax error")

        with pytest.raises(RuntimeError) as excinfo:
            tangle_wrapper.run(str(web_file))

        assert "TANGLE execution failed: Syntax error" in str(excinfo.value)
