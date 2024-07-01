import re
from collections import defaultdict


def get_list_by_key(operations: list, state: str = "EXECUTED") -> list:
    """Функция вернет список словарей по ключу (state)"""

    new_list = []
    for operation in operations:
        if operation.get("state") == state:
            new_list.append(operation)

    return new_list


def sort_list_by_data(operations: list, ascending: bool = True) -> list:
    """Функция сортрует спиисок словарей по дате. По умолчанию (по убыванию)"""

    sort_list = sorted(operations, key=lambda operation: operation["date"], reverse=ascending)

    return sort_list


def get_filter_list_by_description(list_operations: list[dict], search_line: str) -> list[dict]:
    """
     Функция фильтрует банковские операции по строке введеной пользователем
    :param list_operations: Список словарей о банковских операций.
    :param search_line: Строка поиска.
    :return: Список словарей в которой есть в отисании строка поиска.
    """
    filtr_operation = []
    for operation in operations:
        descript = operation.get('description')
        try:
            match = re.search(search_line, descript, re.IGNORECASE)
            if match:
                filtr_operation.append(operation)
        except Exception:
            continue
    return filtr_operation


def get_count_operations_by_description(list_opetations: list[dict], list_category: list) -> list[dict]:
    """
    Функция счетчик операций по выбранным категориям
    :param list_opetations: Список словарей банковских операций.
    :param list_category: Список операций для поиска.
    :return:
    """
    filtr_operations = defaultdict(int)
    for operation in list_opetations:
        try:
            descript = operation.get('description')
            if descript in list_category:
                filtr_operations[descript] += 1
        except Exception:
            continue
    return filtr_operations
