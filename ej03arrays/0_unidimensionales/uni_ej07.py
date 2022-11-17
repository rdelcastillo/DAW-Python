"""
Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los
elementos de ese array, es decir, el elemento de la posición 0 debe pasar a la posición 1,
el de la 1 a la 2, etc. El número que se encuentra en la última posición debe pasar a la
posición 0. Finalmente, muestra el contenido del array.

Ejercicio sacado del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

Created on 27 nov. 2018.

@author: Rafael del Castillo
"""

TOTAL_NUMBERS = 15  
numbers = list()

# Pedimos los datos
print("Vaya introduciendo números enteros y pulsando INTRO:")
for i in range(TOTAL_NUMBERS):
    numbers.append(int(input()))
print("\nLista original:", numbers)

# Rotamos una posición a la derecha
aux = numbers[-1]
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]
numbers[0] = aux
print("\nLista rotada una posición a la derecha:", numbers)
