"""
Este programa pide una cadena y dos caracteres por teclado y sustituye la aparición del primer carácter
en la cadena por el segundo carácter.

Fecha: 22 de Noviembre de 2021.
Autoría: Clase de 1ºDAW-B.
"""
import sys

print("Sustitución de un carácter por otro en una cadena")
print("-------------------------------------------------")

# Petición los datos
user_string = input("Dame una cadena de caracteres: ")
char_to_replace = input("Carácter a sustituir en la cadena: ")
if len(char_to_replace) != 1:
    print("No es un carácter", file=sys.stderr)
    exit(1)
char_replaced = input("Carácter por el que lo reemplazaremos: ")
if len(char_replaced) != 1:
    print("No es un carácter", file=sys.stderr)
    exit(1)

# Proceso de sustitución
final_string = ""
for c in user_string:
    if c == char_to_replace:
        final_string += char_replaced
    else:
        final_string += c

print("Resultado:", final_string)