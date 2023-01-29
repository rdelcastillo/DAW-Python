"""
En este ejemplo se define una clase "Punto" con dos atributos "x" e "y", y se sobrecargan algunos operadores.

Autor: Rafael del Castillo Gomariz.
"""
from typeguard import typechecked

@typechecked
class Point:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __mul__(self, other: int):
        return Point(self.x * other, self.y * other)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

