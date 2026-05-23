import subprocess
import logging
from pathlib import Path

class TFtoPLWrapper:
    """Wrapper for the TFtoPL utility."""

    def __init__(self, tftopl_exe):
        """
        Initialize the TFtoPLWrapper.

        :param tftopl_exe: Path to the TFtoPL executable.
        """
        self.tftopl_exe = tftopl_exe

    def convert(self, tfm_path, pl_path):
        """
        Converts a TFM file to PL format.

        :param tfm_path: Path to the input .tfm file.
        :param pl_path: Path where the .pl output should be saved.
        """
        tfm_path = Path(tfm_path).resolve()
        pl_path = Path(pl_path).resolve()

        if not tfm_path.exists():
            raise FileNotFoundError(f"TFM file not found: {tfm_path}")

        # Ensure the output directory exists
        pl_path.parent.mkdir(parents=True, exist_ok=True)

        # TFtoPL typically accepts two positional arguments: tfm_file and pl_file
        cmd = [str(self.tftopl_exe), str(tfm_path), str(pl_path)]

        logging.info(f"Running TFtoPL: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            logging.info(f"TFtoPL conversion completed: {pl_path}")

        except subprocess.CalledProcessError as e:
            logging.error(f"TFtoPL failed with exit code {e.returncode}")
            logging.error(f"TFtoPL stderr: {e.stderr}")
            raise RuntimeError(f"TFtoPL execution failed: {e.stderr}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during TFtoPL execution: {e}")
            raise

    def __call__(self, binary_path, text_output_path):
        """Callable interface for use with Comparer.compare_binary_files."""
        self.convert(binary_path, text_output_path)
