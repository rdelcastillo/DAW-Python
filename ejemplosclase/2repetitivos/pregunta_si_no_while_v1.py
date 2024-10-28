"""
En este programa le vamos a preguntar al usuario algo a lo que debe contestar S ó N.

Probamos con while.
"""

resp = input("Contesta S ó N: ").upper()
while resp != 'S' and resp != 'N':
    resp = input("Contesta S ó N: ").upper()

print("Has contestado:", resp)