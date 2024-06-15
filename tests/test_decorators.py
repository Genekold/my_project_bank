import os

import pytest

from src.decorators import log


def test_log_to_console(capsys):
    @log()
    def my_function1(x, y):
        return x + y

    my_function1(2, 3)

    captured = capsys.readouterr()
    assert captured.out == "my_function1 ok\n"


def test_log_to_file():
    @log("test_log.txt")
    def my_function2(x, y):
        return x + y

    my_function2(1, 2)

    with open("test_log.txt") as file:
        text_log = file.read()

    assert "my_function2 ok" in text_log

    os.remove("test_log.txt")


def test_log_error_to_console(capsys):

    @log()
    def func_err1(x, y):
        raise IndexError("test_error")

    with pytest.raises(IndexError, match="test_error"):
        func_err1(8, 2)

    captured = capsys.readouterr()
    assert captured.out == "func_err1 error: IndexError. Inputs: (8, 2), {}\n"


def test_log_error_to_file():
    @log("test_log.txt")
    def func_err2(x, y):
        raise ValueError("test_error")

    with pytest.raises(ValueError, match="test_error"):
        func_err2(2, 4)

    with open("test_log.txt") as file:
        text_log = file.read()

    assert "func_err2 error: ValueError. Inputs: (2, 4), {}" in text_log

    os.remove("test_log.txt")
