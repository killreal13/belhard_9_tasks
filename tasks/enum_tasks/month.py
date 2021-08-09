"""
Написать класс Month, который будет наследоваться от Enum и содержать
константы-названия месяцев на английском языке
"""
from enum import Enum


class Month(Enum):
    MONTH_1 = 'January'
    MONTH_2 = 'February'
    MONTH_3 = 'March'
    MONTH_4 = 'April'
    MONTH_5 = 'May'
    MONTH_6 = 'June'
    MONTH_7 = 'July'
    MONTH_8 = 'August'
    MONTH_9 = 'September'
    MONTH_10 = 'October'
    MONTH_11 = ''