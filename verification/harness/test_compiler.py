import pytest
import subprocess
import os
from unittest.mock import MagicMock, patch
from verification.harness.compiler import CompileWrapper

@pytest.fixture
def compile_wrapper():
    return CompileWrapper("gpc")

def test_compile_run_success(compile_wrapper, tmp_path):
    # Setup mock file
    pascal_file = tmp_path / "test.p"
    pascal_file.write_text("program test; begin end.")

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

        output_exe = compile_wrapper.run(str(pascal_file))

        expected_exe = str(pascal_file.with_suffix(''))
        assert output_exe == expected_exe

        mock_run.assert_called_once_with(
            ["gpc", "-o", expected_exe, str(pascal_file)],
            capture_output=True,
            text=True,
            check=True
        )

def test_compile_run_with_options(compile_wrapper, tmp_path):
    pascal_file = tmp_path / "test.p"
    pascal_file.write_text("program test; begin end.")
    options = ["-O2", "-Wall"]

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

        output_exe = compile_wrapper.run(str(pascal_file), options=options)

        expected_exe = str(pascal_file.with_suffix(''))
        mock_run.assert_called_once_with(
            ["gpc", "-O2", "-Wall", "-o", expected_exe, str(pascal_file)],
            capture_output=True,
            text=True,
            check=True
        )

def test_compile_run_with_custom_output(compile_wrapper, tmp_path):
    pascal_file = tmp_path / "test.p"
    pascal_file.write_text("program test; begin end.")
    custom_exe = str(tmp_path / "my_program")

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

        output_exe = compile_wrapper.run(str(pascal_file), output_exe=custom_exe)

        assert output_exe == custom_exe
        mock_run.assert_called_once_with(
            ["gpc", "-o", custom_exe, str(pascal_file)],
            capture_output=True,
            text=True,
            check=True
        )

def test_compile_file_not_found(compile_wrapper):
    with pytest.raises(FileNotFoundError):
        compile_wrapper.run("non_existent.p")

def test_compile_run_failure(compile_wrapper, tmp_path):
    pascal_file = tmp_path / "test.p"
    pascal_file.write_text("program test; begin end.")

    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "gpc", stderr="Compilation error")

        with pytest.raises(RuntimeError) as excinfo:
            compile_wrapper.run(str(pascal_file))

        assert "Compilation failed: Compilation error" in str(excinfo.value)
