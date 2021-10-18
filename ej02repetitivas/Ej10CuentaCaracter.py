"""
Propósito: Pedir una cadena y un carácter por teclado y mostrar cuantas veces aparece el carácter en la cadena.

Autor: Rafael del Castillo Gomariz.
Fecha: 16/11/2020.
"""

print("Ocurrencias de un carácter en una cadena")
print("----------------------------------------")

# Petición de datos
cadena = input("Introduce una cadena: ")  # pedimos cadena

caracter = input("Introduce un carácter: ")  # pedimos carácter (longitud de la cadena == 1)
while len(caracter) != 1:
    caracter = input(f"{caracter} no es un carácter. Introduce un carácter válido: ")

# Proceso (el método str.count() hace esto sin necesidad de este código)
ocurrencias = 0
for c in cadena:
    if c == caracter:
        ocurrencias += 1

# Salida
print(f"El carácter {caracter} aparece en la cadena introducida {ocurrencias} veces.")
