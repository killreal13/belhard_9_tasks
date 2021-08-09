"""
Написать класс FilmTypes, который будет наследоваться от Enum и содержать
константы-названия жанров фильмов.
"""
from enum import Enum


class FilmTypes(Enum):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    COMEDY = 'Comedy'
    CRIME = 'Crime'
    DRAMA = 'Drama'
    HISTORICAL = 'Historical'
    HORROR = 'Horror'
    MUSICAL = 'Musical'
    SCI_FI = 'Sci-fi'
    WAR = 'War'
    WESTERN = 'Western'
