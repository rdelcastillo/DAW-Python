# Tres en raya contra el ordenador
#
# Usaremos como tablero una tabla de 3x3 donde en cada celda tenemos:
#   0: vacía
#   1: ocupada por jugador
#   2: ocupada por ordenador
#
# Autor: Rafael del Castillo

from funciones_tresenraya import *

# inicializamos
JUGADAS_MAXIMAS=9   # si hay estas jugadas y nadie gana se produce un empate
jugadas=0
tablero = [[0,0,0],[0,0,0],[0,0,0]]
turno = random.randint(1,2) # turno 1 para jugador, 2 para ordenador

# proceso
dibuja(tablero)
while jugadas<JUGADAS_MAXIMAS and not ganador(tablero):
    jugada(turno,tablero)
    jugadas+=1
    dibuja(tablero)
    turno=siguiente_turno(turno)

# final
ha_ganado=ganador(tablero)
if ha_ganado==1:
    print("¡¡¡Has ganado al ordenador!!!")
elif ha_ganado==2:
    print("Has perdido contra el ordenador")
else:
    print("Empate")
