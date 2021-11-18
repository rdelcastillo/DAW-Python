# ################################################################################
# Programa que pida tres números y los muestre ordenados (de mayor a menor)
# ################################################################################
# Análisis
# Pedimos por teclado tres números, se comparan para mostrarlos ordenados.
# Datos de entrada: num1, num2, num3 (entero)
# Información de salida: Los tres número ordenados de mayor a menor
# Variables: num1, num2, num3 (entero)
# ################################################################################
# Diseño
# 1. Leer num1,num2,num3
# 2. Si num1>num2>num3 mostrar num1,num2,num3
# 3. Si num2>num1>num3 mostrar num2,num1,num3
# 4. Si num2>num3>num1 mostrar num2,num3,num1
# 5. Si num3>num2>num1 mostrar num3,num2,num1
# 6. Si num3>num1>num2 mostrar num3,num1,num2
# ################################################################################

# Pedimos datos
num1 = int(input("Dime el número 1: "))
num2 = int(input("Dime el número 2: "))
num3 = int(input("Dime el número 3: "))

# Proceso
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num1} {num2} {num3}")
    else:
        print(f"{num1} {num3} {num2}")
if num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"{num2} {num1} {num3}")
    else:
        print(f"{num2} {num3} {num1}")
if num3 >= num1 and num3 >= num2:
    if num1 > num2:
        print(f"{num3} {num1} {num2}")
    else:
        print(f"{num3} {num2} {num1}")
