import difflib
from pathlib import Path

class Comparer:
    """Utility for comparing outputs and determining pass/fail."""

    def compare_text_files(self, expected_path, actual_path, normalizer=None):
        """
        Compares two text files and returns whether they match and a diff if they don't.

        :param expected_path: Path to the expected output file.
        :param actual_path: Path to the actual output file.
        :param normalizer: Optional Normalizer instance to mask variable data.
        :return: (bool, str) - (True if match, "" if match else diff string)
        """
        expected_path = Path(expected_path)
        actual_path = Path(actual_path)

        if not expected_path.exists():
            return False, f"Expected file not found: {expected_path}"
        if not actual_path.exists():
            return False, f"Actual file not found: {actual_path}"

        with open(expected_path, 'r', errors='replace') as f_exp:
            expected_content = f_exp.read()

        with open(actual_path, 'r', errors='replace') as f_act:
            actual_content = f_act.read()

        if normalizer:
            expected_content = normalizer.normalize_content(expected_content)
            actual_content = normalizer.normalize_content(actual_content)

        if expected_content == actual_content:
            return True, ""
        else:
            exp_lines = expected_content.splitlines(keepends=True)
            act_lines = actual_content.splitlines(keepends=True)

            diff = difflib.unified_diff(
                exp_lines, act_lines,
                fromfile=str(expected_path),
                tofile=str(actual_path)
            )
            return False, "".join(diff)
