"""
FUNCIONES para el programa tresenraya

Autor: Rafael del Castillo Gomariz
"""
import random

def dibuja(tablero):
    """Dibuja el tablero de 3x3 en pantalla.

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
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
    """Devuelve el ganador, en caso de que lo haya.

    Valores devueltos:
        0 - no hay ganador
        1 - gana el jugador
        2 - gana el ordenador

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    # filas
    for i in range(3):
        if tresenraya_fila(i,tablero):
            return tablero[i][0]
    # columnas
    for j in range(3):
        if tresenraya_columna(j,tablero):
            return tablero[0][j]
    # diagonales
    if tresenraya_diagonal1(tablero):
        return tablero[0][0]
    elif tresenraya_diagonal2(tablero):
        return tablero[0][2]
    else:
        return 0
# -----

def jugada(turno,tablero):
    """Realiza la jugada del jugador o del ordenador.

    Parámetros:
    turno -
        1 si es el turno del jugador
        2 si es el turno del ordenador
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    if turno==1:
        juega_persona(tablero)
    else:
        juega_ordenador(tablero)
# -----

def siguiente_turno(turno):
    """Devuelve el jugador que juega el siguiente turno.

    Valores devueltos: 1 ó 2

    Parámetros:
    turno -
        1 si es el turno del jugador
        2 si es el turno del ordenador

    """
    if turno==1:
        return 2
    else:
        return 1

# --------------------
# Funciones auxiliares
# --------------------

def borra_pantalla():
    """Borra la pantalla teniendo en cuenta el sistema operativo.

    Usada por dibuja()

    """
    import os
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("<-No se pudo borrar la pantalla->")
# -----

def tresenraya_fila(i,tablero):
    """Comprueba si hay tres en raya en la fila indicada.

    Usada por ganador() y dosenraya()

    Valores devueltos: True ó False

    Parámetros:
    i - fila
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    return tablero[i][0]!=0 and (tablero[i][0]==tablero[i][1]==tablero[i][2])

def tresenraya_columna(j,tablero):
    """Comprueba si hay tres en raya en la columna indicada.

    Usada por ganador() y dosenraya()

    Valores devueltos: True ó False

    Parámetros:
    j - columna
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    return tablero[0][j]!=0 and (tablero[0][j]==tablero[1][j]==tablero[2][j])

def tresenraya_diagonal1(tablero):
    """Comprueba si hay tres en raya en la diagonal de izquierda a derecha.

    Usada por ganador() y dosenraya()

    Valores devueltos: True ó False

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    return tablero[0][0]!=0 and (tablero[0][0]==tablero[1][1]==tablero[2][2])

def tresenraya_diagonal2(tablero):
    """Comprueba si hay tres en raya en la diagonal de derecha a izquierda.

    Usada por ganador() y dosenraya()

    Valores devueltos: True ó False

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    return tablero[0][2]!=0 and (tablero[0][2]==tablero[1][1]==tablero[2][0])
# -----

def juega_persona(tablero):
    """Realiza la jugada del jugador 'persona'.

    Usada por jugada()

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    # pedimos datos
    fila=int(input("\nDame la fila: "))
    columna=int(input("Dame la columna: "))
    while incorrecta(fila,columna,tablero):
        print("\nHas puesto valores incorrectos\n")
        fila=int(input("\nDame la fila CORRECTA: "))
        columna=int(input("Dame la columna CORRECTA: "))

    # colocamos en tablero
    tablero[fila-1][columna-1]=1    # quitamos 1 por empezar en índice 0

def juega_ordenador(tablero):
    """Realiza la jugada del jugador 'ordenador'.

    Usada por jugada()

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    # ¿podemos ganar? Buscamos fila, columna o diagonal con dos 2 y un 0
    fila,columna = dosenraya(tablero,2) # devolverá 0,0 si no podemos ganar
    if fila==0:
        # ¿podemos perder? Buscamos fila, columna o diagonal con dos 1 y un 0
        fila,columna = dosenraya(tablero,1) # devolverá 0,0 si no estamos a punto de perder
        if fila==0:
            # generamos datos
            fila=random.randint(1,3)
            columna=random.randint(1,3)
            while incorrecta(fila,columna,tablero):
                fila=random.randint(1,3)
                columna=random.randint(1,3)

    # colocamos en tablero
    tablero[fila-1][columna-1]=2    # quitamos 1 por empezar en índice 0

def incorrecta(f,c,tablero):
    """Indica si la jugada es incorrecta.

    Usada por juega_persona() y juega_ordenador()

    Valores devueltos: True ó False

    Parámetros:
    f - fila de la casilla escogida
    c - columna de la casilla escogida
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador

    """
    return f<1 or f>3 or c<1 or c>3 or tablero[f-1][c-1]!=0

def dosenraya(tablero,jugador):
    """Comprueba si hay alguna jugada que puede hacer ganar a "jugador".

    Usada por juega_ordenador()

    Valores devueltos: Fila y Columna (entre 1 y 3), si no hay jugada devuelve 0,0

    Parámetros:
    tablero - lista de 3x3 casillas donde:
        0 es una casilla vacía (aparece blanco)
        1 es una casilla ocupada por el jugador
        2 es una casilla ocupada por el ordenador
    jugador - 1 si es la persona y 2 si es el ordenador

    La manera de proceder será:
        - crear una copia del tablero
        - comprobar cada fila, si hay un cero lo cambiamos por 'jugador'
            * si hay tres en raya en esa fila acabamos
        - lo mismo para las columnas y diagonales

    """
    # copiamos tablero en tablero_auxiliar
    # consultar: http://elclubdelautodidacta.es/wp/2012/09/python-como-copiar-una-lista/
    from copy import deepcopy
    tablero_auxiliar=deepcopy(tablero)

    # comprobamos filas
    for i in range(3):
        j=0
        while j<3 and tablero_auxiliar[i][j]!=0:    # buscamos celda libre
            j+=1
        if j<3: # hay casilla libre, probamos
            tablero_auxiliar[i][j]=jugador
            if tresenraya_fila(i,tablero_auxiliar):
                return i+1,j+1
            else:
                tablero_auxiliar[i][j]=0    # dejamos como estaba

    # comprobamos columnas
    for j in range(3):
        i=0
        while i<3 and tablero_auxiliar[i][j]!=0:    # buscamos celda libre
            i+=1
        if i<3: # hay casilla libre, probamos
            tablero_auxiliar[i][j]=jugador
            if tresenraya_columna(j,tablero_auxiliar):
                return i+1,j+1
            else:
                tablero_auxiliar[i][j]=0    # dejamos como estaba

    # comprobamos diagonal izquierda a derecha
    i=0
    while i<3 and tablero_auxiliar[i][i]!=0:    # buscamos celda libre
        i+=1
    if i<3: # hay casilla libre, probamos
        tablero_auxiliar[i][i]=jugador
        if tresenraya_diagonal1(tablero_auxiliar):
            return i+1,i+1
        else:
            tablero_auxiliar[i][i]=0    # dejamos como estaba

    # comprobamos diagonal derecha a izquierda
    i=0
    while i<3 and tablero_auxiliar[i][2-i]!=0:    # buscamos celda libre
        i+=1
    if i<3: # hay casilla libre, probamos
        tablero_auxiliar[i][2-i]=jugador
        if tresenraya_diagonal2(tablero_auxiliar):
            return i+1,2-i+1
        else:
            tablero_auxiliar[i][2-i]=0    # dejamos como estaba

    # si llegamos aquí es que no hemos devuelto nada, no hay jugada
    return 0,0

