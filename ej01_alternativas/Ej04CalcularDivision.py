# ################################################################################
# Crea un programa que pida al usuario dos números y muestre su división
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
# ################################################################################
# Análisis
# Tenemos que pedir dos números, y mostrar el resultado de la división.
# Si el divisor es 0 debemos responder un mensaje de error.
# Datos de entrada: dividendo, divisor (entero)
# Información de salida: El resultado de la división o un mensaje de error
# indicando que el divisor es igual a 0.
# Variables: dividendo,divisor (enteros)
# ################################################################################
# Diseño
# 1. Leer los números
# 2. Si el divisor es igual a 0 escribir "No se puede dividir por 0"
# 3. En caso contrario mostrar el resultado de la división
# ################################################################################

# Pedimos datos
dividendo = int(input("Dime el número 1: "))
divisor = int(input("Dime el número 2: "))

# Mostramos
if divisor==0:
    print("No puedes dividir por 0")
else:
    print(f"La división es {dividendo/divisor}")



