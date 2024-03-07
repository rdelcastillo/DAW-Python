"""
Clase Mobile, subclase de Terminal.

Cada móvil lleva asociada una tarifa que puede ser "rata", "mono" o "bisonte". El coste por minuto es de 6, 12 y 30
céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede cambiar.

Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada.

No cumple con el principio SOLID de responsabilidad única.

Autor: Rafael del Castillo Gomariz
"""
from enum import Enum
from typeguard import typechecked
from ej05poo.tanda3.ej11terminal.terminal import Terminal


@typechecked
class Mobile(Terminal):
    __Rate = Enum('Rate', "RATA MONO BISONTE")
    __RATA_PRICE = 0.06
    __MONO_PRICE = 0.12
    __BISONTE_PRICE = 0.30

    def __init__(self, number: str, rate: str):
        if not Mobile.exists_rate(rate):
            raise ValueError("La tarifa indicada es errónea")
        super().__init__(number)
        self.__rate = Mobile.__Rate[rate.upper()]
        self.__price = 0

    @classmethod
    def exists_rate(cls, rate: str):
        for r in cls.__Rate:
            if r.name == rate.upper():
                return True
        return False

    @property
    def rate(self):
        return self.__rate.name

    @property
    def price(self):
        return self.__price

    def call(self, other: Terminal, seconds: int):
        super().call(other, seconds)
        minutes = seconds / 60
        match self.__rate:
            case Mobile.__Rate.RATA: minute_price = Mobile.__RATA_PRICE
            case Mobile.__Rate.MONO: minute_price = Mobile.__MONO_PRICE
            case Mobile.__Rate.BISONTE: minute_price = Mobile.__BISONTE_PRICE
        self.__price += minutes * minute_price

    def __str__(self):
        return super().__str__() + f" - tarificados {self.__price:.2f} euros"
