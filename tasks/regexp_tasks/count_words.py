"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words(some_text: str) -> int:
    counter = re.finditer('[^ \W]?[A-Za-zА-Яа-я]+[^ \W]', some_text)
    result = list()
    for word in counter:
        result.append(word)
    return len(result)
