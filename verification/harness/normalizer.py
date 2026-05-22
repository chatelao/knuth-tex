import re
from pathlib import Path

class Normalizer:
    """Utility for normalizing text-based outputs (Log, Terminal) for TeX and Metafont."""

    def __init__(self):
        # Banner pattern: version and date/time
        # Example: This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  4 JUL 1776 12:00
        self.banner_pattern = re.compile(
            r"^(This is (TeX|Metafont), Version [^)]+\)).*$"
        )

        # Generic date pattern often seen in TeX/MF logs
        # Example: 4 JUL 1776 12:00
        self.date_pattern = re.compile(r"\d{1,2} [A-Z]{3} \d{4} \d{2}:\d{2}")

    def normalize_line(self, line):
        """
        Normalizes a single line of text by masking variable information.

        :param line: The input line.
        :return: The normalized line.
        """
        # If it's the banner line, keep only the version part and mask the rest
        match = self.banner_pattern.match(line)
        if match:
            # We preserve the newline if it was present
            suffix = "\n" if line.endswith("\n") else ""
            return match.group(1) + "  <masked-date-time>" + suffix

        # Mask other date/time occurrences
        line = self.date_pattern.sub("<masked-date-time>", line)

        return line

    def normalize_content(self, content):
        """
        Normalizes a multiline string.

        :param content: The input string.
        :return: The normalized string.
        """
        lines = content.splitlines(keepends=True)
        return "".join(self.normalize_line(line) for line in lines)

    def normalize_file(self, input_path, output_path):
        """
        Reads a file, normalizes its content, and writes to an output file.

        :param input_path: Path to the input file.
        :param output_path: Path to the output file.
        """
        input_path = Path(input_path)
        output_path = Path(output_path)

        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        with open(input_path, 'r', errors='replace') as f_in:
            content = f_in.read()

        normalized_content = self.normalize_content(content)

        # Ensure parent directory of output_path exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f_out:
            f_out.write(normalized_content)
