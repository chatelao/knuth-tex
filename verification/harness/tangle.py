import subprocess
import os
import logging
from pathlib import Path

class TangleWrapper:
    """Wrapper for the TANGLE processor."""

    def __init__(self, tangle_exe):
        """
        Initialize the TangleWrapper.

        :param tangle_exe: Path to the TANGLE executable.
        """
        self.tangle_exe = tangle_exe

    def run(self, web_file, change_file=None, pascal_file=None, pool_file=None):
        """
        Runs TANGLE to convert a WEB file to a Pascal file and string pool.

        :param web_file: Path to the .web file.
        :param change_file: Path to the .ch file (optional). Defaults to os.devnull.
        :param pascal_file: Path to the output .p file (optional).
        :param pool_file: Path to the output .pool file (optional).
        :return: A tuple of (pascal_file_path, pool_file_path).
        :raises FileNotFoundError: If the WEB file or change file does not exist.
        :raises RuntimeError: If TANGLE execution fails.
        """
        web_path = Path(web_file)
        if not web_path.exists():
            raise FileNotFoundError(f"WEB file not found: {web_file}")

        if change_file is None:
            change_file = os.devnull

        if not os.path.exists(change_file):
             raise FileNotFoundError(f"Change file not found: {change_file}")

        # Infer output filenames if not provided
        # In a real scenario, these might be directed to a results directory.
        if pascal_file is None:
            pascal_file = str(web_path.with_suffix('.p'))
        if pool_file is None:
            pool_file = str(web_path.with_suffix('.pool'))

        cmd = [
            self.tangle_exe,
            str(web_file),
            str(change_file),
            str(pascal_file),
            str(pool_file)
        ]

        logging.info(f"Running TANGLE: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            logging.info("TANGLE completed successfully.")
            return pascal_file, pool_file
        except subprocess.CalledProcessError as e:
            logging.error(f"TANGLE failed with exit code {e.returncode}")
            logging.error(f"TANGLE stderr: {e.stderr}")
            raise RuntimeError(f"TANGLE execution failed: {e.stderr}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during TANGLE execution: {e}")
            raise
