import pytest
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch
from verification.harness.dvitype import DVItypeWrapper
from verification.harness.gftype import GFtypeWrapper
from verification.harness.pktype import PKtypeWrapper
from verification.harness.tftopl import TFtoPLWrapper

@pytest.fixture
def temp_io(tmp_path):
    input_file = tmp_path / "input.bin"
    input_file.write_text("dummy binary content")
    output_file = tmp_path / "output.txt"
    return input_file, output_file

class TestDVItypeWrapper:
    def test_run_success_stdout(self, temp_io):
        input_file, output_file = temp_io
        wrapper = DVItypeWrapper("dvitype")

        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="symbolic content", stderr="")

            wrapper.convert(input_file, output_file)

            assert output_file.read_text() == "symbolic content"
            mock_run.assert_called_once()
            args, kwargs = mock_run.call_args
            assert args[0] == ["dvitype", str(input_file.resolve())]
            assert kwargs["input"] == "\n\n\n\n"

    def test_run_success_hardcoded_file(self, temp_io, tmp_path):
        input_file, output_file = temp_io
        wrapper = DVItypeWrapper("dvitype")

        with patch("subprocess.run") as mock_run:
            def side_effect(*args, **kwargs):
                cwd = kwargs.get("cwd")
                if cwd:
                    (Path(cwd) / "dvitype.out").write_text("file content")
                return MagicMock(returncode=0, stdout="", stderr="")

            mock_run.side_effect = side_effect

            wrapper.convert(input_file, output_file)

            assert output_file.read_text() == "file content"

    def test_file_not_found(self, tmp_path):
        wrapper = DVItypeWrapper("dvitype")
        with pytest.raises(FileNotFoundError):
            wrapper.convert(tmp_path / "non_existent.dvi", tmp_path / "out.txt")

    def test_run_failure(self, temp_io):
        input_file, output_file = temp_io
        wrapper = DVItypeWrapper("dvitype")

        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, "dvitype", stderr="Some error")

            with pytest.raises(RuntimeError) as excinfo:
                wrapper.convert(input_file, output_file)
            assert "DVItype execution failed: Some error" in str(excinfo.value)

    def test_call_interface(self, temp_io):
        input_file, output_file = temp_io
        wrapper = DVItypeWrapper("dvitype")
        with patch.object(DVItypeWrapper, 'convert') as mock_convert:
            wrapper(input_file, output_file)
            mock_convert.assert_called_once_with(input_file, output_file)

class TestGFtypeWrapper:
    def test_run_success_stdout(self, temp_io):
        input_file, output_file = temp_io
        wrapper = GFtypeWrapper("gftype")

        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="gf symbolic", stderr="")

            wrapper.convert(input_file, output_file)

            assert output_file.read_text() == "gf symbolic"
            mock_run.assert_called_once()
            args, kwargs = mock_run.call_args
            assert args[0] == ["gftype", str(input_file.resolve())]

    def test_run_success_hardcoded_file(self, temp_io):
        input_file, output_file = temp_io
        wrapper = GFtypeWrapper("gftype")

        with patch("subprocess.run") as mock_run:
            def side_effect(*args, **kwargs):
                cwd = kwargs.get("cwd")
                if cwd:
                    (Path(cwd) / "gftype.out").write_text("gf file content")
                return MagicMock(returncode=0, stdout="", stderr="")

            mock_run.side_effect = side_effect

            wrapper.convert(input_file, output_file)

            assert output_file.read_text() == "gf file content"

    def test_run_failure(self, temp_io):
        input_file, output_file = temp_io
        wrapper = GFtypeWrapper("gftype")

        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, "gftype", stderr="GF error")

            with pytest.raises(RuntimeError) as excinfo:
                wrapper.convert(input_file, output_file)
            assert "GFtype execution failed: GF error" in str(excinfo.value)

class TestPKtypeWrapper:
    def test_run_success_stdout(self, temp_io):
        input_file, output_file = temp_io
        wrapper = PKtypeWrapper("pktype")

        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="pk symbolic", stderr="")

            wrapper.convert(input_file, output_file)

            assert output_file.read_text() == "pk symbolic"

    def test_run_success_hardcoded_file(self, temp_io):
        input_file, output_file = temp_io
        wrapper = PKtypeWrapper("pktype")

        with patch("subprocess.run") as mock_run:
            def side_effect(*args, **kwargs):
                cwd = kwargs.get("cwd")
                if cwd:
                    (Path(cwd) / "pktype.out").write_text("pk file content")
                return MagicMock(returncode=0, stdout="", stderr="")

            mock_run.side_effect = side_effect

            wrapper.convert(input_file, output_file)

            assert output_file.read_text() == "pk file content"

class TestTFtoPLWrapper:
    def test_run_success(self, temp_io):
        input_file, output_file = temp_io
        wrapper = TFtoPLWrapper("tftopl")

        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

            wrapper.convert(input_file, output_file)

            mock_run.assert_called_once_with(
                ["tftopl", str(input_file.resolve()), str(output_file.resolve())],
                capture_output=True,
                text=True,
                check=True
            )

    def test_run_failure(self, temp_io):
        input_file, output_file = temp_io
        wrapper = TFtoPLWrapper("tftopl")

        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, "tftopl", stderr="TFM error")

            with pytest.raises(RuntimeError) as excinfo:
                wrapper.convert(input_file, output_file)
            assert "TFtoPL execution failed: TFM error" in str(excinfo.value)
