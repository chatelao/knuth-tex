import pytest
from verification.harness.normalizer import Normalizer

def test_normalize_banner_tex():
    n = Normalizer()
    input_line = "This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  4 JUL 1776 12:00\n"
    expected = "This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  <masked-date-time>\n"
    assert n.normalize_line(input_line) == expected

def test_normalize_banner_mf():
    n = Normalizer()
    input_line = "This is Metafont, Version 2.7182818 (preloaded base=trap 1991.11.6)  6 NOV 1991 12:00\n"
    expected = "This is Metafont, Version 2.7182818 (preloaded base=trap 1991.11.6)  <masked-date-time>\n"
    assert n.normalize_line(input_line) == expected

def test_normalize_other_date():
    n = Normalizer()
    input_line = "Date of this run: 25 DEC 2023 08:30"
    expected = "Date of this run: <masked-date-time>"
    assert n.normalize_line(input_line) == expected

def test_normalize_content():
    n = Normalizer()
    content = (
        "This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  4 JUL 1776 12:00\n"
        "** &trip  trip\n"
        "(trip.tex ##\n"
        "End of run: 4 JUL 1776 12:05\n"
    )
    expected = (
        "This is TeX, Version 3.141592653 (preloaded format=trip 1776.7.4)  <masked-date-time>\n"
        "** &trip  trip\n"
        "(trip.tex ##\n"
        "End of run: <masked-date-time>\n"
    )
    assert n.normalize_content(content) == expected
