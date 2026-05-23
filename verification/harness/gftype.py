import subprocess
import shutil
import logging
import tempfile
from pathlib import Path

class GFtypeWrapper:
    """Wrapper for the GFtype utility."""

    def __init__(self, gftype_exe):
        """
        Initialize the GFtypeWrapper.

        :param gftype_exe: Path to the GFtype executable.
        """
        self.gftype_exe = gftype_exe

    def convert(self, gf_path, output_path, dialog_input="\n\n"):
        """
        Converts a GF file to symbolic text format.

        :param gf_path: Path to the input .gf file.
        :param output_path: Path where the symbolic text output should be saved.
        :param dialog_input: Inputs to be passed to the GFtype dialog.
        """
        gf_path = Path(gf_path).resolve()
        output_path = Path(output_path).resolve()

        if not gf_path.exists():
            raise FileNotFoundError(f"GF file not found: {gf_path}")

        # Ensure the output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        cmd = [str(self.gftype_exe), str(gf_path)]

        logging.info(f"Running GFtype: {' '.join(cmd)}")

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)

            try:
                result = subprocess.run(
                    cmd,
                    input=dialog_input,
                    capture_output=True,
                    text=True,
                    cwd=tmp_path,
                    check=True
                )

                hardcoded_out = tmp_path / "gftype.out"
                if hardcoded_out.exists():
                    shutil.move(hardcoded_out, output_path)
                else:
                    # If 'gftype.out' is not found, it might have written to stdout
                    with open(output_path, "w") as f:
                        f.write(result.stdout)

                logging.info(f"GFtype conversion completed: {output_path}")

            except subprocess.CalledProcessError as e:
                logging.error(f"GFtype failed with exit code {e.returncode}")
                logging.error(f"GFtype stderr: {e.stderr}")
                raise RuntimeError(f"GFtype execution failed: {e.stderr}")
            except Exception as e:
                logging.error(f"An unexpected error occurred during GFtype execution: {e}")
                raise

    def __call__(self, binary_path, text_output_path):
        """Callable interface for use with Comparer.compare_binary_files."""
        self.convert(binary_path, text_output_path)
