def sort_list_by_key(operations: list, state='EXECUTED') -> list:
    """Функция отсортирует список словарей по ключу 'state'"""

    new_list = []
    for operation in operations:
        if operation.get('state') == state:
            new_list.append(operation)

    return new_list


