"""
Clase Bike.

Hereda de Vehicle y además puede "hacer el caballito".

El ASCII Art se ha sacado de http://stuffthatspins.com/stuff/ASCII-Art-bicycle-bike-cycling.html

Autor: Rafael del Castillo Gomariz.
"""
from vehicle import Vehicle


class Bike(Vehicle):
    __WHEELIE = "            o       _      _          _\n" \
                + "   _o      /\\_    _ \\\\o   (_)\\__/o   (_)\n" \
                + " _< \\_    _>(_)  (_)/<_     \\_| \\    _|/' \\/\n" \
                + "(_)>(_)  (_)         (_)    (_)     (_)'  _\\o_\n" \
                + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1DAW~~\n"


    @classmethod
    def do_wheelie(cls):
        print(cls.__WHEELIE)
        