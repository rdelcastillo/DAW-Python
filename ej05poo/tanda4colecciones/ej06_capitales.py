"""
Programa que sabe decir la capital de un país (en caso de conocer la respuesta) y que, además, es capaz de aprender
nuevas capitales. En principio, el programa solo conoce las capitales de España, Portugal y Francia. Estos datos deberán
estar almacenados en un diccionario. Los datos sobre capitales que vaya aprendiendo el programa se deben almacenar en el
mismo diccionario. El usuario sale del programa escribiendo la palabra “salir”.

Ejemplo:

Escribe el nombre de un país y te diré su capital: España
La capital de España es Madrid
Escribe el nombre de un país y te diré su capital: Alemania
No conozco la respuesta ¿cuál es la capital de Alemania?: Berlín
Gracias por enseñarme nuevas capitales
Escribe el nombre de un país y te diré su capital: Portugal
La capital de Portugal es Lisboa
Escribe el nombre de un país y te diré su capital: Alemania
La capital de Alemania es Berlín
Escribe el nombre de un país y te diré su capital: Francia
La capital de Francia es París
Escribe el nombre de un país y te diré su capital: salir

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""

capitals = {
    "España": "Madrid",
    "Portugal": "Lisboa",
    "Francia": "París"
}

while True:
    country = input("Escribe el nombre de un país y te diré su capital: ").capitalize()
    if country == "Salir":
        break

    if country in capitals:
        print("La capital de", country, "es", capitals[country])
    else:
        capital = input(f"No conozco la respuesta ¿cuál es la capital de {country}: ").capitalize()
        capitals[country] = capital

print("Adiós")
