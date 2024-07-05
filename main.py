from src.processing import get_list_by_key, sort_list_by_data, get_filter_list_by_description
from src.utils import get_transactions_from_json, get_transactions_from_csv, get_transactions_from_xlsx
from src.widget import data_view, card_account


def get_data_on_user_choice(answer: str) -> list[dict]:
    """
    Функция для загрузки списка транзацкций из фала в зависимости от выбора пользователя
    :param answer: Строчное значение выбора пользователя
    :return: Загруженый список словарей транзакций
    """
    if answer == "1":
        print('Для обработки выбран JSON-файл')
        return get_transactions_from_json("operations.json")
    elif answer == "2":
        print('Для обработки выбран CSV-файл')
        return get_transactions_from_csv("transactions.csv")
    elif answer == "3":
        print('Для обработки выбран XLSX-файл')
        return get_transactions_from_xlsx("transactions_excel.xlsx")
    else:
        print("В меню такого нет.")
        user_answer = input("Выбери пункт снова:")
        get_data_on_user_choice(user_answer)


def get_filter_by_status(transactions: list[dict], status: str) -> list[dict]:
    """
    Функция фильтрует список транзакций по выбранному пользователем статусу
    :param transactions: Список словарей транзакций
    :param status: Строчное значение выбранного статуса
    :return: Отфильтрованный список транзакций
    """
    base_status = ["EXECUTED", "CANCELED", "PENDING"]
    if status not in base_status:
        print("""Такого ствтуса в операциях нет. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        status = input("Введите статус: ")
        upper_status = status.upper()
        get_filter_by_status(transactions, upper_status)
        print(f"Операции отфильтрованы по статусу {upper_status}")
    return get_list_by_key(transactions, status)


# def filtr_by_code()
def main():
    """ Основная функция программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файл
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
          """)
    user_answer = input("Введи пункт:")
    data_tansactions = get_data_on_user_choice(user_answer)

    print("""Выберите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    status = input("Введите статус: ")
    upper_status = status.upper()
    data_filter_transaction = get_filter_by_status(data_tansactions, upper_status)

    print("Для уточнения выборки операций, необходимо ответить на несколько вопросов.")
    while True:
        sort_by_date = input("Отсортировать операции по дате? Да/Нет \nОтвет: ")
        if sort_by_date.lower() == "да":
            while True:
                sort_by_descending = input("Отсортировать по возрастанию или по убыванию? \nОтвет: ")
                if sort_by_descending.lower() == "по возрастанию":
                    finish_list = sort_list_by_data(data_filter_transaction, False)
                    break
                elif sort_by_descending.lower() == "по убыванию":
                    finish_list = sort_list_by_data(data_filter_transaction)
                    break
            break
        elif sort_by_date.lower() == "нет":
            finish_list = data_filter_transaction
            break

    while True:
        filter_by_code = input("Выводить только рублевые тразакции? Да/Нет \nОтвет: ")
        if filter_by_code.lower() == "да":
            if user_answer == "1":
                finish_list = [i for i in finish_list if i["operationAmount"]["currency"]["code"] == "RUB"]
            else:
                finish_list = [i for i in finish_list if i.get("currency_code") == "RUB"]
            break
        elif filter_by_code.lower() == "нет":
            finish_list = data_filter_transaction
            break

    while True:
        filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \nОтвет: ")
        if filter_by_word.lower() == "да":
            word = input("Введите слово для поиска: ")
            finish_list = get_filter_list_by_description(finish_list, word)
            break
        elif filter_by_word.lower() == "нет":
            break

    print("Распечатываю итоговый список трназакций... \n")

    if len(finish_list) > 0:

        print(f"\nВсего банковсих операций в выборке {len(finish_list)}\n")
        for transaction in finish_list:
            # print(type(transaction.get("from", "нет")))
            date = data_view(transaction.get("date", "нет данных"))
            from_data = card_account(transaction.get("from", "нет данных"))
            to_data = card_account(transaction.get("to", "нет данных"))
            if user_answer == "1":
                description = transaction["description"]
                amount = transaction["operationAmount"]["amount"]
                currency_code = transaction["operationAmount"]["currency"]["code"]
            else:
                description = transaction.get("description")
                amount = transaction.get("amount")
                currency_code = transaction.get("currency_code")

            print(f"{date} {description}\n{from_data} -> {to_data} \nСумма: {amount} {currency_code}\n")

    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == '__main__':
    main()
