# Tres en raya contra el ordenador
#
# Usaremos como tablero una tabla de 3x3 donde en cada celda tenemos:
#   0: vacía
#   1: ocupada por jugador
#   2: ocupada por ordenador
#
# Autor: Rafael del Castillo

# ---------
# FUNCIONES
# ---------

import random

def dibuja(tablero):
    borra_pantalla()
    print("----------")
    for i in range(3):
        print("|",end="")
        for j in range(3):
            if tablero[i][j]==0:
                print("  |",end="")
            else:
                print(tablero[i][j],"|",end="")
        print("\n----------")
# ------

def ganador(tablero):
    # filas
    for i in range(3):
        if tresenraya_fila(i,tablero):
            return tablero[i][0]
    # columnas
    for j in range(3):
        if tresenraya_columna(j,tablero):
            return tablero[i][0]
    # diagonales
    if tresenraya_diagonal1(tablero):
        return tablero[0][0]
    elif tresenraya_diagonal2(tablero):
        return tablero[0][2]
    else:
        return 0
# -----

def jugada(turno,tablero):
    if turno==1:
        juega_persona(tablero)
    else:
        juega_ordenador(tablero)
# -----

def siguiente_turno(turno):
    if turno==1:
        return 2
    else:
        return 1

# --------------------
# Funciones auxiliares
# --------------------

def borra_pantalla():
    import os
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("<-No se pudo borrar la pantalla->")
# -----

def tresenraya_fila(i,tablero):
    if tablero[i][0]!=0 and (tablero[i][0]==tablero[i][1]==tablero[i][2]):
        return True
    else:
        return False

def tresenraya_columna(j,tablero):
    if tablero[0][j]!=0 and (tablero[0][j]==tablero[1][j]==tablero[2][j]):
        return True
    else:
        return False

def tresenraya_diagonal1(tablero):
    if tablero[0][0]!=0 and (tablero[0][0]==tablero[1][1]==tablero[2][2]):
        return True
    else:
        return False

def tresenraya_diagonal2(tablero):
    if tablero[0][2]!=0 and (tablero[0][2]==tablero[1][1]==tablero[2][0]):
        return True
    else:
        return False
# -----

def juega_persona(tablero):
    # pedimos datos
    fila=int(input("\nDame la fila: "))
    columna=int(input("\nDame la columna: "))
    while incorrecta(fila,columna,tablero):
        print("Has puesto valores incorrectos\n\n")
        fila=int(input("\nDame la fila CORRECTA: "))
        columna=int(input("Dame la columna CORRECTA: "))

    # colocamos en tablero
    tablero[fila-1][columna-1]=1    # quitamos 1 por empezar en índice 0

def juega_ordenador(tablero):
    # generamos datos
    fila=random.randint(1,3)
    columna=random.randint(1,3)
    while incorrecta(fila,columna,tablero):
        fila=random.randint(1,3)
        columna=random.randint(1,3)

    # colocamos en tablero
    tablero[fila-1][columna-1]=2    # quitamos 1 por empezar en índice 0

def incorrecta(f,c,tablero):
    if f<1 or f>3 or c<1 or c>3 or tablero[f-1][c-1]!=0:
        return True
    else:
        return False

#----------------------------------------------------------------------
# PRINCIPAL
# ---------------------------------------------------------------------

# inicializamos
JUGADAS_MAXIMAS=9
jugadas=0
tablero = [[0,0,0],[0,0,0],[0,0,0]]
turno = random.randint(1,2) # turno 1 para jugador, 2 para ordenador

# proceso
dibuja(tablero)
while jugadas<JUGADAS_MAXIMAS and ganador(tablero)==0:
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
