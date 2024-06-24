import json
import os
from unittest.mock import patch, mock_open

from config import ROOT_DIR
from src.utils import data_transaction


def test_data_transaction(json_transactions_from_file):
    file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')

    assert data_transaction(file_path) == json_transactions_from_file

    not_file_path = os.path.join(ROOT_DIR, "data", "nonefile.json")
    assert data_transaction(not_file_path) == []


@patch('builtins.open')
def test_data_transaction_patch(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    mock_file.read.return_value = json.dumps({})
    assert data_transaction("test.json") == []

    mock_file.read.return_value = json.dumps("testtest")
    assert data_transaction("test.json") == []

    mock_file.read.return_value = ""
    assert data_transaction("test.json") == []
