def mask_card(nuber_card: str) -> str:
    """Функция которая маскирует номер карты в формате ХХХХ ХХ** **** ХХХХ"""

    first_digit = nuber_card[:4]
    second_digit = nuber_card[4:6]
    last_digit = nuber_card[-4:]
    result = f"{first_digit} {second_digit}** **** {last_digit}"

    return result


def mask_bank_account(number_bank_account: str) -> str:
    """Функция которая маскирует номер счета в формате **ХХХХ"""
    last_digits = number_bank_account[-4:]
    result = f"**{last_digits}"

    return result
