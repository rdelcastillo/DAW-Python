# Menú de 4 opciones CON alternativa múltiple (usando match)
# funciona a partir de la versión 3.10 de Python

print("Calculadora básica")
print("------------------")

# datos de entrada
n1 = float(input("Dame el 1er número: "))
n2 = float(input("Dame el 2º número.: "))

# mostramos las opciones
print("\nMenú de opciones")
print("----------------")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

option = int(input("\nDame una opción: ")) # pedimos la opción

# ejecutar la opción escogida
match option:
    case 1:
        print("Suma:", n1 + n2)
    case 2:
        print("Resta:", n1 - n2)
    case 3:
        print("Multiplicación:", n1 * n2)
    case 4:
        print("División:", n1 / n2)
    case _:
        print("Opción incorrecta")