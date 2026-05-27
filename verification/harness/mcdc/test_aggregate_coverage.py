import yaml
from pathlib import Path
from verification.harness.mcdc.aggregate_coverage import merge_reports

def test_merge_reports():
    report1 = {
        'decisions': {
            1: {
                'decision_id': 1,
                'executed': True,
                'total_conditions': 2,
                'conditions': {
                    1: {'covered': True},
                    2: {'covered': False}
                }
            }
        }
    }
    report2 = {
        'decisions': {
            1: {
                'decision_id': 1,
                'executed': True,
                'total_conditions': 2,
                'conditions': {
                    1: {'covered': False},
                    2: {'covered': True}
                }
            }
        }
    }

    merged = merge_reports([report1, report2])

    assert merged['decisions'][1]['executed'] is True
    assert merged['decisions'][1]['conditions'][1]['covered'] is True
    assert merged['decisions'][1]['conditions'][2]['covered'] is True
    assert merged['summary']['covered_conditions'] == 2
    assert merged['summary']['mcdc_percentage_overall'] == 100.0

if __name__ == "__main__":
    test_merge_reports()
    print("Aggregate coverage test passed!")
