"""
Clase "Rectángulo" (inmutable) determinada por sus dos lados (ancho y alto).

Tiene como propiedades su área y su perímetro.

Autor: Rafael del Castillo Gomariz.
"""
from typeguard import typechecked

@typechecked
class Rectangle:

    def __init__(self, width: int, height: int):
        if width <= 0 or height <= 0:
            raise ValueError("Los lados deben ser enteros positivos.")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def area(self):
        return self.width * self. height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"