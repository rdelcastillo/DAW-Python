"""
Aplicación que permita adivinar un número.

La aplicación genera un número aleatorio del 1 al 100. A continuación va
pidiendo números y va respondiendo si el número a adivinar es mayor o
menor que el introducido, además de los intentos que te quedan
(tienes 10 intentos para acertarlo).

El programa termina cuando se acierta el número (además te dice en
cuantos intentos lo has acertado), si se llega al limite de intentos te
muestra el número que había generado.

Fecha: 11/11/2019.

Autores: Clase de 1ºDAW

Otra versión del programa anterior.
"""

import random

# Constantes
STARTING_NUMBER = 1
FINAL_NUMBER = 100
MAXIMUM_TRIES = 10

# Inicializamos
number_to_guess = random.randint(STARTING_NUMBER, FINAL_NUMBER)

# Proceso

# implementamos un ciclo postcondición, ejecutamos la instrucción
# antes de entrar en el ciclo y al final del ciclo.
input_number = int(input(f"Introduce un número entre {STARTING_NUMBER} y {FINAL_NUMBER}: "))
remaining_tries = MAXIMUM_TRIES - 1
while input_number != number_to_guess and remaining_tries > 0:
    if input_number < number_to_guess:
        print(f"{input_number} es menor que el número a adivinar.")
    else:
        print(f"{input_number} es mayor que el número a adivinar.")
    input_number = int(input("Te quedan " + str(remaining_tries) +
                                   " intentos. Introduce un número entre 1 y 100: "))
    remaining_tries -= 1

# Mostramos resultado
if input_number == number_to_guess:  # ha adivinado
    print(f"Has adivinado el número en {MAXIMUM_TRIES - remaining_tries} intentos")
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {number_to_guess}")
