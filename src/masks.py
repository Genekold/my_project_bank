import logging
import os

from config import LOGS_DIR

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "masks.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card(nuber_card: str) -> str:
    """Функция которая маскирует номер карты в формате ХХХХ ХХ** **** ХХХХ"""

    logger.info(f'Получен номер карты {nuber_card}')
    first_digit = nuber_card[:4]
    second_digit = nuber_card[4:6]
    last_digit = nuber_card[-4:]
    result = f"{first_digit} {second_digit}** **** {last_digit}"
    logger.debug(f'замаскированный номер карты {result}')

    return result


def mask_bank_account(number_bank_account: str) -> str:
    """Функция которая маскирует номер счета в формате **ХХХХ"""

    logger.info(f'Получен номер cчета {number_bank_account}')
    last_digits = number_bank_account[-4:]
    result = f"**{last_digits}"
    logger.debug(f'Замаскированный номер счета {result}')

    return result


if __name__ == '__main__':
    print(mask_bank_account('70007922896063613356'))
