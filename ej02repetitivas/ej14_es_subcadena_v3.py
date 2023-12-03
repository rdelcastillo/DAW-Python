"""
Comprobamos si hay una subcadena dentro de una cadena usando ciclos y obviando los métodos de Python
para ello.

Programa anterior sin slices.
"""

# Pedimos datos
user_string = input("Dame una cadena: ")
user_substring = input(f"Dame una subcadena de '{user_string}': ")

# Proceso de búsqueda de la subcadena
is_substring = False
last_index_to_check = len(user_string) - len(user_substring) + 1
for index in range(last_index_to_check):
    # creamos una subcadena de la cadena original desde index hasta index + longitud subcadena a buscar
    substring_user_string = ""
    for i in range(index, index + len(user_substring)):
        substring_user_string += user_string[i]

    # comprobamos si la subcadena candidata coincide con la subcadena a buscar, en ese caso acabamos
    if user_substring == substring_user_string:
        is_substring = True
        break

# Mostramos resultado
if is_substring:
    print("Muy bien")
else:
    print(f"Me estás engañando '{user_substring}' no forma parte de '{user_string}'")
