# Programa: perimetro.py
# Propósito: Calcula el perímetro de una circunferencia y lo muestra.
# Autor: Rafael del Castillo.
# Fecha: 9/10/2019.
#
# Variables a usar:
#   * radio (numérico): el radio de la circunferencia a tratar
#   * perimetro: almacenaré el perímetro --> 2*PI*radio
#
# Algoritmo:
#   LEER radio
#   perimetro <-- 2*PI*radio
#   ESCRIBIR perimetro

import math

print("Cálculo del perímetro de una circunferencia")
print("-------------------------------------------")

# Petición de datos
# -----------------
# Usamos excepciones para controlar que el usuario no de valores no numéricos.
try:
    radius = float(input("Dame el radio de la circunferencia: "))
except ValueError:
    print("Tienes que introducir datos numéricos, lo introducido no lo es.")
    print("Ejecuta el programa de nuevo introduciendo los datos correctamente.")
    exit(1)

# Cálculos
perimeter = 2 * math.pi * radius

# Salida
print("El perímetro de la circunferencia es", perimeter)
