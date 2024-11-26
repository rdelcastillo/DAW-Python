"""
Este programa lee una cadena por teclado y convierte las mayúsculas a minúsculas y viceversa.

No usamos métodos de cadena y aprovechamos que hay una diferencia de 32 en el código entre minúscula y mayúscula.

Fecha: 25 de noviembre de 2024.
Autoría: Clase de 1ºDAW-B.
"""

print("Conversión de mayúsculas a minúsculas y viceversa")
print("-------------------------------------------------")

user_string = input("Dame una cadena de caracteres: ")
final_string = ""
for c in user_string:
    if "a" <= c <= "z" or c == "á" or c == 'é' or c == 'í' or c == 'ó' or c == 'ú' or c == 'ñ' or c == 'ü':
        final_string += chr(ord(c) - 32)
    elif "A" <= c <= "Z" or c == "Á" or c == 'É' or c == 'Í' or c == 'Ó' or c == 'Ú' or c == 'Ñ' or c == 'Ü':
        final_string += chr(ord(c) + 32)
    else:
        final_string += c

print("Resultado:", final_string)
