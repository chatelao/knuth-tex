import pytest
from pathlib import Path
from verification.harness.comparer import Comparer
from verification.harness.normalizer import Normalizer

@pytest.fixture
def temp_files(tmp_path):
    f1 = tmp_path / "file1.txt"
    f2 = tmp_path / "file2.txt"
    return f1, f2

def test_compare_match(temp_files):
    f1, f2 = temp_files
    content = "Hello World\nLine 2\n"
    f1.write_text(content)
    f2.write_text(content)

    comparer = Comparer()
    match, diff = comparer.compare_text_files(f1, f2)
    assert match is True
    assert diff == ""

def test_compare_mismatch(temp_files):
    f1, f2 = temp_files
    f1.write_text("Hello World\nLine 2\n")
    f2.write_text("Hello World\nLine 2 modified\n")

    comparer = Comparer()
    match, diff = comparer.compare_text_files(f1, f2)
    assert match is False
    assert "Line 2 modified" in diff
    assert "--- " + str(f1) in diff
    assert "+++ " + str(f2) in diff

def test_compare_normalization_match(temp_files):
    f1, f2 = temp_files
    # Different dates, but same version banner
    f1.write_text("This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  4 JUL 1776 12:00\n")
    f2.write_text("This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  1 JAN 2000 00:00\n")

    comparer = Comparer()
    normalizer = Normalizer()

    # Should fail without normalizer
    match, _ = comparer.compare_text_files(f1, f2)
    assert match is False

    # Should pass with normalizer
    match, diff = comparer.compare_text_files(f1, f2, normalizer=normalizer)
    assert match is True
    assert diff == ""

def test_compare_normalization_mismatch(temp_files):
    f1, f2 = temp_files
    # Same version banner, but different content elsewhere
    f1.write_text("This is TeX, Version 3.141592653 (preloaded format=trip)  4 JUL 1776 12:00\nContent A\n")
    f2.write_text("This is TeX, Version 3.141592653 (preloaded format=trip)  1 JAN 2000 00:00\nContent B\n")

    comparer = Comparer()
    normalizer = Normalizer()

    match, diff = comparer.compare_text_files(f1, f2, normalizer=normalizer)
    assert match is False
    assert "Content A" in diff
    assert "Content B" in diff
    # The date part should be normalized in the diff
    assert "<masked-date-time>" in diff

def test_missing_files(temp_files):
    f1, f2 = temp_files
    comparer = Comparer()

    match, msg = comparer.compare_text_files(f1, f2)
    assert match is False
    assert "Expected file not found" in msg

    f1.write_text("exists")
    match, msg = comparer.compare_text_files(f1, f2)
    assert match is False
    assert "Actual file not found" in msg

def test_compare_tolerance_match(temp_files):
    f1, f2 = temp_files
    # Difference of 0.0001
    f1.write_text("Value: 12.3456\n")
    f2.write_text("Value: 12.3457\n")

    comparer = Comparer()
    # Fails without tolerance
    match, _ = comparer.compare_text_files(f1, f2)
    assert match is False

    # Passes with 0.001 tolerance
    match, diff = comparer.compare_text_files(f1, f2, tolerance=0.001)
    assert match is True
    assert diff == ""

def test_compare_tolerance_mismatch(temp_files):
    f1, f2 = temp_files
    # Difference of 0.1
    f1.write_text("Value: 12.3\n")
    f2.write_text("Value: 12.4\n")

    comparer = Comparer()
    # Fails even with 0.01 tolerance
    match, diff = comparer.compare_text_files(f1, f2, tolerance=0.01)
    assert match is False
    assert "-Value: 12.3" in diff
    assert "+Value: 12.4" in diff

def test_compare_tolerance_non_numeric_mismatch(temp_files):
    f1, f2 = temp_files
    # Numbers match but labels don't
    f1.write_text("Width: 10.0\n")
    f2.write_text("Height: 10.0\n")

    comparer = Comparer()
    match, diff = comparer.compare_text_files(f1, f2, tolerance=0.1)
    assert match is False
    assert "-Width: 10.0" in diff
    assert "+Height: 10.0" in diff

def test_compare_tolerance_multiple_numbers(temp_files):
    f1, f2 = temp_files
    f1.write_text("Coords: 10.0, 20.0, 30.0\n")
    f2.write_text("Coords: 10.05, 19.95, 30.0\n")

    comparer = Comparer()
    match, diff = comparer.compare_text_files(f1, f2, tolerance=0.1)
    assert match is True

def test_compare_binary_match(temp_files):
    f1, f2 = temp_files
    # "Binary" files (we'll mock the converter anyway)
    f1.write_text("binary1")
    f2.write_text("binary2")

    def mock_converter(binary_path, text_path):
        # Always output the same text for both
        with open(text_path, 'w') as f:
            f.write("symbolic representation")

    comparer = Comparer()
    match, diff = comparer.compare_binary_files(f1, f2, mock_converter)
    assert match is True
    assert diff == ""

def test_compare_binary_mismatch(temp_files):
    f1, f2 = temp_files
    f1.write_text("binary1")
    f2.write_text("binary2")

    def mock_converter(binary_path, text_path):
        # Output different text based on the "binary" content
        with open(binary_path, 'r') as f_in:
            content = f_in.read()
        with open(text_path, 'w') as f_out:
            f_out.write(f"symbolic {content}")

    comparer = Comparer()
    match, diff = comparer.compare_binary_files(f1, f2, mock_converter)
    assert match is False
    assert "symbolic binary1" in diff
    assert "symbolic binary2" in diff

def test_compare_binary_conversion_failure(temp_files):
    f1, f2 = temp_files
    f1.write_text("binary1")
    f2.write_text("binary2")

    def failing_converter(binary_path, text_path):
        raise RuntimeError("Something went wrong")

    comparer = Comparer()
    match, diff = comparer.compare_binary_files(f1, f2, failing_converter)
    assert match is False
    assert "Conversion failed: Something went wrong" in diff
