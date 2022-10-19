"""
Imprimimos por pantalla los cien primeros números pares (hasta 200) usando REPETIR.

ALGORITMO
    VAR pair (ENTERO)

    par <-- 2
    REPETIR
        ESCRIBIR par
        par <-- par + 2
    HASTA QUE par > 200

En Python no existe el ciclo REPETIR por lo que voy a tener que simularlo.

Fecha: 19/10/2022
Autor: Rafael del Castillo
"""
LAST_PAIR = 200

print(f"Primeros {LAST_PAIR // 2} números pares")
print("--------------------------")

pair = 2
while True:
    print(f"Par número {pair // 2:03}: {pair}")    # El 0 es para que salga "001" en vez de "  1"
    pair += 2
    if pair > LAST_PAIR:
        break
