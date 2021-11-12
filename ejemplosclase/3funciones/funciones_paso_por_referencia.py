"""
Paso de parámetros por referencia a una función.

Listas.
"""

def suma_n(l,v):
    for i in range(0,len(l)):
        l[i] += v

lista = [1,2,3,4,5,6,7,8,9,10]
print("Lista inicial:", lista)
n = int(input("¿Cuanto le sumo? "))
suma_n(lista,n)
print("\nLa lista después de sumarle", n, lista)
print(lista)