import pytest
import subprocess
import os
from unittest.mock import MagicMock, patch
from verification.harness.executor import ExecuteWrapper

@pytest.fixture
def execute_wrapper(tmp_path):
    exe_path = tmp_path / "mock_exe"
    exe_path.touch()
    return ExecuteWrapper(str(exe_path))

def test_execute_run_success(execute_wrapper):
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="success", stderr="")

        result = execute_wrapper.run(args=["--version"], input_data="test input")

        assert result.returncode == 0
        assert result.stdout == "success"
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        assert args[0] == [execute_wrapper.executable_path, "--version"]
        assert kwargs["input"] == "test input"
        assert kwargs["capture_output"] is True
        assert kwargs["text"] is True

def test_execute_run_with_cwd_and_env(execute_wrapper, tmp_path):
    custom_cwd = tmp_path / "workdir"
    custom_env = {"VAR": "VALUE"}

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)

        execute_wrapper.run(cwd=str(custom_cwd), env=custom_env)

        assert os.path.exists(custom_cwd)
        mock_run.assert_called_once()
        _, kwargs = mock_run.call_args
        assert kwargs["cwd"] == str(custom_cwd)
        assert kwargs["env"] == custom_env

def test_execute_run_failure_exit_code(execute_wrapper):
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="error")

        result = execute_wrapper.run()

        assert result.returncode == 1
        assert result.stderr == "error"

def test_execute_file_not_found():
    wrapper = ExecuteWrapper("non_existent_exe")
    with pytest.raises(FileNotFoundError):
        wrapper.run()

def test_execute_run_runtime_error(execute_wrapper):
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = Exception("Spawn failed")

        with pytest.raises(RuntimeError) as excinfo:
            execute_wrapper.run()

        assert "Execution failed: Spawn failed" in str(excinfo.value)
