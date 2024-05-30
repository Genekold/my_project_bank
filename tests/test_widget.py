import pytest

from src.widget import card_account, data_view


def test_card_account(number_card, number_account):
    assert card_account(number_card) == "Visa Gold 5999 41** **** 6353"

    assert card_account(number_account) == "Счет **9589"


def test_data_view():
    assert data_view("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.mark.parametrize("value, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982", "Не верный номер карты/счета")
])
def test_card_account_parametrize(value, expected):
    assert card_account(value) == expected
