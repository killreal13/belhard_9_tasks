"""
Написать класс Day, который будет наследоваться от Enum и содержать
константы-названия дней недели на английском языке
"""
from enum import Enum


class Day(Enum):
    DAY_1 = 'Monday'
    DAY_2 = 'Tuesday'
    DAY_3 = 'Wednesday'
    DAY_4 = 'Thursday'
    DAY_5 = 'Friday'
    DAY_6 = 'Saturday'
    DAY_7 = 'Sunday'
