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
