'''
Este codigo ha sido generado por el modulo psexport 20180125-l64 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http:#pseint.sourceforge.net).

Retocado por Rafael del Castillo con el comando sed.
'''

# ################################################################################
# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
# en cuenta su sueldo base y comisiones.
# ################################################################################
# Análisis
# El vendedor tiene un sueldo base mas una comisión del 10% por cada venta.
# Hace tres ventas.
# Datos de entrada: sueldo base, las tres ventas (real).
# Información de salida: comisiones y sueldo total (real).
# Variables: sueldo_base, venta1, venta2, venta3, comision(real).
# ################################################################################
# Diseño
# 1. Leer sueldo base
# 2. Leer las tres ventas
# 3. Calcular las comisiones. Suma del 10 % de cada venta.
# 4. Mostrar comisión
# 5. Mostrar sueldo total: sueldo_base+comisión
# ################################################################################

# Pedimos datos
sueldo_base = float(input("Dime el sueldo base: "))
venta1 = float(input("Dime precio de la venta 1: "))
venta2 = float(input("Dime precio de la venta 2: "))
venta3 = float(input("Dime precio de la venta 3: "))

# Cálculos
comision = venta1*0.1+venta2*0.1+venta3*0.1

# Salida
print(f"Comisión por ventas: {comision}")
print(f"Sueldo total: {sueldo_base+comision}")



