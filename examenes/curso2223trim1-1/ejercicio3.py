"""
Realiza un conversor del sistema decimal al sistema de “palotes”.

Ejemplo:
Por favor, introduzca un número entero positivo: 47021
El 47021 en decimal es el | | | | - | | | | | | | - - | | - | en el sistema de palotes.

Si no se introduce un número entero positivo el programa debe terminar de manera anormal con un mensaje de error.
"""
import sys

print("Conversor de números al sistema de palotes")
print("------------------------------------------")

n = int(input("Dame un número entero positivo: "))
if n < 0:
    print("ERROR. El número introducido no es válido.", file=sys.stderr)
    exit(1)

for digit in str(n):
    print("|" * int(digit), "- ", end="")
print("\b\b ")  # para quitar el guion del final
