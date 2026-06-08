import pytest
from unittest.mock import patch, mock_open
from verification.harness.verify_gotos import verify_gotos

# Mock data for identify_gotos
MOCK_WEB_GOTOS = [
    {'module': 1, 'line': 10, 'target': 'exit'},
    {'module': 2, 'line': 20, 'target': '30'},
    {'module': 3, 'line': 30, 'target': 'exit', 'macro': 'return'}
]
MOCK_WEB_LABELS = []
MOCK_WEB_MACROS = {'return': 'goto exit'}

# Mock data for PascalGOTOExtractor.identify_gotos
MOCK_PASCAL_GOTOS = [
    {'module': 1, 'line': 100, 'target': 'exit'},
    {'module': 2, 'line': 200, 'target': '30'},
    {'module': 3, 'line': 300, 'target': 'exit'}
]
MOCK_PASCAL_LABELS = []

@patch('verification.harness.verify_gotos.identify_gotos')
@patch('verification.harness.verify_gotos.PascalGOTOExtractor.identify_gotos')
def test_verify_gotos_success(mock_pascal_extract, mock_web_extract):
    mock_web_extract.return_value = (MOCK_WEB_GOTOS, MOCK_WEB_LABELS, MOCK_WEB_MACROS)
    mock_pascal_extract.return_value = (MOCK_PASCAL_GOTOS, MOCK_PASCAL_LABELS)

    assert verify_gotos('dummy.web', 'dummy.p') == True

@patch('verification.harness.verify_gotos.identify_gotos')
@patch('verification.harness.verify_gotos.PascalGOTOExtractor.identify_gotos')
def test_verify_gotos_mismatch(mock_pascal_extract, mock_web_extract):
    # Pascal has an extra GOTO or wrong module
    bad_pascal_gotos = MOCK_PASCAL_GOTOS + [{'module': 4, 'line': 400, 'target': '99'}]

    mock_web_extract.return_value = (MOCK_WEB_GOTOS, MOCK_WEB_LABELS, MOCK_WEB_MACROS)
    mock_pascal_extract.return_value = (bad_pascal_gotos, MOCK_PASCAL_LABELS)

    assert verify_gotos('dummy.web', 'dummy.p') == False

@patch('verification.harness.verify_gotos.identify_gotos')
@patch('verification.harness.verify_gotos.PascalGOTOExtractor.identify_gotos')
def test_verify_gotos_case_insensitivity(mock_pascal_extract, mock_web_extract):
    web_gotos = [{'module': 1, 'line': 10, 'target': 'EXIT'}]
    pascal_gotos = [{'module': 1, 'line': 100, 'target': 'exit'}]

    mock_web_extract.return_value = (web_gotos, [], {})
    mock_pascal_extract.return_value = (pascal_gotos, [])

    assert verify_gotos('dummy.web', 'dummy.p') == True
