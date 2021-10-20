"""
Imprimimos por pantalla los cien primeros números pares usando while.

ALGORITMO
    VAR n (ENTERO)

    n <-- 0
    MIENTRAS n < 100
        n <-- n + 1
        ESCRIBIR n * 2
    FIN-MIENTRAS

Fecha: 20/10/2021
Autor: Rafael del Castillo
"""
NUM_PARES = 100

print(f"Primeros {NUM_PARES} números pares")
print("--------------------------")

n = 0
while n < NUM_PARES:
    n += 1
    print(f"Par número {n:03}: {n * 2}")    # El 0 es para que salga "001" en vez de "  1"
