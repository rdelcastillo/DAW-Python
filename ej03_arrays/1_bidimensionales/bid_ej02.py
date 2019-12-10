'''
Programa que pide 20 números enteros.

Modificación del ejercicio 2 de tal forma que los números que se introducen en
el array se generan de forma aleatoria (valores entre 100 y 999) y las sumas parciales
y la suma total aparecen en la pantalla con un pequeño retardo, dando la impresión de
que el ordenador se queda pensando antes de mostrar los números.

@author Rafael del Castillo

Ejercicio del libro "Aprende Java con Ejercicios" (https://leanpub.com/aprendejava)

'''
import time
import random

# creamos array (lista) vacío de 4 filas por 5 columnas
num = [None] * 4
for i in range(4):
    num[i] = [None] * 5

# Introduce valores aleatorios en el array
for fila in range(4):
    for columna in range(5):
        num[fila][columna] = int((random.random() * 900) + 100)

# Muestra los datos y las sumas parciales de las filas
for fila in range(4):
    suma_fila = 0
    for columna in range(5):
        print("%7d   "%(num[fila][columna]),end="")
        suma_fila += num[fila][columna]
        time.sleep(0.1)
    print("|%7d\n"%(suma_fila),end="")
    time.sleep(0.5) 
    
# Muestra las sumas parciales de las columnas
for columna in range(5):
    print("----------",end="")
print("-----------")

suma_total = 0

for columna in range(5):
    suma_columna = 0
    for fila in range(4):
        suma_columna += num[fila][columna]
    suma_total += suma_columna
    print("%7d   "%(suma_columna),end="")
    time.sleep(0.5)
print("|%7d   "%(suma_total),end="")
