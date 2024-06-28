import json
import logging
import os.path

import pandas as pd

from config import DATA_DIR, LOGS_DIR

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_from_json(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Список словарей будет пустой если файл не найден, файл пустой, файл
    не содержит список или файл невозможно декодировать.
    :param path: путь до файла.
    :return: список словарей с данными о финансовых транзакцияхю
    """

    file_path = os.path.join(DATA_DIR, path)

    if not os.path.exists(file_path):
        logger.error(f"{file_path} Такого файла не существует")
        return []

    try:
        if path.endswith('.json'):
            logger.debug(f"{path} это JSON-файл")
            with open((file_path), encoding="utf8") as file:
                data = json.load(file)
                logger.info(f"Файл {path} загружен")
                if isinstance(data, list):
                    logger.info("Обьект является списком")
                    return data
                else:
                    logger.error(f"Обьект {data} не является списком")
                    return []
        else:
            logger.debug(f"{path} это не JSON-файл")
            return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка кодирования {path} файла")
        return []
    except Exception as e:
        logger.error(f"Ошибка {e} при чтении {path} файла")


def get_transactions_from_csv(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до CSV-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Список словарей будет пустой если файл не найден, файл пустой, файл
    не содержит список или файл невозможно декодировать.
    :param path: путь до файла.
    :return: список словарей с данными о финансовых транзакцияхю
    """

    file_path = os.path.join(DATA_DIR, path)

    if not os.path.exists(file_path):
        logger.error(f"{file_path} Такого файла не существует")
        return []

    try:
        if path.endswith(".csv"):
            logger.debug(f"{path} это CSV-файл")
            data = pd.read_csv(file_path, encoding="utf8", delimiter=";")
            logger.info(f"Файл {path} загружен")
            return data.to_dict(orient="records")
        else:
            logger.debug(f"{path} это не CSV-файл")
            return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка кодирования {path} файла")
        return []
    except Exception as e:
        logger.error(f"Ошибка {e} при чтении {path} файла")

def get_transactions_from_xlsx(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до XLSX-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Список словарей будет пустой если файл не найден, файл пустой, файл
    не содержит список или файл невозможно декодировать.
    :param path: путь до файла.
    :return: список словарей с данными о финансовых транзакцияхю
    """

    file_path = os.path.join(DATA_DIR, path)

    if not os.path.exists(file_path):
        logger.error(f"{file_path} Такого файла не существует")
        return []

    try:
        if path.endswith(".xlsx"):
            logger.debug(f"{path} это XLSX-файл")
            data = pd.read_excel(file_path)
            logger.info(f"Файл {path} загружен")
            return data.to_dict(orient="records")
        else:
            logger.debug(f"{path} это не XLSX-файл")
            return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка кодирования {path} файла")
        return []
    except Exception as e:
        logger.error(f"Ошибка {e} при чтении {path} файла")

if __name__ == '__main__':
    print(get_transactions_from_json('operations.json'))
