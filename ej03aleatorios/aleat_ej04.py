import random

"""
Números aleatorios
 
Muestra 20 números enteros aleatorios entre 0 y 10 (ambos incluidos)
separados por espacios.
"""

for i in range(20):
    print(random.randint(0,10), end=" ")
print()
