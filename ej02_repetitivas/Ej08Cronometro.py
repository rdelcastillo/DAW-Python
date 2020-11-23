"""
Programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.
"""

import time

# Inicializamos
horas = 0
minutos = 0
segundos = 0

# Proceso
# hacemos un ciclo infinito y esperamos 1 segundo cada iteración
while True:
    # escribimos el tiempo actual en la pantalla
    # en el print usamos:
    #   - 02 para que el tiempo ocupe dos lugares y se rellene con ceros
    #   - flush=True para forzar a que el buffer de pantalla se escriba
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)

    time.sleep(1)   # espera de un segundo

    # pasamos al siguiente segundo
    segundos += 1
    # ¿Me he pasado de segundos?
    if segundos == 60:   # vamos al siguiente minuto
        segundos = 0
        minutos += 1
        # ¿Me he pasado de minutos?
        if minutos == 60:
            minutos = 0
            horas += 1  # vamos a la hora siguiente

    # ponemos el cursor al principio de la línea
    print(8 * "\b", end="")  # \b desplaza el cursor a la izquierda

