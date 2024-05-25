from src.masks import mask_bank_account, mask_card


def card_account(type_number: str) -> str:
    """Функция которая вернет тип карты/счета и маску номера карты/счета"""
    elements = type_number.split()
    if len(elements[-1]) == 16:
        elements[-1] = mask_card(elements[-1])
        return " ".join(elements)
    else:
        elements[-1] = mask_bank_account(elements[-1])
        return " ".join(elements)


def data_view(data: str) -> str:
    """Функция которая возвращает дату в формате ДД.ММ.ГГГГ"""
    format_data = f"{data[8:10]}.{data[5:7]}.{data[:4]}"
    return format_data
