#!/usr/bin/env python3

"""
Ejemplo de paso de argumentos a un script.

La primera línea (#...) es para que este programa pueda funcionar desde un sistema operativo GNU/Linux sin llamar
explícitamente al intérprete de Python, se hace de forma implícita, y funciona como un script.

Autor: Rafael del Castillo Gomariz.
"""

import sys

print("Nombre programa:", sys.argv[0])
print("Argumentos pasados:", len(sys.argv)-1)
print("Argumentos:", sys.argv[1:])
for n, arg in enumerate(sys.argv):
    print(f"Argumento {n}: {arg}")
