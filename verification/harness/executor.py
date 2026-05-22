import subprocess
import logging
import os

class ExecuteWrapper:
    """Wrapper for executing the compiled TeX/Metafont programs."""

    def __init__(self, executable_path):
        """
        Initialize the ExecuteWrapper.

        :param executable_path: Path to the executable to run.
        """
        self.executable_path = executable_path

    def run(self, args=None, input_data=None, cwd=None, env=None):
        """
        Executes the program with the specified arguments and environment.

        :param args: List of command-line arguments.
        :param input_data: String to be passed to the program's stdin.
        :param cwd: Working directory for the execution.
        :param env: Dictionary of environment variables.
        :return: A subprocess.CompletedProcess instance.
        :raises FileNotFoundError: If the executable does not exist.
        :raises RuntimeError: If the execution fails to start.
        """
        if not os.path.exists(self.executable_path):
            raise FileNotFoundError(f"Executable not found: {self.executable_path}")

        cmd = [str(self.executable_path)]
        if args:
            cmd.extend([str(a) for a in args])

        if cwd:
            os.makedirs(cwd, exist_ok=True)
            logging.info(f"Using working directory: {cwd}")

        logging.info(f"Executing command: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                input=input_data,
                capture_output=True,
                text=True,
                cwd=cwd,
                env=env,
                check=False # We return the result and let the caller decide
            )

            if result.returncode == 0:
                logging.info(f"Execution completed successfully (exit code 0).")
            else:
                logging.warning(f"Execution finished with exit code {result.returncode}.")

            return result

        except Exception as e:
            logging.error(f"Failed to execute {self.executable_path}: {e}")
            raise RuntimeError(f"Execution failed: {e}")
