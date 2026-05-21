import pytest
import os
import yaml
from verification.harness.runner import load_config

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
