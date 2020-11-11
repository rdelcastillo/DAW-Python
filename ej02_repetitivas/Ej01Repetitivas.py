"""
Aplicación que permita adivinar un número.

La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo
si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan
(hay 10 intentos para acertarlo).

El programa termina cuando se acierta el número (además dice en cuantos intentos se ha acertado),
si se llega al límite de intentos muestra el número que había generado.

Fecha: 10/11/2020.

Autores: Clase de 1ºDAW. Idea original de Sergio Vera.
-------------------------------------------------------------------------------------------------------------
Variables a usar:

- numero_a_adivinar
- numero_introducido    (número introducido por el usuario)
- intentos_que_quedan

Algoritmo:

numero_a_adivinar <-- Aleatorio entre 1 y 100
intentos_que_quedan <-- 10

REPETIR
    LEER numero_introducido
    SI numero_introducido < numero_a_adivinar
        ESCRIBIR numero_introducido, " es menor que el número a adivinar"
    SINO
        SI numero_introducido > numero_a_adivinar
            ESCRIBIR numero_introducido, " es mayor que el número a adivinar"
        FIN-SI
    FIN-SI
    intentos_que_quedan <-- intentos_que_quedan -1
HASTA QUE intentos_que_quedan=0 O numero_a_adivinar=numero_introducido

SI numero_a_adivinar = numero_introducido
    ESCRIBIR "Acertaste en ", 10-intentos_que_quedan, "intentos"
SINO
    ESCRIBIR "No lo adivinaste, era ", numero_a_adivinar
FIN-SI
"""

import random

# Inicializamos
numero_a_adivinar = random.randint(1, 100)
intentos_que_quedan = 10

# Proceso
while True:  # implementación ciclo postcondición REPETIR
    numero_introducido = int(input(f"Te quedan {intentos_que_quedan} intentos. Introduce un número entre 1 y 100: "))

    # pista (si no acierta) para que le sea más fácil adivinar
    if numero_introducido < numero_a_adivinar:
        print(f"{numero_introducido} es menor que el número a adivinar.")
    elif numero_introducido > numero_a_adivinar:
        print(f"{numero_introducido} es mayor que el número a adivinar.")

    intentos_que_quedan -= 1    # hemos consumido un intento

    # salida ciclo
    if numero_introducido == numero_a_adivinar or intentos_que_quedan == 0:  # acabo si adivino o supero los intentos
        break

# Mostramos si acertó o no
if numero_introducido == numero_a_adivinar:  # ha adivinado
    print(f"Has adivinado el número en {10 - intentos_que_quedan} intentos")
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {numero_a_adivinar}")
