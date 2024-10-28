"""
Imprimimos por pantalla los cien primeros números pares usando while.

ALGORITMO
    VAR n (ENTERO)

    num_par <-- 0
    MIENTRAS num_par < 100
        num_par <-- num_par + 1
        ESCRIBIR num_par * 2
    FIN-MIENTRAS

Fecha: 20/10/2021
Autor: Rafael del Castillo
"""

NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

num_par = 0
while num_par < NUM_PAIRS:
    num_par += 1
    print(f"Par número {num_par: 3}: {num_par * 2: 3}")
