# ################################################################################
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las
# dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triángulo es, teniendo en cuenta:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.
# ################################################################################
# Análisis
# Pedir la medida de los tres lados de un triángulo:
# Si se cumple el teorema de pitágoras es un triángulo rectángulo
# Además, si tienes dos lados iguales y uno desigual, es isósceles
# O si tiene todos los lados iguales es equilátero
# o si son los tres distintos es escaleno.
# Datos de entrada: los tres lados del triángulo (real)
# Información de salida: Tipo de rectángulo
# Variables: ladoA, ladoB, ladoC (real)
# ################################################################################
# Diseño
# 1.Leer ladoA, ladoB, ladoC
# 2.Si se cumple el teorema de pitágoras ( tenemos que suponer que cualquier
# lado puede ser la hipotenusa) mostrar "Triángulo rectángulo"
# 3.Si tiene dos lados iguales y uno desigual mostrar "Triángulo Isósceles"
# 4. En otro caso, si tiene los tres lados iguales, mostrar "Triángulo Equilátero"
# 5. En otro caso, mostrar "Triángulo Escaleno"
# ################################################################################
# Ejemplos
# (3,4,5) rectángulo,escaleno
# (7,7,9.8994949366117) rectángulo,isósceles
# ################################################################################

import math

# Pedimos datos
ladoa = float(input("Introduce longitud lado A: "))
ladob = float(input("Introduce longitud lado B: "))
ladoc = float(input("Introduce longitud lado C: "))

# Pitágoras
if math.pow(ladoa,2)+math.pow(ladob,2)==math.pow(ladoc,2) or math.pow(ladob,2)+math.pow(ladoc,2)==math.pow(ladoa,2) or math.pow(ladoc,2)+math.pow(ladoa,2)==math.pow(ladob,2):
    print("Triángulo Rectángulo")
# isósceles
if (ladoa==ladob and ladoa!=ladoc) or (ladob==ladoc and ladob!=ladoa) or (ladoc==ladoa and ladoc!=ladob):
    print("Triángulo Isósceles")
# equilátero
elif ladoa==ladob and ladoa==ladoc:
    print("Triángulo Equilátero")
# escaleno
else:
    print("Triángulo Escaleno")



