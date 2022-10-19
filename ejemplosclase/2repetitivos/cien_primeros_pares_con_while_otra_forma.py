"""
Imprimimos por pantalla los cien primeros números pares (hasta 200) usando while.

ALGORITMO
    VAR n (ENTERO)

    par <-- 2
    MIENTRAS par <= 200
        ESCRIBIR par
        par <-- par + 2
    FIN-MIENTRAS

Fecha: 19/10/2022
Autor: Rafael del Castillo
"""

LAST_PAIR = 200

print(f"Primeros {LAST_PAIR // 2} números pares")
print("--------------------------")

pair = 2
while pair <= LAST_PAIR:
    print(f"Par número {pair // 2: 3}: {pair: 3}")
    pair += 2
