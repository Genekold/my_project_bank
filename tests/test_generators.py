import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(list_transactions):
    generator = filter_by_currency(list_transactions, "USD")
    assert next(generator)["id"] == 939719570
    assert next(generator)["id"] == 142264268
    assert next(generator)["id"] == 895315941


def test_filter_by_currency_empty_list(list_transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(list_transactions, ""))


def test_transaction_descriptions(list_transactions):
    generator = transaction_descriptions(list_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_empty_list():
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)


def test_card_number_generator():
    generator = card_number_generator(1234234, 1234237)
    assert next(generator) == "0000 0000 0123 4234"
    assert next(generator) == "0000 0000 0123 4235"
    assert next(generator) == "0000 0000 0123 4236"
    assert next(generator) == "0000 0000 0123 4237"


def test_card_number_generator_wrong_value():
    with pytest.raises(StopIteration):
        assert next(card_number_generator(10, 1))
