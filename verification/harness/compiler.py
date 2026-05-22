import subprocess
import os
import logging
from pathlib import Path

class CompileWrapper:
    """Wrapper for the Pascal compiler."""

    def __init__(self, compiler_exe):
        """
        Initialize the CompileWrapper.

        :param compiler_exe: Path to the Pascal compiler executable (e.g., 'gpc', 'fpc', 'pc').
        """
        self.compiler_exe = compiler_exe

    def run(self, pascal_file, output_exe=None, options=None):
        """
        Compiles a Pascal file into an executable.

        :param pascal_file: Path to the .p file.
        :param output_exe: Path to the output executable (optional).
        :param options: List of additional compiler options (optional).
        :return: Path to the generated executable.
        :raises FileNotFoundError: If the Pascal file does not exist.
        :raises RuntimeError: If compilation fails.
        """
        pascal_path = Path(pascal_file)
        if not pascal_path.exists():
            raise FileNotFoundError(f"Pascal file not found: {pascal_file}")

        if output_exe is None:
            # Default to the same name as the Pascal file without the extension
            output_exe = str(pascal_path.with_suffix(''))

        cmd = [self.compiler_exe]

        if options:
            cmd.extend(options)

        cmd.extend(["-o", str(output_exe), str(pascal_file)])

        logging.info(f"Running Pascal compiler: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            logging.info("Compilation completed successfully.")
            return output_exe
        except subprocess.CalledProcessError as e:
            logging.error(f"Compilation failed with exit code {e.returncode}")
            logging.error(f"Compiler stderr: {e.stderr}")
            raise RuntimeError(f"Compilation failed: {e.stderr}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during compilation: {e}")
            raise
