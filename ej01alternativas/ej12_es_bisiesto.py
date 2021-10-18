"""
Programa que pide un año y nos dice si ese año es bisiesto.

Autores/as: Clase 1ºDAW Curso 2019/20
"""

# Informar del programa:
print("Programa para indicar si un año es bisiesto.")
print("------------------------------------------\n")

# Leer las variables:
year = int(input("Introduzca el año: "))
print("\n")

# Comprobar si es bisiesto y mostrar el resultado:
if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print("El año", year, "es bisiesto")
else:
    print("El año", year, "NO es bisiesto")
