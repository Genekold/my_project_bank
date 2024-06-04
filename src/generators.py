from typing import Iterator


def filter_by_currency(list_of_banking_transactions: list, value: str) -> Iterator:
    """Функция - генератор которая возвращает список транзакций по заданному ключу 'currency'"""

    list_for_iteration = []
    for transaction in list_of_banking_transactions:
        transaction_currency = transaction["operationAmount"]["currency"]["code"]
        if transaction_currency == value:
            list_for_iteration.append(transaction)

    for one_transaction in list_for_iteration:
        yield one_transaction


def transaction_descriptions(list_of_banking_transactions: list) -> Iterator:
    """Функция - генератор, которая принимает список словарей и возвращает описание каждой операции по очереди."""

    for transaction in list_of_banking_transactions:
        if transaction.get("description"):
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator:
    """Функция генеррует номер банковской карты в заданном диапазаоне"""

    base_number = "0000000000000000"
    for numb in range(start, end + 1):
        len_end = len(str(numb))
        number_card = base_number[:-len_end] + str(numb)
        yield f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
