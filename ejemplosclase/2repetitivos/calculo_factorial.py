"""
Este programa calcula el factorial de un número introducido por el usuario.

Autor: Rafael del Castillo
Fecha: 3/11/2021
"""
import sys

print(f"Cálculo del factorial de un número")
print("-----------------------------------")

# Pedimos el número a calcular su factorial
num = int(input(f"Dame un número para que calcule su factorial: "))
if num < 0:
    print("No se puede calcular el factorial de un número negativo.", file=sys.stderr)
    exit(1)

# Cálculo del factorial
factorial = 1   # esta variable es un "acumulador"
for i in range(2, num+1):
    factorial *= i

# Muestro resultado
print("El factorial de", num, "es", factorial)
