'''
Modicación del programa anterior de forma que no se repita ningún número en el array.
 
@author Rafael del Castillo Gomariz

Ejercicio del libro "Aprende Java con Ejercicios" (https://leanpub.com/aprendejava)

'''
import sys
import random
import time

numeros = [[None] * 10 for i in range(6)]

# Genera el contenido del array sin que se repita ningún valor
for fila in range(6): 
    for columna in range(10): 
        while True:
            numeros[fila][columna] = int(random.random() * 1001)
            # Comprueba si el número generado ya está en el array.
            repetido = False
            for i in range(10 * fila + columna):
                if numeros[fila][columna] == numeros[i // 10][i % 10]:
                    repetido = True
            if not (repetido): break

# Proceso            
minimo = sys.maxsize
fila_minimo = 0
columna_minimo = 0

maximo = -sys.maxsize-1
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
