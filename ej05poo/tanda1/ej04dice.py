"""
Otra implementación de la clase "Dado". Por defecto el dado tiene 6 caras. Hay tres formar de construir un dado:

- No se le pasa nada al constructor e inicializa el dado al azar.
- Solo se le pasa que número tiene el dado en la cara superior.
- Se le pasa el número del dado en la cara superior y el número de caras del dado.

Autor: Rafael del Castillo Gomariz.
Fecha: 22/1/2023.
"""
import random
from typing import Optional

from typeguard import typechecked

DEFAULT_NUM_SIDES = 6

@typechecked
class Dice:

    def __init__(self, side: Optional[int] = None, num_sides = DEFAULT_NUM_SIDES):
        """
        Inicializa los valores del dado.
        :param side: Cara del dado, si no se pasa toma valor None, Optional[int] admite None e int
        :param num_sides: Número de caras del dado, por defecto 6.
        """
        if num_sides <= 0:
            raise ValueError(f"El número de caras del dado no puede ser menor o igual a cero. Recibido: {num_sides}")
        self.__num_sides = num_sides

        if side is None:
            self.roll()
            return
        if side <= 0 or side > num_sides:
            raise ValueError(f"No se le puede asignar al dado un valor menor o igual a cero o mayor que el número de "
                             f"caras. Recibido: {side}")
        self.__side = side

    @property
    def side(self):
        return self.__side

    def __str__(self):
        return str(self.__side)

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.__side}, num_sides={self.__num_sides})"

    def roll(self):
        self.__side = random.randint(1, self.__num_sides)
        return self.__side
