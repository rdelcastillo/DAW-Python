"""
Clase que modele un dado de parchís trucado que, de cuando en cuando, nos permita poner el valor que queramos en la cara
del dado (entre 1 y 6), de manera que:

- No se puede usar el método que pone el valor que queramos en la cara del dado (put) si no hemos tirado al menos tres
  veces de forma normal, si lo llamamos sin haberse cumplido esta excepción lanzaremos una excepción.
- Hay que tener en cuenta que NO PODEMOS cambiar directamente el valor de la cara de un dado, ya que se almacena en una
  variable de instancia privada de una clase de la que hereda (Dice) y no hay acceso.
"""

from ludo_dice import LudoDice

class TrickedLudoDice(LudoDice):
    __MIN_NORMAL_DICE_ROLLS = 3

    def __init__(self):
        self.__normal_dice_rolls = 0
        super().__init__()

    def roll(self):
        self.__normal_dice_rolls += 1
        return super().roll()

    def put(self, n: int):
        self.__check_put(n)
        self.__roll_until_n(n)
        self.__normal_dice_rolls = 0

    def __check_put(self, n):
        if n not in self.sides:
            raise ValueError(f"Valor incorrecto de cara del dado: {n}")
        if self.__normal_dice_rolls < self.__MIN_NORMAL_DICE_ROLLS:
            raise ValueError(f"No ha tirado aún {self.__MIN_NORMAL_DICE_ROLLS} veces.")

    def __roll_until_n(self, n):
        while True:
            super().roll()
            if self.side == n:
                break
