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

TOTAL_PARES = 100

print(f"Primeros {TOTAL_PARES} números pares")
print("--------------------------")

num_par = 1
while num_par <= TOTAL_PARES:
    print(f"Par número {num_par: 3}: {num_par * 2: 3}")
    num_par += 1
