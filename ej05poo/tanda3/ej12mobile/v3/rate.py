"""
Clase para manejo de las tarifas de la clase Mobile.
"""
from typeguard import typechecked


@typechecked
class Rate:
    __rates = {'RATA': 0.06, 'MONO': 0.12, 'BISONTE': 0.3}

    def __init__(self, rate: str):
        rate = rate.upper()
        if rate not in Rate.__rates:
            raise ValueError(f"La tarifa {rate} es errónea")
        self.__name = rate
        self.__minute_fee = Rate.__rates[rate]

    @property
    def name(self):
        return self.__name

    @property
    def minute_fee(self):
        return self.__minute_fee

    def price(self, seconds: int):
        return self.__minute_fee * seconds/60
