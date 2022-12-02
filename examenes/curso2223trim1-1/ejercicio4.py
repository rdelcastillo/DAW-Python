"""
Según cierta cultura oriental, los números de la suerte son el 3, el 7, el 8 y el 9. Los números de la mala suerte son
el resto: el 0, el 1, el 2, el 4, el 5 y el 6.

Un número es afortunado si contiene más números de la suerte que de la mala suerte.

Realiza un programa que diga si un número introducido por el usuario es afortunado o no.

Ejemplo 1:	Introduzca un número: 772
El 772 es un número afortunado.

Ejemplo 2:	Introduzca un número: 7720
El 7720 no es un número afortunado.

Ejemplo 3:	Introduzca un número: 43081
El 43081 no es un número afortunado.

Ejemplo 4:	Introduzca un número: 888
El 888 es un número afortunado.

Ejemplo 5:	Introduzca un número: 1234
El 1234 no es un número afortunado.

Ejemplo 6:	Introduzca un número: 6789
El 6789 es un número afortunado.
"""
import sys

print("Test de número afortunado")
print("-------------------------")

LUCKY_NUMBERS = "3789"

number = input("Introduzca un número: ")
if not number.isdigit():
    print("ERROR. No ha introducido un número.", file=sys.stderr)

# Contamos la cantidad de dígitos de la suerte
num_lucky_numbers = 0
for digit in number:
    if digit in LUCKY_NUMBERS:
        num_lucky_numbers += 1

# Si la cantidad de dígitos de la suerte es mayor que la mitad del total de dígitos, el número es afortunado
if num_lucky_numbers > len(number) // 2:
    print(f"El {number} es un número afortunado.")
else:
    print(f"El {number} no es un número afortunado.")