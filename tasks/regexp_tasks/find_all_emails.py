"""
Написать функцию find_emails, которая принимает текст и находит в нем
все email вида some@some.some
"""
import re


def find_emails(some_text: str) -> list:
    return re.findall('[A-Z-a-z0-9\.-]+@[a-z]+\.[a-z]+', some_text)