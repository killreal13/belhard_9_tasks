"""
Реализация Haversine formula для Python.
https://en.wikipedia.org/wiki/Haversine_formula

Написать функцию distance, которая будет возвращать расстояние между
точками GPS на карте в метрах.

Функция должна принимать следующие аргументы:
* a_lat - широта первой точки
* a_lon - долгота первой точки
* b_lat - широта второй точки
* b_lon - долгота второй точки

Алгоритм:
1. Посчитать значение каждой координаты в радианах.
Формула: float(value) * pi / 180
2. Вычислить sin и cos радианов широт из п1.
3. Вычислить разницу (delta) радианов долгот из п1.
4. Вычислить sin и cos разницы долгот из п3.
5. Вычислить y = sqrt(pow(b_lat_cos * delta_sin, 2)) + pow(a_lat_cos * b_lat_sin - a_lat_sin * b_lat_cos * delta_cos, 2))
6. Вычислить x = a_lat_sin * b_lat_sin + a_lat_cos * b_lat_cos * delta_cos
7. Вычислить ad = atan2(y, x)
8. Вернуть ad * EARTH_R
"""
import math
from math import sqrt

# радиус сферы (Земли)
EARTH_R = 6372795


def distance(a_lat,  a_lon, b_lat, b_lon) -> int:
    rad_a_lat = float(a_lat) * math.pi / 180
    rad_a_lon = float(a_lon) * math.pi / 180
    rad_b_lat = float(b_lat) * math.pi / 180
    rad_b_lon = float(b_lon) * math.pi / 180
    sin_a_lat = math.sin(rad_a_lat)
    cos_a_lat = math.cos(rad_a_lat)
    sin_b_lat = math.sin(rad_b_lat)
    cos_b_lat = math.cos(rad_b_lat)
    delta_lon = rad_a_lon - rad_b_lon
    delta_sin = math.sin(delta_lon)
    delta_cos = math.cos(delta_lon)
    y = sqrt(math.pow(cos_b_lat * delta_sin, 2)) + math.pow(cos_a_lat * sin_b_lat - sin_a_lat * cos_b_lat * delta_cos, 2)
    x = sin_a_lat * sin_b_lat + cos_a_lat * cos_b_lat * delta_cos
    ad = math.atan2(y, x)
    return ad * EARTH_R

