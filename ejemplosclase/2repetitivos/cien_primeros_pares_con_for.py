"""
Imprimimos por pantalla los cien primeros números pares usando for.

ALGORITMO
    VAR n (ENTERO)

    PARA num_par <-- 1 HASTA 100
        ESCRIBIR num_par * 2
    FIN-PARA

Fecha: 26/10/2021
Autor: Rafael del Castillo
"""

NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

for num_par in range(1, NUM_PAIRS+1):
    print(f"Par número {num_par: 3}: {num_par * 2: 3}")
