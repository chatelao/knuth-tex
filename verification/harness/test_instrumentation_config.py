import pytest
from unittest.mock import patch, mock_open
from pathlib import Path
from verification.harness.runner import VerificationTestRunner

def test_run_instrumentation_with_include_routines(tmp_path):
    """Test run_instrumentation passes include_routines to Instrumenter."""
    harness_config = {
        'output_dir': str(tmp_path / "results"),
        'mcdc_include_routines': ['routine1', 'routine2']
    }
    test_dir = tmp_path / "mytest"
    test_dir.mkdir()
    test_config_path = test_dir / "test_config.yaml"
    test_config_path.write_text("test_id: TC-001\nsource_web: test.web")

    runner = VerificationTestRunner(harness_config, str(test_config_path))

    pascal_file = tmp_path / "test.p"
    pascal_file.write_text("PROGRAM test; BEGIN END.")

    with patch("verification.harness.runner.Lexer") as MockLexer, \
         patch("verification.harness.runner.Parser") as MockParser, \
         patch("verification.harness.runner.Instrumenter") as MockInstrumenter, \
         patch("verification.harness.runner.PascalEmitter") as MockEmitter:

        mock_inst_instance = MockInstrumenter.return_value
        mock_inst_instance.instrument.return_value = "instrumented_ast"
        mock_inst_instance.decisions = {}

        mock_emitter_instance = MockEmitter.return_value
        mock_emitter_instance.emit.return_value = "BEGIN END"

        runner.run_instrumentation(str(pascal_file))

        MockInstrumenter.assert_called_once_with(include_routines=['routine1', 'routine2'])
        mock_inst_instance.instrument.assert_called_once()
