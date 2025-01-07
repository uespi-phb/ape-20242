
from random import randint


class Die:
    def __init__(self, sides=6):
        if not isinstance(sides, int):
            raise TypeError(f'Argument sides must be int: {sides}')
        if sides < 1:
            raise ValueError(
                f'Argument sides must be greater than zero: {sides}'
            )
        self.__sides = sides

    def roll(self):
        return randint(1, self.__sides)

    def get_sides(self):
        return self.__sides
