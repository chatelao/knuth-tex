import subprocess
import os
import shutil
import logging
from pathlib import Path

class DVItypeWrapper:
    """Wrapper for the DVItype utility."""

    def __init__(self, dvitype_exe):
        """
        Initialize the DVItypeWrapper.

        :param dvitype_exe: Path to the DVItype executable.
        """
        self.dvitype_exe = dvitype_exe

    def convert(self, dvi_path, output_path, dialog_input="\n\n\n\n"):
        """
        Converts a DVI file to symbolic text format.

        :param dvi_path: Path to the input .dvi file.
        :param output_path: Path where the symbolic text output should be saved.
        :param dialog_input: Inputs to be passed to the DVItype dialog (defaults to all defaults).
        """
        dvi_path = Path(dvi_path).resolve()
        output_path = Path(output_path).resolve()

        if not dvi_path.exists():
            raise FileNotFoundError(f"DVI file not found: {dvi_path}")

        # Ensure the output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        cmd = [str(self.dvitype_exe), str(dvi_path)]

        logging.info(f"Running DVItype: {' '.join(cmd)}")

        # DVItype often writes to a hardcoded 'dvitype.out' in the current working directory.
        # To avoid conflicts and ensure we capture the output, we run in a temporary directory
        # or carefully move the result.

        # We will use a temporary directory to run DVItype to avoid polluting the current directory
        # and to handle the hardcoded 'dvitype.out' reliably.
        import tempfile
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

                hardcoded_out = tmp_path / "dvitype.out"
                if hardcoded_out.exists():
                    shutil.move(hardcoded_out, output_path)
                else:
                    # If 'dvitype.out' is not found, it might have written to stdout
                    with open(output_path, "w") as f:
                        f.write(result.stdout)

                logging.info(f"DVItype conversion completed: {output_path}")

            except subprocess.CalledProcessError as e:
                logging.error(f"DVItype failed with exit code {e.returncode}")
                logging.error(f"DVItype stderr: {e.stderr}")
                raise RuntimeError(f"DVItype execution failed: {e.stderr}")
            except Exception as e:
                logging.error(f"An unexpected error occurred during DVItype execution: {e}")
                raise

    def __call__(self, binary_path, text_output_path):
        """Callable interface for use with Comparer.compare_binary_files."""
        self.convert(binary_path, text_output_path)
