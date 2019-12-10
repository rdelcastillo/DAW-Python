'''
Programa que rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000
(ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

@author Rafael del Castillo Gomariz

Ejercicio del libro "Aprende Java con Ejercicios. Edición 2018" (https://leanpub.com/aprendejava)

'''
import sys
import time
import random

# creamos array (lista) vacío de 6 filas por 10 columnas usando 
# "listas por comprensión", ver https://bit.ly/2Ga1MNv y https://bit.ly/2QncHrJ
# equivalente en Java a "int[][] numeros = new int[6][10]"

numeros = [[None] * 10 for i in range(6)]

minimo = sys.maxsize
fila_minimo = 0
columna_minimo = 0

maximo = (-sys.maxsize-1)
fila_maximo = 0
columna_maximo = 0

print("\n      ",end="")
for columna in range(10):
    print(f"   {columna}  ",end="")
print()

print("    ┌",end="")
for columna in range(10):
    print("──────",end="")
print("┐")

for fila in range(6):
    print(f"  {fila} │",end="")
    for columna in range(10):
        numeros[fila][columna] = int(random.random() * 1001)
        print("%5d "%(numeros[fila][columna]),end="")
        time.sleep(0.1)
        
        # Calcula el mínimo y guarda sus coordenadas
        if numeros[fila][columna] < minimo:
            minimo = numeros[fila][columna]
            fila_minimo = fila
            columna_minimo = columna
        # Calcula el máximo y guarda sus coordenadas
        if numeros[fila][columna] > maximo:
            maximo = numeros[fila][columna]
            fila_maximo = fila
            columna_maximo = columna
    print("│")
print("    └",end="")
for columna in range(10):
    print("──────",end="")
print(f"┘\n\nEl máximo es {maximo} y está en la fila {fila_maximo}, columna {columna_maximo}")
print(f"El mínimo es {minimo} y está en la fila {fila_minimo}, columna {columna_minimo}")
