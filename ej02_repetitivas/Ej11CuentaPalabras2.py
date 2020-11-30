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
cadena = input("Introduce una frase: ")

# Proceso
caracter_anterior = " "
contador_palabras = 0
for caracter_actual in cadena:
    if caracter_actual != " " and caracter_anterior == " ":
        contador_palabras += 1
    caracter_anterior = caracter_actual

# Salida
print("Número de palabras:", contador_palabras)
