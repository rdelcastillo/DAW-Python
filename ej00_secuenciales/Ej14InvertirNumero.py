'''
Ejercicio 14: Dado un número de dos cifras este programa lo invierte.

Vamos a hacerlo de dos formas.

1ª forma:   Pasamos el número a entero y extraemos sus dos cifras con
            la división (1ª) y el resto (2ª) entre 10.
            Variables: numero, cifra1, cifra2, invertido

2ª forma:   Tratamos el número como una cadena de caracteres y mediante
            "slicing" accedemos a las posiciones de su primera y segunda
            cifra.
            Variables: numero, cifra1, cifra2, invertido
'''

# -------------
# Primera forma
# -------------

# pedimos datos
numero = int(input("Dame un número de dos cifras para invertir: "))

# cálculos
cifra1 = numero // 10
cifra2 = numero % 10
invertido = cifra2*10 + cifra1

# muestro resultado
print("El número invertido es", invertido)

# -------------
# Primera forma
# -------------

# pedimos datos
numero = input("Dame un número de dos cifras para invertir: ")

# cálculos
cifra1 = numero[0]
cifra2 = numero[1]
invertido = cifra2 + cifra1
# otras opciones
#invertido = numero[1] + numero[0]

# muestro resultado
print("El número invertido es", invertido)
#print("El número invertido es", numero[::-1])

