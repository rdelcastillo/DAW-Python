"""
Imprimimos por pantalla los cien primeros números pares usando DO-WHILE.

ALGORITMO
    VAR n (ENTERO)

    n <-- 0
    DO
        n <-- n + 1
        ESCRIBIR n * 2
    WHILE n < 100

En Python no existe el ciclo DO-WHILE por lo que voy a tener que simularlo.

Fecha: 20/10/2021
Autor: Rafael del Castillo
"""
NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

n = 0
while True:
    n += 1
    print(f"Par número {n:03}: {n * 2}")    # El 0 es para que salga "001" en vez de "  1"
    if not n < NUM_PAIRS:
        break
