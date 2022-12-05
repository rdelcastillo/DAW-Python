"""
Operaciones con arrays como listas de Python.
"""

import random

# Muestra el valor del elemento 6 de un array f.
f = [random.randint(0,100) for _ in range(10)]  # creamos lista con 10 valores aleatorios entre 0 y 100
print("Lista generada:", f)
print(f"Valor posición 6: {f[6]}\n")

# Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
for i in range(4):
    f[i] = 8
print("Lista después de cambiar el valor de los cinco primeros elementos a 8:", f, "\n")

# Total de los 100 elementos de punto-flotante de un array c.
c = [random.random() for _ in range(100)]  # creamos lista con 100 valores aleatorios entre 0 y 1
print("Lista generada:", c)
total = 0
for n in c:
    total += n
print("La suma total de sus elementos es ", total, "\n")  # podríamos habernos ahorrado el cálculo con sum[c]

# Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.
a = [random.randint(0,100) for _ in range(11)]
print("Lista a:", a)
b = [random.randint(0,100) for _ in range(34)]
print("Lista b:", b)
for i in range(len(a)):
    b[i] = a[i]
print("b después de copiar en sus primeras 11 posiciones los elementos de a:", b, "\n")

# Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante.
w = [random.random()*100 for _ in range(99)]  # creamos lista con 99 valores aleatorios reales entre 0 y 100
print("Lista generada:", w)
minimum = maximum = w[0]
for n in w[1:]:
    if n < minimum:
        minimum = n
    elif n > maximum:
        maximum = n
print("El mínimo de los valores es:", minimum)
print("El máximo de los valores es:", maximum)
