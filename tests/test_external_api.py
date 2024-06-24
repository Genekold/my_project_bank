import unittest
from unittest.mock import patch

import requests

from src.external_api import get_convert_trasaction


@patch("requests.get")
def test_get_convert_trasaction(mock_get):
    transaction = {
    "id": 636137913,
    "state": "EXECUTED",
    "date": "2019-06-16T22:17:01.825020",
    "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "USD",
        "code": "RUB"
      }
    }}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_convert_trasaction(transaction) == 100


@patch("requests.get")
def test_get_convert_trasaction(mock_get):
    transaction = {
    "id": 636137913,
    "state": "EXECUTED",
    "date": "2019-06-16T22:17:01.825020",
    "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8824.85}
    assert get_convert_trasaction(transaction) == 8824.85


@patch("requests.get")
def test_get_convert_trasaction(mock_get):
    transaction = {
    "id": 636137913,
    "state": "EXECUTED",
    "date": "2019-06-16T22:17:01.825020",
    "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "USD",
        "code": "EUR"
      }
    }}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 9435.03}
    assert get_convert_trasaction(transaction) == 9435.03