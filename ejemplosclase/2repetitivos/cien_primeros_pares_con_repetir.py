"""
Imprimimos por pantalla los cien primeros números pares usando REPETIR.

ALGORITMO
    VAR n (ENTERO)

    n <-- 0
    REPETIR
        n <-- n + 1
        ESCRIBIR n * 2
    HASTA QUE n = 100

En Python no existe el ciclo REPETIR por lo que voy a tener que simularlo.

Fecha: 20/10/2021
Autor: Rafael del Castillo
"""
NUM_PARES = 100

print(f"Primeros {NUM_PARES} números pares")
print("--------------------------")

n = 0
while True:
    n += 1
    print(f"Par número {n:03}: {n * 2}")    # El 0 es para que salga "001" en vez de "  1"
    if n == NUM_PARES:
        break
