"""
En este programa le vamos a preguntar al usuario algo a lo que debe contestar S ó N.

Probamos con un ciclo postcondición.
"""

while True:
    resp = input("Contesta S ó N: ").upper()
    if resp == 'S' or resp == 'N':
        break

print("Has contestado:", resp)