# ################################################################################
# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
# ################################################################################
# Análisis
# Pedimos por teclado una cadena
# y hay que comprobar que todas las letras sean mayúsculas.
# Datos de entrada: cadena (cadena)
# Información de salida: Mensajes de es mayúsculas o no es mayúsculas.
# Variables: cadena (cadena)
# ################################################################################
# Diseño
# 1. Leer la cadena
# 2. Si la cadena es igual a la cadena convertida en mayúsculas,
# mostrar "La cadena es mayúsculas"
# 3. En caso contrario mostrar "La cadena no es mayúsculas"
# ################################################################################

# Pedir datos
cad = input("Introduce una cadena: ")

# Comprobamos ymostramos resultados
if len(cad)==1 and cad>="A" and cad<="Z":
    print("La cadena es una letra mayúscula")
else:
    print("La cadena no es una letra mayúscula")



