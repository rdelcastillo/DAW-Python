"""
En este ejemplo se define una clase "Punto" con dos atributos "x" e "y", y se sobrecargan algunos operadores.

La suma y la resta deben devolver objetos de la clase Point, para poder indicar que el parámetro es del mismo tipo que
la clase que estamos creando tenemos dos opciones:

- Hacer referencia a la propia clase utilizando el nombre de la clase entre comillas.
- Utilizar el módulo __future__ y la importación absoluta, lo cual permite referenciar la clase sin comillas. Esta es
  la recomendada en las versiones de Python 3.7 en adelante.

El módulo __future__ en Python es un mecanismo que permite a los desarrolladores habilitar características de versiones
futuras de Python en versiones actuales. Esto permite que el código escrito en una versión actual sea compatible con
cambios que se introducirán en versiones posteriores.

Autor: Rafael del Castillo Gomariz.
"""
from __future__ import annotations
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

    def __add__(self, other: Point):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other: Point):
        return Point(self.__x - other.__x, self.__y - other.__y)

    def __neg__(self):
        return Point(-self.__x, -self.__y)

    def __mul__(self, other: int):
        return Point(self.__x * other, self.__y * other)

    def __rmul__(self, other: int):  # para casos donde el operando está a la izquierda (5 * p)
        return self * other

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__x}, {self.__y})"
