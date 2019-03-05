'''
Programa que pide 20 números enteros.

Estos números se introducen en un array de 4 filas por 5 columnas.
El programa muestra las sumas parciales de filas y columnas igual que
si de una hoja de cálculo se tratara.
La suma total aparece en la esquina inferior derecha.

@author Rafael del Castillo
'''

num = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #array de F filas por C columnas
F = 4
C = 5

# Lee los datos de teclado
print("Por favor, introduzca los números (enteros) en el array:")
for fila in range(0,F):
    for columna in range(0,C):
        num[fila][columna] = int(input(f"Fila {fila} columna {columna}: "))

# Muestra los datos y las sumas parciales de las filas
for fila in range(0,F):
    suma_fila = 0;
    for columna in range(0,C):
        print("%7d   " %(num[fila][columna]),end="")
        suma_fila += num[fila][columna]
    print("|%7d" %(suma_fila))

# Muestra las sumas parciales de las columnas
for columna in range(0,C):
    print("----------",end="")
print("-----------")
sumaTotal = 0;
for columna in range(0,C):
    sumaColumna = 0;
    for fila in range(0,F):
        sumaColumna += num[fila][columna];
    sumaTotal += sumaColumna
    print("%7d   " %(sumaColumna),end="")
print("|%7d   " %(sumaTotal))


