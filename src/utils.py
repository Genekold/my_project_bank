import json
import os.path


def data_transaction(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Список словарей будет пустой если файл не найден, файл пустой, файл
    не содержит список или файл невозможно декодировать.
    :param path: путь до файла
    :return: список словарей с данными о финансовых транзакцияхю
    """

    if not os.path.exists(path):
        return [1]

    with open(path, encoding="utf8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []

        except json.JSONDecodeError:
            return []
