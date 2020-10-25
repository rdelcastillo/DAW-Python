# Programa: primergrado_v2.py
# Propósito:    Resuelve una ecuación de 1er.grado tipo ax+b=0.
#               Uso una estructura alternativa doble
# Autor: Rafael del Castillo.
# Fecha: 10/10/2019.
#
# Variables a usar:
#   * a y b: coeficiente de x y término independiente.
#
# Algoritmo:
#   LEER a,b
#   x <-- -b/a
#   ESCRIBIR x

print("Resolución de una ecuación de 1er.grado tipo 'ax+b=0'")
print("-----------------------------------------------------")

# Pedimos datos
a = float(input("Valor de 'a' (coeficiente x)........: "))
b = float(input("Valor de 'b' (término independiente): "))

# Cálculos
if a!=0:
    x =-b/a
    # Mostramos resultado
    print("El valor de X es", x)
else:
    if b!=0:
        print("No hay solución")
    else:
        print("Hay infinitas soluciones")
