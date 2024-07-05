import re

from src.masks import mask_bank_account, mask_card


def card_account(type_number: str) -> str:
    """Функция которая вернет тип карты/счета и маску номера карты/счета"""

    if isinstance(type_number, str):
        pattern = re.compile(r"\D+ \D+ \d+|\D+ \d+")
        matches = pattern.findall(type_number)
        if matches:
            elements = type_number.split()
            if len(elements[-1]) == 16:
                elements[-1] = mask_card(elements[-1])
                return " ".join(elements)
            elif len(elements[-1]) == 20:
                elements[-1] = mask_bank_account(elements[-1])
                return " ".join(elements)
            else:
                return "Не верный номер карты/счета"
        else:
            return "Нет данных"
    else:
        return "Нет данных"


def data_view(data: str) -> str:
    """Функция которая возвращает дату в формате ДД.ММ.ГГГГ"""
    format_data = f"{data[8:10]}.{data[5:7]}.{data[:4]}"
    return format_data
