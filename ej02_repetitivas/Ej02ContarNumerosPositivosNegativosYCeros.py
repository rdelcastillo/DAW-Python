# ################################################################################
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
# números a introducir). El programa debe informar de cuantos números introducidos
# son mayores que 0, menores que 0 e iguales a 0.
# ################################################################################
# Análisis
# Se pide la cantidad de números que se van a leer. Vamos introduciendo números.
# Tenemos que contar los positivos, negativos y 0.
# Datos de entrada:Cantidad de números, los números.
# Información de salida: Cantidad de positivos, de negativos y de 0.
# Variables:cantidad_num,num,contPositivos,cant_negativos,cantidad_ceros(entero)
# ################################################################################
# Diseño
# 1.- Inicializo los contadores
# 2.- Leer cantidad de números
# 3.- Desde 1 hasta cantidad de números
# 4.- Leer num
# 5.- Si num> 0-> incremento contPositivos
# 6.- Si num< 0-> incremento contNegativos
# 7.- Si num = 0-> incremento contCeros.
# Muestro cont_postivos, contNegativos, contCeros
# ################################################################################

# Inicializamos contadores
contPositivos = 0
contNegativos = 0
contCeros = 0

# Pedimos cantidad de números a introducir
cantidad_num = int(input("¿Cuántos números vas a introducir?: "))

# Ciclo
for i in range(1,cantidad_num+1):
    num = int(input(f"Número {i}: "))
    # Comprobamos si es +, - ó 0 e incrementamos contador
    if num>0:
        contPositivos += 1
    elif num<0:
        contNegativos += contNegativos+1
    else:
        contCeros += 1
        
# Mostramos resultados
print(f"Números positivos: {contPositivos}")
print(f"Números negativos: {contNegativos}")
print(f"Números igual a 0: {contCeros}")

