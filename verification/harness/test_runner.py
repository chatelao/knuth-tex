import pytest
import os
import yaml
import logging
from verification.harness.runner import load_config, setup_logging

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
