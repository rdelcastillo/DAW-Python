"""
Clase Mobile, subclase de Terminal.

Cada móvil lleva asociada una tarifa que puede ser "rata", "mono" o "bisonte". El coste por minuto es de 6, 12 y 30
céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede cambiar.

Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada.

Autor: Rafael del Castillo Gomariz
"""
from typeguard import typechecked
from ej05poo.tanda3.ej11terminal.terminal import Terminal
from rates import Rates


@typechecked
class Mobile(Terminal):

    def __init__(self, number: str, rate: str):
        if not Rates.exists(rate):
            raise ValueError("La tarifa indicada es errónea")
        super().__init__(number)
        self.__rate = rate.upper()
        self.__price = 0

    @property
    def rate(self):
        return self.__rate

    @property
    def price(self):
        return self.__price

    def call(self, other: Terminal, seconds: int):
        super().call(other, seconds)
        self.__price += Rates.price(self.__rate, seconds)

    def __str__(self):
        return super().__str__() + f" - tarificados {self.__price:.2f} euros"
