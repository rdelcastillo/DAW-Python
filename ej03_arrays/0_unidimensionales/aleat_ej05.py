"""
Muestra 50 números enteros aleatorios entre 100 y 199 (ambos incluidos) separados por espacios.
Muestra también el máximo, el mínimo, la moda, la media, la mediana y la desviación típica de esos números.

Algoritmo:

* Para la moda usaré un vector con las 100 posibilidades de número aleatorio
* Ejemplo: salen los números aleatorios 103,105,102,103,103,103,199
* En modas[0] (que se corresponde al número 100) habrá un 0 porque no ha salido 100
* En modas[1] (que se corresponde al número 101) habrá un 0 porque no ha salido 101
* En modas[2] (que se corresponde al número 102) habrá un 1 porque no ha salido 102 ha salido una vez
* En modas[3] (que se corresponde al número 103) habrá un 4 porque no ha salido 103 ha salido cuatro veces
* ...
* Mi moda será 103 porque modas[3] es el máximo del vector modas y la posición 3 equivale a 103

* Inicializamos
sumatorio <-- 0
maximo <-- 100
minimo <-- 199
frecuencia_maxima <-- 0
frecuencias[1..100] <-- 0  * inicializo a cero los elementos de cada posibilidad

* Generación números aleatorios, cálculo de media, máximo, mínimo
PARA i DESDE 0 HASTA 49
    n <-- aleatorio(100,199)
    numeros[i] <-- n
    sumatorio <-- sumatorio + n
    frecuencias[n-100] <-- modas[n-100] + 1
    SI frecuencias[n-100] > frecuencia_maxima ENTONCES
        frecuencia_maxima <-- modas[n-100]
    FIN-SI
    SI n<minimo ENTONCES
        minimo <-- n
    FIN-SI
    SI n>maximo ENTONCES
        maximo <-- n
    FIN-SI
FIN-PARA
media <-- sumatorio/50

* Cálculo mediana

Ordenar(numeros)
mediana <-- (numeros[24]+numeros[25]) / 2

* Cálculo varianza
sumatorio <-- 0
PARA i DESDE 0 HASTA 49
    sumatorio <-- sumatorio + (n-media)^2
FIN-PARA
desviaciont <-- RAIZ.CUADRADA(sumatorio/50)

* Mostrar resultados
ESCRIBIR maximo,minimo,moda,media,mediana,varianza
"""

import random
import math

# Constantes
NUM = 10
RANGO_INICIAL = 1
RANGO_FINAL = 5

# Inicializamos
sumatorio = 0
frecuencia_maxima = 0
maximo = RANGO_INICIAL
minimo = RANGO_FINAL
frecuencias=[0] * (RANGO_FINAL-RANGO_INICIAL+1)     # creo array(lista) de tamaño 100 (RANGO_FINAL-RANGO_INICIAL+1)
numeros=[0] * NUM                                   # creo array(lista) de tamaño 50 (NUM)

# Generación números aleatorios, cálculo de media, máximo, mínimo
for i in range(0,NUM):
    n = random.randint(RANGO_INICIAL,RANGO_FINAL)   # genero aleatorio
    numeros[i] = n  # añado a array
    sumatorio += n
    # frecuencias aparición y frecuencia máxima
    frecuencias[n - RANGO_INICIAL] += 1   # actualizo frecuencia de aparición de n
    if frecuencia_maxima < frecuencias[n - RANGO_INICIAL]:
        frecuencia_maxima = frecuencias[n - RANGO_INICIAL]
    # actualizo mínimo y máximo
    if n<minimo:
        minimo = n
    if n>maximo:
        maximo = n
media = sumatorio/NUM

# Cálculo mediana
numeros.sort()  # Ordenar(numeros)
mediana = (numeros[NUM//2 -1]+numeros[NUM//2]) / 2    # media elementos centrales

# Cálculo desviación típica
sumatorio = 0
for i in range(0, NUM):
    sumatorio += (n-media)**2
desviaciont = math.sqrt(sumatorio/NUM)

# Mostrar resultados
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación típica:", desviaciont)
print("Moda: ", end="")
for i in range(0, len(frecuencias)):
    if frecuencias[i]==frecuencia_maxima:   # he encontrado una moda
        print(i+RANGO_INICIAL, end=" ")
print()