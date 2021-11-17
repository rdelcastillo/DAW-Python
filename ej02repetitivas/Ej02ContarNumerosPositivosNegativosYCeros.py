"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
números a introducir). El programa debe informar de cuantos números introducidos
son mayores que 0, menores que 0 e iguales a 0.
---
Análisis
Se pide la cantidad de números que se van a leer. Vamos introduciendo números.
Tenemos que contar los positivos, negativos y 0.
Datos de entrada:Cantidad de números, los números.
Información de salida: Cantidad de positivos, de negativos y de 0.
Variables: cantidad_num, num, cont_positivos, cont_negativos, cont_ceros (enteros)
---
Diseño
1.- Inicializo los contadores
2.- Leer cantidad de números
3.- Desde 1 hasta cantidad de números
        Leer num
        Si num > 0-> incremento cont_positivos
        Si num < 0-> incremento cont_negativos
        Si num = 0-> incremento cont_ceros.
4.- Muestro contadores
"""

# Inicializamos contadores
cont_positivos = 0
cont_negativos = 0
cont_ceros = 0

# Pedimos cantidad de números a introducir
cantidad_num = int(input("¿Cuántos números vas a introducir?: "))

# Ciclo
for i in range(cantidad_num):
    num = int(input(f"Número {i+1}: "))
    # Comprobamos si es +, - ó 0 e incrementamos contador
    if num > 0:
        cont_positivos += 1
    elif num < 0:
        cont_negativos += 1
    else:
        cont_ceros += 1

# Mostramos resultados
print(f"Números positivos: {cont_positivos}")
print(f"Números negativos: {cont_negativos}")
print(f"Números igual a 0: {cont_ceros}")
