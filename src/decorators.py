from functools import wraps
from typing import Any, Callable


def log(filepath: str | None = None) -> Callable[..., Any]:
    """
    Декоратор для логгирования вызовов функций и их результатов
    :param filepath: Путь к файлу для записи логов. По умолчанию произойдет вывод в консоль
    :return: Функция или None в случае ошибки
    """

    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                massege = f"{func.__name__} ok"
                return result

            except Exception as e:
                massege = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                raise

            finally:
                if not filepath:
                    print(massege)

                else:
                    with open(filepath, "a") as file:
                        file.write(massege + "\n")

        return inner

    return wrapper
