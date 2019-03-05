'''
Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los
elementos de ese array, es decir, el elemento de la posición 0 debe pasar a la posición 1,
el de la 1 a la 2, etc. El número que se encuentra en la última posición debe pasar a la
posición 0. Finalmente, muestra el contenido del array.

Created on 27 nov. 2018

@author: rafa
'''
N = 15  #tamaño lista
# si creo la lista con 15 elementos
#numeros = list([None]*15)

# si creo lista vacía y voy añadiendo
numeros=list()

# pido datos
print("Vaya introduciendo números enteros y pulsando INTRO:")
for i in range(0,N):
    #numeros[i] = int(input())
    numeros.append(int(input()))

print()

# Muestra el array original
print("Array original:");
for i in range(0,15):
    print("|%3d "%(i),end="")
print("|\n","⎯"*75,end="")
print("⎯");
for n in numeros:
    print("|%3d "%(n),end="")
print("|")

# rota una posición a la derecha //////////
aux = numeros[-1]
for i in range(len(numeros)-1,0,-1):
    numeros[i] = numeros[i-1]
numeros[0] = aux;

# Muestra el array rotado 
print("\nArray rotado a la derecha una posición:")
for i in range(0,15):
    print("|%3d "%(i),end="")
print("|\n","⎯"*75)
for n in numeros:
    print("|%3d "%(n),end="")
print("|",end="")



