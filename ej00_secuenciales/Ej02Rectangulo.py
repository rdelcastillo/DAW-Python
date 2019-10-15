################################################################################
# Calcular el perímetro y área de un rectángulo dada su base y su altura.
################################################################################
# Análisis
# Tenemos que leer la base y la altura del triangulo y calcular el perímetro y el
# área.
# Datos de entrada: base(real), altura(real)
# Información de salida: perímetro(real) y área(real)
# Variables: base, altura, perimetro y area (Real)
################################################################################
# Diseño
# 1. Leer base y altura
# 2. Calcular perímetro (2*base + 2*altura)
# 3. Calcular área (base * altura)
# 4. Mostrar perímetro y área
################################################################################

# Pedimos datos
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

# Cálculos
perimetro = 2*(base+altura)
area = base*altura

# Mostramos resultado
print("El perímetro es", perimetro, "y el área es", area)



