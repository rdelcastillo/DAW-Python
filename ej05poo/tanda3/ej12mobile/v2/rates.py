"""
Clase para manejo de las tarifas de la clase Mobile.

Incumple el principio SOLID abierto/cerrado.
"""
from typeguard import typechecked


@typechecked
class Rates:
    __rates = {'RATA': 0.06, 'MONO': 0.12, 'BISONTE': 0.3}

    @classmethod
    def exists(cls, rate: str):
        return rate.upper() in cls.__rates

    @classmethod
    def price(cls, rate: str, seconds: int):
        if not cls.exists(rate):
            raise ValueError(f"La tarifa {rate} no existe")
        return cls.__rates[rate.upper()] * seconds/60
