"""
Programa Ej08CalcularSueldo.py

Propósito: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto
dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
El vendedor tiene un sueldo base mas una comisión del 10% por cada venta. Hace tres ventas.

Datos de entrada: sueldo base, las tres ventas (real).

Información de salida: comisiones y sueldo total (real).

Variables: base_salary, sale1, sale2, sale3, commission(real).
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer sueldo base
2. Leer las tres ventas
3. Calcular las comisiones. Suma del 10 % de cada venta.
4. Mostrar comisión
5. Mostrar sueldo total: base_salary + comisión
"""

print("Cálculo de la comisión y sueldo de un vendedor")
print("----------------------------------------------")

# Pedimos datos
base_salary = float(input("Dime el sueldo base: "))
sale1 = float(input("Dime precio de la venta 1: "))
sale2 = float(input("Dime precio de la venta 2: "))
sale3 = float(input("Dime precio de la venta 3: "))

# Cálculos
commission = 0.1 * (sale1 + sale2 + sale3)     # 10% de las ventas

# Salida
print(f"Comisión por ventas: {commission}")
print(f"Sueldo total: {base_salary + commission}")
