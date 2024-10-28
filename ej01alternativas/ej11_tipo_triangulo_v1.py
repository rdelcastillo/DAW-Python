"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triángulo es, teniendo en cuenta:
- Si se cumple Pitágoras entonces es triángulo rectángulo
- Si solo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Autor: Clase 1ºDAW.
Fecha: 29/10/2019.

Análisis
--------
1. Pedir la medida de los tres lados de un triángulo.
2. Comprobamos si es equilátero (si lo es no puede ser el resto de casos, ni siquiera rectángulo)
En caso contrario
3. Comprobamos si se cumple el teorema de pitágoras, entonces es un triángulo rectángulo.
4. Comprobamos si tiene dos lados iguales (y uno desigual, sino sería equilátero), es isósceles
5. Si no es isósceles, es escaleno.

- Datos de entrada: los tres lados del triángulo (flotante).
- Información de salida: Tipo de rectángulo.
- Variables: ladoA, ladoB, ladoC (flotante)

-----------
Ejemplos:
(3,4,5) rectángulo,escaleno
(7,7,9.8994949366117) rectángulo,isósceles
"""

# Pedimos los datos de los lados del triángulo
side_a = float(input("Introduce longitud lado A: "))
side_b = float(input("Introduce longitud lado B: "))
side_c = float(input("Introduce longitud lado C: "))

# Cálculos
# Comprobamos si es equilátero, este caso es excluyente
if side_a == side_b and side_b == side_c:  # Python permitiría lado_a == lado_b == lado_c
    print("El triángulo es EQUILÁTERO")
else:
    # Comprobamos si es rectángulo (puede ser rectángulo y isósceles o escaleno)
    if side_a ** 2 == (side_b ** 2 + side_c ** 2) \
            or side_b ** 2 == (side_a ** 2 + side_c ** 2) \
            or side_c ** 2 == (side_b ** 2 + side_a ** 2):
        print("El triángulo es RECTÁNGULO")
    # Comprobamos si es isósceles o escaleno (equilátero no es)
    if side_a == side_b or side_a == side_c or side_b == side_c:
        print("El triángulo es ISÓSCELES")
    else:
        print("El triángulo es ESCALENO")
