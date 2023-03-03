"""
Clase Terminal.

Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos a otros y el tiempo de
conversación corre para ambos.

Los números de teléfono tienen que validarse como tales al crear el objeto (solo dígitos, empiezan por 9, 6 ó 7, su
longitud es de nueve dígitos) y no puede haber dos terminales con el mismo número.

Autor: Rafael del Castillo Gomariz
"""
from typeguard import typechecked

PHONE_NUMBER_LEN = 9

@typechecked
class Terminal:
    __registered_numbers = []

    def __init__(self, number: str):
        if not Terminal.__is_phone_number(number):
            raise ValueError("El número de teléfono es erróneo")
        if number in Terminal.__registered_numbers:
            raise ValueError("El número de teléfono ya ha sido dado de alta")
        Terminal.__registered_numbers.append(number)
        self.__number = number
        self.__talk_time = 0

    @property
    def number(self):
        return self.__number[:3] + " " + self.__number[3:5] + " " + self.__number[5:7] + " " + self.__number[7:9]

    @property
    def talk_time(self):
        return self.__talk_time

    def call(self, other: 'Terminal', seconds: int):
        if seconds < 0:
            raise ValueError("El tiempo de conversación no puede ser negativo")
        if other.number == self.number:
            raise ValueError("Un teléfono no se puede llamar a sí mismo")
        self.__talk_time += seconds
        other.__talk_time += seconds

    def __str__(self):
        return f"Nº {self.number} - {self.__talk_time}s de conversación"

    @staticmethod
    def __is_phone_number(number: str):
        return len(number) == PHONE_NUMBER_LEN and number[0] in "967" and number.isdigit()
