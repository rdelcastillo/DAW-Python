"""
Este programa pedirá al usuario el número de filas y columnas de una caja y la mostrará
por pantalla numerando cada celda de la caja con sus dos coordenadas.

El máximo tamaño de la caja será de 9x9.

Autor: Rafael del Castillo
Fecha: 27/10/2021
"""
import sys

print("Dibujo de una caja bidimensional")
print("--------------------------------")

# Pedimos las dimensiones de la caja

filas = int(input("Número de filas de la caja: "))
if filas < 1 or filas > 9:
    print("Dimensión de las filas incorrecta (entre 1 y 9).", file=sys.stderr)
    exit(1)

columnas = int(input("Número de columnas de la caja: "))
if columnas < 1 or columnas > 9:
    print("Dimensión de las columnas incorrecta (entre 1 y 9).", file=sys.stderr)
    exit(2)

# Impresión de la caja

for f in range(1, filas+1):
    for c in range(1, columnas+1):
        print(f"{f}{c}\t", end="")
    print()
