import pytest
from unittest.mock import patch, mock_open, MagicMock
from verification.harness.compare_signatures import compare_signatures, normalize_name

def test_normalize_name():
    assert normalize_name("Print_Id") == "printid"
    assert normalize_name("make_string") == "makestring"
    assert normalize_name("ID_LOOKUP") == "idlookup"
    assert normalize_name("simple") == "simple"

@patch("verification.harness.compare_signatures.extract_web_modules")
@patch("verification.harness.compare_signatures.PascalRoutineExtractor")
@patch("builtins.open", new_callable=mock_open, read_data="dummy content")
def test_compare_signatures_match(mock_file, mock_extractor_cls, mock_web_ext):
    mock_web_ext.return_value = [
        {'module': 1, 'name': 'Print_Id', 'kind': 'procedure'},
        {'module': 2, 'name': 'Id_Lookup', 'kind': 'function'}
    ]

    mock_extractor = mock_extractor_cls.return_value
    mock_extractor.extract_signatures.return_value = [
        {'name': 'printid', 'kind': 'procedure'},
        {'name': 'idlookup', 'kind': 'function'}
    ]

    matches, mismatches = compare_signatures("test.web", "test.p")

    assert len(matches) == 2
    assert len(mismatches) == 0

@patch("verification.harness.compare_signatures.extract_web_modules")
@patch("verification.harness.compare_signatures.PascalRoutineExtractor")
@patch("builtins.open", new_callable=mock_open, read_data="dummy content")
def test_compare_signatures_missing(mock_file, mock_extractor_cls, mock_web_ext):
    mock_web_ext.return_value = [
        {'module': 1, 'name': 'Missing_Proc', 'kind': 'procedure'}
    ]

    mock_extractor = mock_extractor_cls.return_value
    mock_extractor.extract_signatures.return_value = []

    matches, mismatches = compare_signatures("test.web", "test.p")

    assert len(matches) == 0
    assert len(mismatches) == 1
    assert mismatches[0]['type'] == 'missing_in_pascal'
    assert mismatches[0]['name'] == 'Missing_Proc'

@patch("verification.harness.compare_signatures.extract_web_modules")
@patch("verification.harness.compare_signatures.PascalRoutineExtractor")
@patch("builtins.open", new_callable=mock_open, read_data="dummy content")
def test_compare_signatures_kind_mismatch(mock_file, mock_extractor_cls, mock_web_ext):
    mock_web_ext.return_value = [
        {'module': 1, 'name': 'Wrong_Kind', 'kind': 'procedure'}
    ]

    mock_extractor = mock_extractor_cls.return_value
    mock_extractor.extract_signatures.return_value = [
        {'name': 'wrongkind', 'kind': 'function'}
    ]

    matches, mismatches = compare_signatures("test.web", "test.p")

    assert len(matches) == 0
    assert len(mismatches) == 1
    assert mismatches[0]['type'] == 'kind_mismatch'
    assert mismatches[0]['web_kind'] == 'procedure'
    assert mismatches[0]['pascal_kind'] == 'function'
