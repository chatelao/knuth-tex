import subprocess
import shutil
import logging
import tempfile
from pathlib import Path

class PKtypeWrapper:
    """Wrapper for the PKtype utility."""

    def __init__(self, pktype_exe):
        """
        Initialize the PKtypeWrapper.

        :param pktype_exe: Path to the PKtype executable.
        """
        self.pktype_exe = pktype_exe

    def convert(self, pk_path, output_path):
        """
        Converts a PK file to symbolic text format.

        :param pk_path: Path to the input .pk file.
        :param output_path: Path where the symbolic text output should be saved.
        """
        pk_path = Path(pk_path).resolve()
        output_path = Path(output_path).resolve()

        if not pk_path.exists():
            raise FileNotFoundError(f"PK file not found: {pk_path}")

        # Ensure the output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        cmd = [str(self.pktype_exe), str(pk_path)]

        logging.info(f"Running PKtype: {' '.join(cmd)}")

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)

            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    cwd=tmp_path,
                    check=True
                )

                hardcoded_out = tmp_path / "pktype.out"
                if hardcoded_out.exists():
                    shutil.move(hardcoded_out, output_path)
                else:
                    # If 'pktype.out' is not found, it might have written to stdout
                    with open(output_path, "w") as f:
                        f.write(result.stdout)

                logging.info(f"PKtype conversion completed: {output_path}")

            except subprocess.CalledProcessError as e:
                logging.error(f"PKtype failed with exit code {e.returncode}")
                logging.error(f"PKtype stderr: {e.stderr}")
                raise RuntimeError(f"PKtype execution failed: {e.stderr}")
            except Exception as e:
                logging.error(f"An unexpected error occurred during PKtype execution: {e}")
                raise

    def __call__(self, binary_path, text_output_path):
        """Callable interface for use with Comparer.compare_binary_files."""
        self.convert(binary_path, text_output_path)
