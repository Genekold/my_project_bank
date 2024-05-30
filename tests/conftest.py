import pytest


@pytest.fixture
def number_card():
    return "Visa Gold 5999414228426353"


@pytest.fixture
def number_account():
    return "Счет 64686473678894779589"


@pytest.fixture
def list_by():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
