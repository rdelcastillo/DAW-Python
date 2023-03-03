"""
Clase Car.

Hereda de Vehicle y además puede "quemar rueda".

El ASCII Art se ha sacado de https://ascii.co.uk/art/formula1

Autor: Rafael del Castillo Gomariz.
"""
from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.__burnout = "  _    _             /'_'_/.-''/                             _______\n" \
            + "  \\`../ |o_..__     / /__   / /  -= WORLD CHAMPIONSHIP =-   _\\=.o.=/_\n" \
            + "`.,(_)______(_).>  / ___/  / /                             |_|_____|_|\n" \
            + "~~~~~~~~~~~~~~~~~~/_/~~~~~/_/~~~~~~~~~~~~~~1DAW~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    def do_burnout(self):  #
        print(self.__burnout)
