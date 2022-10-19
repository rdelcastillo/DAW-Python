"""
Imprimimos por pantalla los cien primeros números pares usando while.

ALGORITMO
    VAR n (ENTERO)

    pair <-- 0
    MIENTRAS pair < 100
        pair <-- pair + 1
        ESCRIBIR pair * 2
    FIN-MIENTRAS

Fecha: 20/10/2021
Autor: Rafael del Castillo
"""

NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

num_par = 1
while num_par <= NUM_PAIRS:
    print(f"Par número {num_par: 3}: {num_par * 2: 3}")
    num_par += 1
