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
