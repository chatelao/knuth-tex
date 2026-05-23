import pytest
import os
import yaml
import logging
from unittest.mock import MagicMock, patch
from pathlib import Path
from verification.harness.runner import load_config, setup_logging, VerificationTestRunner, discover_tests

def test_load_config_success(tmp_path):
    """Test successful loading of a valid YAML configuration file."""
    config_data = {
        'tangle_path': 'path/to/tangle',
        'output_dir': 'verification/results'
    }
    config_file = tmp_path / "config.yaml"
    with open(config_file, 'w') as f:
        yaml.dump(config_data, f)

    loaded_config = load_config(str(config_file))
    assert loaded_config == config_data

def test_load_config_file_not_found():
    """Test load_config with a non-existent file path."""
    with pytest.raises(SystemExit) as e:
        load_config("non_existent_config.yaml")
    assert e.type is SystemExit
    assert e.value.code == 1

def test_load_config_invalid_yaml(tmp_path):
    """Test load_config with an invalid YAML file."""
    config_file = tmp_path / "invalid.yaml"
    with open(config_file, 'w') as f:
        f.write("invalid: yaml: content: : :")

    with pytest.raises(SystemExit) as e:
        load_config(str(config_file))
    assert e.type is SystemExit
    assert e.value.code == 1

def test_setup_logging(tmp_path):
    """Test that setup_logging correctly initializes logging and creates a log file."""
    output_dir = tmp_path / "results"
    setup_logging(str(output_dir))

    log_file = output_dir / "harness.log"
    assert log_file.exists()

    # Check if we can log a message and it appears in the file
    test_message = "Test log message"
    logging.info(test_message)

    with open(log_file, 'r') as f:
        content = f.read()
        assert test_message in content

    # Clean up handlers to avoid interference with other tests
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

def test_discover_tests(tmp_path):
    """Test discovery of test_config.yaml files."""
    test1_dir = tmp_path / "test1"
    test1_dir.mkdir()
    (test1_dir / "test_config.yaml").write_text("id: 1")

    test2_dir = tmp_path / "subdir" / "test2"
    test2_dir.mkdir(parents=True)
    (test2_dir / "test_config.yaml").write_text("id: 2")

    (tmp_path / "not_a_test").mkdir()
    (tmp_path / "not_a_test" / "random.txt").write_text("hello")

    configs = discover_tests(str(tmp_path))
    assert len(configs) == 2
    assert any("test1" in str(c) for c in configs)
    assert any("test2" in str(c) for c in configs)

def test_verification_test_runner_init(tmp_path):
    """Test VerificationTestRunner initialization and config loading."""
    harness_config = {'output_dir': str(tmp_path / "results")}
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web")

    runner = VerificationTestRunner(harness_config, str(test_config_path))
    assert runner.test_id == "TC-001"
    assert runner.test_config['source_web'] == "test.web"
    assert runner.output_dir == Path(harness_config['output_dir']) / "TC-001"
    assert runner.output_dir.exists()

def test_verification_test_runner_run_tangle_success(tmp_path):
    """Test successful Tangle execution via VerificationTestRunner."""
    harness_config = {
        'tangle_path': 'tangle_exe',
        'output_dir': str(tmp_path / "results")
    }
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web\nchange_file: test.ch")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch("verification.harness.runner.TangleWrapper") as MockWrapper:
        mock_instance = MockWrapper.return_value
        mock_instance.run.return_value = ("out.p", "out.pool")

        pascal, pool = runner.run_tangle()

        assert pascal == "out.p"
        assert pool == "out.pool"

        MockWrapper.assert_called_once_with('tangle_exe')
        mock_instance.run.assert_called_once_with(
            web_file="test.web",
            change_file="test.ch",
            pascal_file=str(runner.output_dir / "TC-001.p"),
            pool_file=str(runner.output_dir / "TC-001.pool")
        )

def test_verification_test_runner_run_tangle_missing_config(tmp_path):
    """Test VerificationTestRunner.run_tangle with missing configuration."""
    harness_config = {'output_dir': str(tmp_path / "results")} # Missing tangle_path
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web")

    runner = VerificationTestRunner(harness_config, str(test_config_path))
    with pytest.raises(ValueError, match="tangle_path not specified"):
        runner.run_tangle()

def test_verification_test_runner_run_compile_success(tmp_path):
    """Test successful compilation execution via VerificationTestRunner."""
    harness_config = {
        'pascal_compiler': 'pc_exe',
        'output_dir': str(tmp_path / "results")
    }
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch("verification.harness.runner.CompileWrapper") as MockWrapper:
        mock_instance = MockWrapper.return_value
        mock_instance.run.return_value = "out_exe"

        exe = runner.run_compile("test.p")

        assert exe == "out_exe"

        MockWrapper.assert_called_once_with('pc_exe')
        mock_instance.run.assert_called_once_with(
            pascal_file="test.p",
            output_exe=str(runner.output_dir / "TC-001")
        )

def test_verification_test_runner_run_compile_missing_config(tmp_path):
    """Test VerificationTestRunner.run_compile with missing configuration."""
    harness_config = {'output_dir': str(tmp_path / "results")} # Missing pascal_compiler
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web")

    runner = VerificationTestRunner(harness_config, str(test_config_path))
    with pytest.raises(ValueError, match="pascal_compiler not specified"):
        runner.run_compile("test.p")

def test_verification_test_runner_run_execute_success(tmp_path):
    """Test successful execution via VerificationTestRunner."""
    harness_config = {'output_dir': str(tmp_path / "results")}
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web\ntest_args: ['-a', '-b']\ntest_input_data: 'hello'")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch("verification.harness.runner.ExecuteWrapper") as MockWrapper:
        mock_instance = MockWrapper.return_value
        mock_instance.run.return_value = MagicMock(returncode=0)

        result = runner.run_execute("myexe")

        assert result.returncode == 0
        MockWrapper.assert_called_once_with('myexe')
        mock_instance.run.assert_called_once_with(
            args=['-a', '-b'],
            input_data='hello',
            cwd=str(runner.output_dir)
        )

def test_verification_test_runner_run_execute_with_input_file(tmp_path):
    """Test run_execute with input from a file."""
    harness_config = {'output_dir': str(tmp_path / "results")}
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    input_file = test_dir / "input.txt"
    input_file.write_text("file content")

    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text(f"test_id: TC-001\nsource_web: test.web\ntest_input: {input_file}")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch("verification.harness.runner.ExecuteWrapper") as MockWrapper:
        mock_instance = MockWrapper.return_value
        mock_instance.run.return_value = MagicMock(returncode=0)

        runner.run_execute("myexe")

        mock_instance.run.assert_called_once_with(
            args=[],
            input_data='file content',
            cwd=str(runner.output_dir)
        )

def test_verification_test_runner_run_compare_success(tmp_path):
    """Test successful comparison via VerificationTestRunner."""
    harness_config = {
        'output_dir': str(tmp_path / "results"),
        'dvitype_path': 'dvitype_exe'
    }
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()

    # Create dummy expected files
    exp_log = test_dir / "expected.log"
    exp_log.write_text("log content")
    exp_dvi = test_dir / "expected.dvi"
    exp_dvi.write_text("dvi binary")

    test_config_path = test_dir / "test_config.yaml"
    test_config_data = {
        'test_id': 'TC-001',
        'source_web': 'test.web',
        'expected_outputs': {
            'log': str(exp_log),
            'dvi': str(exp_dvi),
            'terminal': 'dummy' # type only matters for logic
        }
    }
    with open(test_config_path, 'w') as f:
        yaml.dump(test_config_data, f)

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    # Mock execution result
    exe_result = MagicMock(stdout="stdout content", stderr="stderr content")

    with patch.object(runner.comparer, 'compare_text_files') as mock_text_comp, \
         patch.object(runner.comparer, 'compare_binary_files') as mock_bin_comp:

        mock_text_comp.return_value = (True, "")
        mock_bin_comp.return_value = (True, "")

        assert runner.run_compare(exe_result) is True

        # Check terminal output capture
        term_out = runner.output_dir / "terminal.out"
        assert term_out.exists()
        assert term_out.read_text() == "stdout contentstderr content"

        # Check text comparison calls (log and terminal)
        assert mock_text_comp.call_count == 2

        # Log comparison
        args, kwargs = mock_text_comp.call_args_list[0]
        assert args[0] == str(exp_log)
        assert args[1] == runner.output_dir / "expected.log"
        assert kwargs['normalizer'] == runner.normalizer

        # Terminal comparison
        args, kwargs = mock_text_comp.call_args_list[1]
        assert args[0] == 'dummy'
        assert args[1] == runner.output_dir / "terminal.out"
        assert kwargs['normalizer'] == runner.normalizer

        # Check binary comparison call (dvi)
        mock_bin_comp.assert_called_once()
        args, kwargs = mock_bin_comp.call_args
        assert args[0] == str(exp_dvi)
        assert args[1] == runner.output_dir / "expected.dvi"
        assert args[2] == runner.symbolic_comparators['dvi']
        assert kwargs['normalizer'] == runner.normalizer

def test_verification_test_runner_run_compare_failure(tmp_path):
    """Test comparison failure via VerificationTestRunner."""
    harness_config = {'output_dir': str(tmp_path / "results")}
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    exp_log = test_dir / "expected.log"
    exp_log.write_text("expected")

    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text(f"test_id: TC-001\nsource_web: test.web\nexpected_outputs:\n  log: {exp_log}")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch.object(runner.comparer, 'compare_text_files') as mock_text_comp:
        mock_text_comp.return_value = (False, "diff here")

        assert runner.run_compare(MagicMock()) is False

def test_verification_test_runner_full_run_success(tmp_path):
    """Test full workflow success."""
    harness_config = {
        'tangle_path': 'tangle',
        'pascal_compiler': 'pc',
        'output_dir': str(tmp_path / "results")
    }
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch.object(runner, 'run_tangle') as mock_tangle, \
         patch.object(runner, 'run_compile') as mock_compile, \
         patch.object(runner, 'run_execute') as mock_execute, \
         patch.object(runner, 'run_compare') as mock_compare:

        mock_tangle.return_value = ("test.p", "test.pool")
        mock_compile.return_value = "test_exe"
        mock_execute.return_value = MagicMock(returncode=0)
        mock_compare.return_value = True

        assert runner.run() is True

        mock_tangle.assert_called_once()
        mock_compile.assert_called_once_with("test.p")
        mock_execute.assert_called_once_with("test_exe")
        mock_compare.assert_called_once()

def test_verification_test_runner_multi_stage_success(tmp_path):
    """Test full workflow with multiple stages."""
    harness_config = {
        'tangle_path': 'tangle',
        'pascal_compiler': 'pc',
        'output_dir': str(tmp_path / "results")
    }
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_data = {
        'test_id': 'TC-001',
        'source_web': 'test.web',
        'stages': [
            {'id': 's1', 'test_input_data': 'in1', 'expected_outputs': {'log': 'exp1'}},
            {'id': 's2', 'test_input_data': 'in2', 'expected_outputs': {'log': 'exp2'}}
        ]
    }
    with open(test_config_path, 'w') as f:
        yaml.dump(test_config_data, f)

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    with patch.object(runner, 'run_tangle') as mock_tangle, \
         patch.object(runner, 'run_compile') as mock_compile, \
         patch.object(runner, 'run_execute') as mock_execute, \
         patch.object(runner, 'run_compare') as mock_compare:

        mock_tangle.return_value = ("test.p", "test.pool")
        mock_compile.return_value = "test_exe"
        mock_execute.return_value = MagicMock(returncode=0)
        mock_compare.return_value = True

        assert runner.run() is True

        assert mock_tangle.call_count == 1
        assert mock_compile.call_count == 1
        assert mock_execute.call_count == 2
        assert mock_compare.call_count == 2

        # Check stage-specific calls
        mock_execute.assert_any_call("test_exe", stage_config=test_config_data['stages'][0])
        mock_execute.assert_any_call("test_exe", stage_config=test_config_data['stages'][1])
