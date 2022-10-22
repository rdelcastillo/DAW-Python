"""
Programa que muestra un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.
"""

import time

# Inicializamos
hours = 0
minutes = 0
seconds = 0

# Proceso
# hacemos un ciclo infinito y esperamos 1 segundo cada iteración
while True:
    # escribimos el time actual en la pantalla
    # en el print usamos:
    #   - 02 para que el time ocupe dos lugares y se rellene con ceros
    #   - flush=True para forzar a que el buffer de pantalla se escriba
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)

    time.sleep(1)   # espera de un segundo

    # pasamos al siguiente segundo
    seconds += 1
    # ¿Me he pasado de segundos?
    if seconds == 60:   # vamos al siguiente minuto
        seconds = 0
        minutes += 1
        # ¿Me he pasado de minutos?
        if minutes == 60:
            minutes = 0
            hours += 1  # vamos a la hora siguiente

    # ponemos el cursor al principio de la línea
    print(8 * "\b", end="")  # \b desplaza el cursor a la izquierda
