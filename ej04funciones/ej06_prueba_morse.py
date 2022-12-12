"""
Programa para comprobar que la función morse() funciona bien.

Autor: Rafael del Castillo Gomariz
Fecha: 12/12/2022
"""
from ej06_morse import morse

print("Conversor de números a Morse")
print("----------------------------")

n = int(input("Dame un número entero: "))
print(f"{n} convertido a Morse es: {morse(n)}\n")

n = float(input("Dame un número decimal: "))
print(f"{n} convertido a Morse es: {morse(n)}")