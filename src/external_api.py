import os

import requests

from dotenv import load_dotenv


def get_convert_currency(amount: float, currency: str, to_currency: str = "RUB") -> float:
    """
    Функция, котрая переводит сумму транзации в рубли по дейсвующему курсу
    :param amount: сумма транзакции
    :param currency: валюта танзакции
    :param to_currency: валюта в которую необходимо конвертировать (по умолчанию рубли)
    :return: сумма транзакции в запрашиваемой валюте
    """
    load_dotenv()
    url = "https://api.apilayer.com/exchangerates_data/convert"
    header = {'apikey': os.getenv('API_KEY')}
    params = {'amount': amount, 'from': currency, 'to': to_currency}
    response = requests.get(url, headers=header, params=params)
    if response.status_code != 200:
        return f'Неуспешный запрос'
    data = response.json()
    convert_amount = round(data['result'], 2)

    return convert_amount


def get_convert_trasaction(transaction: dict) -> float | None:
    """
    Функция принимает на вход транзакцию и возвращает сумму в рублях
    :param transaction: словарь транзакции
    :return: сумма в рублях.
    """

    try:
        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['code']

        if currency != 'RUB':
            return get_convert_currency(amount, currency)
        return float(amount)
    except KeyError as e:
        raise KeyError(f'Ключ не найден')
