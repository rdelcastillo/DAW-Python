"""
Imprimimos por pantalla los cien primeros números pares usando for.

ALGORITMO
    VAR n (ENTERO)

    PARA pair <-- 1 HASTA 100
        ESCRIBIR pair * 2
    FIN-PARA

Fecha: 26/10/2021
Autor: Rafael del Castillo
"""

NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

for num_par in range(NUM_PAIRS):
    par = (num_par + 1) * 2
    print(f"Par número {num_par+1: 3}: {par: 3}")
