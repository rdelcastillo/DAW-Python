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
    print(f"{horas:02}:{minutos:02}:{segundos:02}", end="")  # 02 para ocupar dos lugares y rellenar con ceros
    time.sleep(1)
    # pasar al siguiente segundo
    if segundos < 59:
        segundos += 1
    else:
        segundos = 0
        if minutos < 59:
            minutos += 1
        else:
            minutos = 0
            horas += 1
    # ponemos el cursor al principio de la línea
    print(8 * "\b", end="")  # \b desplaza el cursor a la izquierda
