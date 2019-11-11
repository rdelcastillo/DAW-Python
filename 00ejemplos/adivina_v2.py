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
- intentos_que_quedan
'''

import random

# Constantes
INTENTOS_MAXIMOS = 3

# Inicializamos
intentos_que_quedan = INTENTOS_MAXIMOS
n_adivinar = random.randrange(1,100)

# Proceso

# implementamos un ciclo postcondición, ejecutamos la instrución
# antes de entrar en el ciclo y al final del ciclo.
n = int(input(  "Te quedan " + str(intentos_que_quedan) +
                " intentos. Introduce un número entre 1 y 100: "))
while n!=n_adivinar and intentos_que_quedan>0:
    intentos_que_quedan-=1
    if n < n_adivinar:
        print(f"{n} es menor que el número a adivinar.")
    else:
        print(f"{n} es mayor que el número a adivinar.")
    n = int(input(  "Te quedan " + str(intentos_que_quedan) +
                " intentos. Introduce un número entre 1 y 100: "))

# Mostramos resultado
if n==n_adivinar: # ha adivinado
    print(f"Has adivinado el número en {intentos} intentos")
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {n_adivinar}")

