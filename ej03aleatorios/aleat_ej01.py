"""
Programa que muestra tres apuestas de la quiniela en tres columnas para los 14 partidos y el pleno al quince (15 filas)
de forma que la probabilidad de que salga un 1 sea  de 1/2, la probabilidad de que salga x sea de 1/3 y la probabilidad
de que salga 2 sea de 1/6.

Pista: 1/2 = 3/6 y 1/3 = 2/6.
"""

import random

columnas = 3
for fila in range(1, 16): # 15 iteraciones (de 1 a 15)
    print(f"{fila:4}. |", end="")
    if fila==15:
        columnas = 1
    for apuesta in range(columnas): # 3 apuestas (3 columnas) salvo el pleno al 15
        resultado_partido = random.randint(1,6)
        if resultado_partido==1 or resultado_partido==2 or resultado_partido==3:
            print("1  |", end="")
        elif resultado_partido==4 or resultado_partido==5:
            print(" X |", end="")
        else:
            print("  2|", end="")
    print()
