from src.widget import data_view


def get_list_by_key(operations: list, state='EXECUTED') -> list:
    """Функция вернет список словарей по ключу 'state'"""

    new_list = []
    for operation in operations:
        if operation.get('state') == state:
            new_list.append(operation)

    return new_list


def sort_list_by_data(operations: list, ascending=True):
    """Функция сортрует спиисок словарей по дате. По умолчанию (по убыванию)"""

    sort_list = sorted(operations, key=lambda operation: operation["date"], reverse=ascending)

    return sort_list
