"""
En este programa le vamos a preguntar al usuario algo a lo que debe contestar S o N y si contesta mal
hay que advertirle.

No sería eficiente un ciclo precondición ni uno postcondición.
"""

while True:
    resp = input("Contesta S o N: ").upper()
    if resp == 'S' or resp == 'N':
        break
    print("Tienes que introducir 'S' o 'N'")

print("Has contestado:", resp)