"""
Muestra 50 números enteros aleatorios entre 100 y 199 (ambos incluidos) separados por espacios.
Muestra también el máximo, el mínimo, la moda, la media, la mediana y la desviación típica de esos números.

Usamos el módulo statistics y hacemos alguna mejora del anterior.
"""

import random
import statistics as stats

# Funciones
def numeros_aleatorios(rango_inicial, rango_final, cantidad):
    """
    Genera números aleatorios y los almacena dentro de una lista enviada como parámetro.

    Parámetros:
    * rango_inicial: valor mínimo del número aleatorio a generar.
    * rango_final: valor máximo del número aleatorio a generar.
    * cantidad: cantidad de números aleatorios a generar

    Devuelve: lista donde se guardan los números aleatorios.
    """
    numeros = []
    for i in range(cantidad):
        numeros.append(random.randint(rango_inicial, rango_final))
    return numeros

def moda(numeros):
    """
    Calcula las modas de la lista pasada como parámetro.

    Parámetros:
    * numeros: lista de números.

    Devuelve:
    * modas: lista con las modas

    Notas:
    * En el módulo statiscs hay una función para el cálculo de la moda, pero solo sirve si es única.
    * Mejoramos la actualización de frecuencias usando el método count que nos dice cuántas veces aparece un elemento en una lista.
    """

    modas = []          # vector para guardar las modas
    # Cálculo frecuencia máxima de aparición
    f_max = 0
    for n in numeros:
        if numeros.count(n) > f_max:
            f_max = numeros.count(n)
    # Meto las modas en la lista modas: reviso cada número, si no está en la lista comprueba si su frecuencia de aparición
    # es igual a f_max
    for n in numeros:
        if n not in modas and numeros.count(n)==f_max:
            modas.append(n)
    return modas

# Programa Principal

# Constantes
NUM = 50            # Cantidad de números aleatorios generados
RANGO_INICIAL = 100 # Rango de números aleatorios generados
RANGO_FINAL = 199

# Proceso
numeros = numeros_aleatorios(RANGO_INICIAL, RANGO_FINAL, NUM)
maximo = max(numeros)
minimo = min(numeros)
media = stats.mean(numeros)
mediana = stats.median(numeros)
desvt = stats.stdev(numeros)
modas = moda(numeros)

# Mostrar resultados
print("Números generados:", numeros)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación típica:", desvt)
print("Moda(s):", modas)
