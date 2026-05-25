import os
from verification.harness.mcdc.post_processor import parse_mcdc_log

def test_parse_mcdc_log(tmp_path):
    log_file = tmp_path / "mcdc_coverage.out"
    log_file.write_text(
        "B 1\n"
        "C 1 1 1\n"
        "C 1 2 0\n"
        "B 2\n"
        "C 2 1 1\n"
        "B 1\n"
        "C 1 1 0\n"
        "C 1 2 0\n"
    )

    results = parse_mcdc_log(str(log_file))

    assert 1 in results
    assert 2 in results

    # Decision 1 should have two evaluations
    assert len(results[1]) == 2
    assert results[1][0] == {1: True, 2: False}
    assert results[1][1] == {1: False, 2: False}

    # Decision 2 should have one evaluation
    assert len(results[2]) == 1
    assert results[2][0] == {1: True}

def test_parse_mcdc_nested(tmp_path):
    # Tests that nested decisions don't interfere
    log_file = tmp_path / "mcdc_coverage.out"
    log_file.write_text(
        "B 1\n"
        "C 1 1 1\n"
        "B 2\n"
        "C 2 1 0\n"
        "C 1 2 1\n"
    )

    results = parse_mcdc_log(str(log_file))

    assert results[1][0] == {1: True, 2: True}
    assert results[2][0] == {1: False}
