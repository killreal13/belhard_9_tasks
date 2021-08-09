"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""
import datetime
import pendulum


def convert_date(timestamp, current_zone, new_zone):
    new_timestamp = datetime.datetime.strptime(timestamp, '%Y.%m.%d %H:%M:%S').replace(tzinfo=pendulum.timezone(current_zone))
    return pendulum.timezone(new_zone).convert(new_timestamp)
