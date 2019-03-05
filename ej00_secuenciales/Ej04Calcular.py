# ################################################################################
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
# ################################################################################
# Análisis
# Tenemos que leer dos números, calcular la suma, resta, multiplicación y división
# Datos de entrada: Los dos números (real)
# Información de salida: suma, resta, multiplicación, división(real)
# Variables: num1, num2 (Real).
# Considero que las salidas no es necesario guardarla en variables.
# ################################################################################
# Diseño
# 1. Leer los números
# 2. Mostrar suma,resta, multiplicación y división
# ################################################################################

# Pedimos datos
num1 = float(input("Introduce el número 1: "))
num2 = float(input("Introduce el número 2: "))

# Mostramos resultados
print(f"La suma es {num1+num2}")
print(f"La resta es {num1-num2}")
print(f"La multiplicación es {num1*num2}")
print(f"La división es {num1/num2}")



