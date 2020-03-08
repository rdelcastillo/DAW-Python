#!/usr/bin/env python3

"""
Ejemplo de paso de argumentos a un script.
"""

import sys

print("Nombre programa:", sys.argv[0])
print("Argumentos pasados:", len(sys.argv)-1)
print("Argumentos:", sys.argv[1:])
for n in range(len(sys.argv)):
    print(f"Argumento {n}: {sys.argv[n]}")
