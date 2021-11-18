"""
Imprimimos por pantalla los cien primeros números pares usando for.

ALGORITMO
    VAR n (ENTERO)

    PARA par <-- 2 HASTA 200 INCREMENTO 2
        ESCRIBIR num_par
    FIN-PARA

Fecha: 26/10/2021
Autor: Rafael del Castillo
"""

NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

for par in range(2, 2*NUM_PAIRS+1, 2):
    print(f"Par número {par//2: 3}: {par: 3}")
