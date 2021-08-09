"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""
import pathlib
import sys
from typing import Optional


def add_to_path(path: Optional[str]):
    sys.path.append(pathlib.Path(path).parent.resolve())

