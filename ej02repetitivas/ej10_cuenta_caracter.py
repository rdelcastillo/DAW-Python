"""
Propósito: Pedir una cadena y un carácter por teclado y mostrar cuantas veces aparece el carácter en la cadena.

Autor: Rafael del Castillo Gomariz.
Fecha: 16/11/2020.
"""

print("Ocurrencias de un carácter en una cadena")
print("----------------------------------------")

# Petición de datos
user_string = input("Introduce una cadena: ")  # pedimos cadena

char = input("Introduce un carácter: ")  # pedimos carácter (longitud de la cadena == 1)
while len(char) != 1:
    char = input(f"{char} no es un carácter. Introduce un carácter válido: ")

# Proceso (el método str.count() hace esto sin necesidad de este código)
occurrences_char = 0
for c in user_string:
    if c == char:
        occurrences_char += 1

# Salida
print(f"El carácter {char} aparece en la cadena introducida {occurrences_char} veces.")
