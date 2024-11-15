"""
Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.

Esta versión funcionará durante 24 horas.
"""

import time

# Proceso
for hours in range(24):  # desde las 0 horas a las 23
    for minutes in range(60):  # desde el minuto 0 al 59
        for seconds in range(60):  # desde el segundo 0 al 59
            print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="")
            time.sleep(1)  # esperamos un segundo
