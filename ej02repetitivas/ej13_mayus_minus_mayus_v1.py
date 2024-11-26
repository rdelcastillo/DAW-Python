"""
Este programa lee una cadena por teclado y convierte las mayúsculas a minúsculas y viceversa.

Fecha: 22 de noviembre de 2021.
Autoría: Clase de 1ºDAW-B.
"""

print("Conversión de mayúsculas a minúsculas y viceversa")
print("-------------------------------------------------")

user_string = input("Dame una cadena de caracteres: ")
final_string = ""
for c in user_string:
    if c.islower():
        final_string += c.upper()
    elif c.isupper():
        final_string += c.lower()
    else:
        final_string += c

print("Resultado:", final_string)
