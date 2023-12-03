"""
Propósito: Pedir una frase por teclado y contar cuantas palabras tiene suponiendo que están separadas por espacios.

Autor: Rafael del Castillo Gomariz.
Fecha: 16/11/2020.

Análisis: Podemos ir recorriendo la cadena de forma que cuando nos encontremos un carácter que no sea un espacio
aumentamos el número de palabras en uno, necesitaremos un contador y un interruptor que nos diga si estamos en
un espacio o no.
"""

print("Contador de palabras")
print("--------------------")

# Petición de datos
user_string = input("Introduce una frase: ")

# Proceso
in_word = False
word_counter = 0
for c in user_string:
    if c != " ":
        if not in_word:
            in_word = True
            word_counter += 1
    else:
        in_word = False

# Salida
print("Número de palabras:", word_counter)
