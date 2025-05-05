"""
Clase Car.

Hereda de Vehicle y además puede "quemar rueda".

El ASCII Art se ha sacado de https://ascii.co.uk/art/formula1

Autor: Rafael del Castillo Gomariz.
"""
from vehicle import Vehicle


class Car(Vehicle):
    __FUEL_TANK_CAPACITY = 50.0
    __FUEL_CONSUMED_PER_KM = 0.1
    __FUEL_CONSUMED_BY_BURNOUT = 1
    __BURNOUT = "  _    _             /'_'_/.-''/                             _______\n" \
            + "  \\`../ |o_..__     / /__   / /  -= WORLD CHAMPIONSHIP =-   _\\=.o.=/_\n" \
            + "`.,(_)______(_).>  / ___/  / /                             |_|_____|_|\n" \
            + "~~~~~~~~~~~~~~~~~~/_/~~~~~/_/~~~~~~~~~~~~~~1DAW~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    def __init__(self):
        super().__init__()
        self.__fuel = 0.0

    @property
    def fuel(self):
        return self.__fuel

    def do_burnout(self):
        if self.__fuel < self.__FUEL_CONSUMED_BY_BURNOUT:
            raise ValueError("No hay combustible para quemar rueda")
        print(self.__BURNOUT)
        self.__fuel -= self.__FUEL_CONSUMED_BY_BURNOUT

    def fill_tank(self):
        self.__fuel = self.__FUEL_TANK_CAPACITY

    def travel(self, kilometers_traveled: float):
        fuel_consumed = self.__FUEL_CONSUMED_PER_KM * kilometers_traveled
        if self.__fuel - fuel_consumed < 0:
            kilometers_traveled = self.__fuel / self.__FUEL_CONSUMED_PER_KM
            fuel_consumed = self.__fuel
        self.__fuel -= fuel_consumed
        super().travel(kilometers_traveled)
