import random

"""
Programa que "piensa" un número al azar entre 0 y 100. El usuario debe adivinarlo y tiene para ello 5 oportunidades. 
Después de cada intento fallido, el programa dirá cuántas oportunidades quedan y si el número introducido es menor o 
mayor que el que ha pensado.

Enunciado del ejercicio sacado del libro "Aprende Java con Ejercicios" (ejercicio 14 del tema 6, edición 2019)
de Luis José Sánchez.
"""

# Inicializamos
oportunidades = 5
minimo = 0
maximo = 100
acertado = False

# Mensaje inicio
print("Piensa un número del 0 al 100. Intentaré adivinarlo en 5 intentos.")
input("Pulsa la tecla INTRO cuando estés preparado.")

# Proceso
while True:
    numero_pensado = int(random.randint(minimo, maximo))
    print(f"¿Es el {numero_pensado}?")
    mayor_menor_o_igual = int(input("El número que estás pensando es 1-mayor / 2-menor /3-el mismo: "))
    oportunidades -= 1
    # ¿acierta?
    if mayor_menor_o_igual == 1:
        minimo = numero_pensado + 1
    elif mayor_menor_o_igual == 2:
        maximo = numero_pensado - 1
    elif mayor_menor_o_igual == 3:
        acertado = True
    else:
        print("No me has dado ninguna pista :-(")
    if not (not acertado and (oportunidades > 0)): break

# Fin
if acertado:
    print("¡Bien! ¡he acertado!")
else:
    print("Vaya, no he conseguido acertar el número.")
