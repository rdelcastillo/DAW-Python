"""
Comprobamos si hay una subcadena dentro de una cadena usando ciclos y obviando los métodos de Python
para ello.

Programa anterior hecho con for.
"""

# Pedimos datos
user_string = input("Dame una cadena: ")
user_substring = input(f"Dame una subcadena de '{user_string}': ")

# Proceso de búsqueda de la subcadena
is_substring = False
last_index_to_check = len(user_string) - len(user_substring) + 1
for index in range(last_index_to_check):
    if user_substring == user_string[index:index + len(user_substring)]:
        is_substring = True
        break

# Mostramos resultado
if is_substring:
    print("Muy bien")
else:
    print(f"Me estás engañando '{user_substring}' no forma parte de '{user_string}'")
