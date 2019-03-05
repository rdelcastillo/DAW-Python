################################################################################
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
################################################################################
# Análisis
# Hay que pedir el nombre y los apellidos, y mostrar las iniciales.
# Primer carácter de cada cadena.
# Datos de entrada: nombre y apellidos (cadena)
# Información de salida: Iniciales (cadena)
# Variables: nombre, apellido1, apellido2, inicial (cadena).
################################################################################
# Diseño
# 1. Leer nombre y apellidos
# 2. Obtener primer carácter de cada cadena
# 3. Concatenar los caracteres
# 4. Mostrar iniciales
################################################################################

# Pedimos datos
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

# Cálculos
inicial = (nombre[0]+apellido1[0]+apellido2[0]).upper()

# Salida
print("Las iniciales son: ",inicial)



