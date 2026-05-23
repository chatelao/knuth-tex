import difflib
import re
from pathlib import Path

class Comparer:
    """Utility for comparing outputs and determining pass/fail."""

    def __init__(self):
        # Regex for floating point numbers
        self.num_regex = re.compile(r"([-+]?\d*\.\d+|[-+]?\d+\.\d*|[-+]?\d+)")

    def _is_numeric_match(self, line1, line2, tolerance):
        """Checks if two lines match, allowing for numeric tolerance."""
        if line1 == line2:
            return True

        nums1 = self.num_regex.findall(line1)
        nums2 = self.num_regex.findall(line2)

        if len(nums1) != len(nums2):
            return False

        # Check if non-numeric parts match
        text1 = self.num_regex.sub("##", line1)
        text2 = self.num_regex.sub("##", line2)

        if text1 != text2:
            return False

        # Check if numbers are within tolerance
        for n1, n2 in zip(nums1, nums2):
            try:
                if abs(float(n1) - float(n2)) > tolerance:
                    return False
            except ValueError:
                if n1 != n2:
                    return False
        return True

    def compare_text_files(self, expected_path, actual_path, normalizer=None, tolerance=None):
        """
        Compares two text files and returns whether they match and a diff if they don't.

        :param expected_path: Path to the expected output file.
        :param actual_path: Path to the actual output file.
        :param normalizer: Optional Normalizer instance to mask variable data.
        :param tolerance: Optional floating-point tolerance for numeric values.
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

        exp_lines = expected_content.splitlines(keepends=True)
        act_lines = actual_content.splitlines(keepends=True)

        # Quick check for exact match
        if exp_lines == act_lines:
            return True, ""

        # If tolerance is specified, we check if they match with tolerance.
        # To generate a clean diff, we "align" act_lines to exp_lines where they match with tolerance.
        if tolerance is not None and len(exp_lines) == len(act_lines):
            matched_all = True
            aligned_act_lines = []
            for el, al in zip(exp_lines, act_lines):
                if self._is_numeric_match(el, al, tolerance):
                    aligned_act_lines.append(el)
                else:
                    matched_all = False
                    aligned_act_lines.append(al)

            if matched_all:
                return True, ""

            act_lines = aligned_act_lines

        # If we are here, there is a mismatch (or files have different lengths)
        diff = difflib.unified_diff(
            exp_lines, act_lines,
            fromfile=str(expected_path),
            tofile=str(actual_path)
        )
        return False, "".join(diff)
