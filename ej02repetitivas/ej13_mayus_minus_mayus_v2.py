"""
Este programa lee una cadena por teclado y convierte las mayúsculas a minúsculas y viceversa.

Vamos a obviar que disponemos de los métodos de las cadenas.

Fecha: 25 de noviembre de 2024.
Autoría: Clase de 1ºDAW-A.
"""
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑÜ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyzáéíóúñü"

print("Conversión de mayúsculas a minúsculas y viceversa")
print("-------------------------------------------------")

user_string = input("Dame una cadena de caracteres: ")

final_string = ""
for c in user_string:
    # ¿c es mayúscula?
    index_c = 0
    for letter in UPPERCASE_LETTERS:
        if c == letter:
            break
        index_c += 1

    # cuando salga del ciclo, tendré que ver si he encontrado c en las mayúsculas
    if index_c < len(UPPERCASE_LETTERS):  # c está en las mayúsculas
        final_string += LOWERCASE_LETTERS[index_c]
    else:
        # ¿c es minúscula?
        index_c = 0
        for letter in LOWERCASE_LETTERS:
            if c == letter:
                break
            index_c += 1
        # cuando salga del ciclo, tendré que ver si he encontrado c en las minúsculas
        if index_c < len(LOWERCASE_LETTERS):  # c está en las minúsculas
            final_string += UPPERCASE_LETTERS[index_c]
        else:
            final_string += c

print("Resultado:", final_string)
