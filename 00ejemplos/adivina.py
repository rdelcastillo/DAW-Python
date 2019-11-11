'''
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

Variables a usar:

- n_adivinar
- n
- intentos
'''

import random

# Constantes
INTENTOS_MAXIMOS = 10

# Inicializamos
intentos = 0
n_adivinar = random.randrange(1,100)

# Proceso
while True:  # implementación ciclo postcondición
    n = int(input(  "Te quedan " + str(INTENTOS_MAXIMOS-intentos) +
                    " intentos. Introduce un número entre 1 y 100: "))
    intentos+=1
    if n < n_adivinar:
        print(f"{n} es menor que el número a adivinar.")
    elif n > n_adivinar:
        print(f"{n} es mayor que el número a adivinar.")
    # salida ciclo
    if n==n_adivinar or intentos==INTENTOS_MAXIMOS:
        # acabo si adivino o supero los intentos
        break

# Mostramos resultado
if n==n_adivinar: # ha adivinado
    print(f"Has adivinado el número en {intentos} intentos")
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {n_adivinar}")

