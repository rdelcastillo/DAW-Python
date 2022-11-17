"""
Programa que pide 10 números por teclado y los muestre junto con las palabras “máximo” y “mínimo” al lado
del máximo y del mínimo respectivamente.

@author Rafael del Castillo Gomariz

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

"""

# Creamos lista que hará de vector de 10 elementos
numeros = [None]*10

# Pedimos datos
print("Introduzca 10 números enteros y pulse INTRO:")
for i in range(10):
    numeros[i] = int(input())

# Calculamos máximo y mínimo, observa que no es necesario hacerlo en el ciclo anterior
maximo = max(numeros)
minimo = min(numeros)

# Mostramos resultado
print()
for i in range(10):
    print(numeros[i],end=" ")
    if numeros[i] == maximo:
        print("máximo ",end=" ")
    if numeros[i] == minimo:
        print("mínimo ",end=" ")