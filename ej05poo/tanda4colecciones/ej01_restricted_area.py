"""
Ejemplo de control de acceso al área restringida de un programa.

Se debe pedir un nombre de usuario y una contraseña. Si el usuario introduce los datos correctamente, el programa dirá
“Ha accedido al área restringida”. El usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el
programa dirá “Lo siento, no tiene acceso al área restringida”.

Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados en un diccionario.

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""

MAX_ATTEMPTS = 3
USERS = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3', 'user4': 'password4', 'user5': 'password5'}

print("Acceso al área restringida")
print("--------------------------")

attempt = 0
access = False

while True:
    attempt += 1
    print(f"Introduzca los datos de acceso (intento {attempt}/{MAX_ATTEMPTS})")
    user = input("Usuario: ")
    if user in USERS:
        password = input("Contraseña: ")
        if USERS[user] == password:
            access = True
        else:
            print("Contraseña INCORRECTA")
    else:
        print("Usuario INCORRECTO")

    if access or attempt == MAX_ATTEMPTS:
        break

print("Ha ACCEDIDO al área restringida") if access else print("Lo siento, NO TIENE ACCESO al área restringida")
