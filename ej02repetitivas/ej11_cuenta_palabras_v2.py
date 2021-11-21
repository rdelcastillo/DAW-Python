"""
Propósito: Pedir una frase por teclado y contar cuantas palabras tiene suponiendo que están separadas por espacios.

Autor: Rafael del Castillo Gomariz.
Fecha: 20/11/2020.

Análisis: Podemos ir recorriendo la cadena de forma que cuando nos encontremos un carácter que no sea un espacio
aumentamos el número de palabras en uno, necesitaremos un contador y un interruptor que nos diga si estamos en
un espacio o no.
"""

print("Contador de palabras")
print("--------------------")

# Petición de datos
user_string = input("Introduce una frase: ")

# Proceso
previous_char = " "
word_counter = 0
for current_char in user_string:
    if current_char != " " and previous_char == " ":
        word_counter += 1
    previous_char = current_char

# Salida
print("Número de palabras:", word_counter)
