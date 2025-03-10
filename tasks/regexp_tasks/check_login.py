"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re


def check_login(login: str) -> bool:
    if re.fullmatch('[A-Za-z0-9_]{5,20}', login):
        return True
    else:
        return False
