import json
import logging
import os.path

from config import LOGS_DIR, DATA_DIR

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def data_transaction(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Список словарей будет пустой если файл не найден, файл пустой, файл
    не содержит список или файл невозможно декодировать.
    :param path: путь до файла
    :return: список словарей с данными о финансовых транзакцияхю
    """

    file_path = os.path.join(DATA_DIR, path)

    if not os.path.exists(file_path):
        logger.error(f'{file_path} Такого пути не существует')
        return []

    with open((file_path), encoding="utf8") as file:
        try:
            data = json.load(file)
            logger.info('Файл загружен')
            if isinstance(data, list):
                logger.info('Обьект является списком')
                return data
            else:
                logger.error(f'Обьект {data} не является списком')
                return []

        except json.JSONDecodeError:
            logger.error('Это не JSON-обьект')
            return []
