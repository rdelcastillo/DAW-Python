"""
Propósito: Programa que pide el límite inferior y superior de un intervalo, si el límite inferior es mayor que
el superior lo tiene que volver a pedir. A continuación se van pidiendo números hasta que se introduzca el 0.

Cuando termine el programa dará las siguientes informaciones:
* La suma de los números que están dentro del intervalo (intervalo abierto).
* Cuantos números están fuera del intervalo.
* Informa si hemos introducido algún número igual a los límites del intervalo.
--------------------------------------------------------------------------------
Análisis:
--------------------------------------------------------------------------------
Pedimos un intervalo (límite inferior y superior).
Nos tenemos que asegurar que el límite inferior sea menor que el superior.
Se van pidiendo números hasta que se introduzca el 0.
    Si el número pertenece al intervalo -> lo voy sumando (necesito un acumulador)
    Si el número no pertenece al intervalo, lo cuento (necesito un contador)
    Si el número es igual a algún límite, lo índico (necesito un interruptor)
Al final muestro la suma de los números que pertenecen al intervalo.
Muestro el contador de número que no pertenecen al intervalo.
Indico si hemos introducido un número igual a algún límite

Datos de entrada: límite superior e inferior del intervalo y números.
Información de salida: La suma de los que pertenecen al intervalo,
el contador de los números que no pertenecen al intervalo
indico si un número ha sido igual a algún intervalo

Variables: lim_inf, lim_sup, num, suma_dentro_intervalo, cont_fuera_intervalo (entero),
igual_limites (Lógico)
----------------------------------------------------------------------------------------
Diseño:
----------------------------------------------------------------------------------------
1.- Inicializo el acumulador, el contador y el interruptor
2.- Repetir -> leer lim_inf y lim_sup hasta que lim_inf<lim_sup
3.- Leer num
4.- Mientras num sea distinto de 0
    5.- Si num pertenece al intervalo -> acumula la suma
    6.- Sino -> incremento contador
    7.- Si es igual a algún límite del intervalo -> Lo indico (indicador a Verdadero)
    8.- Leer num
9.- Muestro la suma de los números pertenecientes al intervalo
10.-Muestro el contador de números no pertenecientes al intervalo
11.-Si el indicador = Verdadero -> Muestro "Un número = a intervalo"
12.-SiNo -> Muestro "No has introducido un número igual al intervalo
"""

# Inicializamos
numbers_out_range = 0    # cuenta los números introducidos fuera del intervalo
there_are_numbers_at_the_limits = False    # interruptor que nos dice si hemos introducido algún extremo
sum_in_range = 0    # suma de los números introducidos dentro del intervalo

# Pido el intervalo y me aseguro que el lim_inf introducido es menor que el lim_sup
# se podía haber hecho con un ciclo ITERAR (ver siguiente ejemplo)
lower_range = int(input("Introduce el límite inferior del intervalo: "))
upper_range = int(input("Introduce el límite superior del intervalo: "))
while lower_range > upper_range:
    print("El límite inferior no puede ser mayor al superior.")
    print("VUELVE a introducir los límites.\n")
    lower_range = int(input("Introduce (correctamente) el límite inferior del intervalo: "))
    upper_range = int(input("Introduce (correctamente) el límite superior del intervalo: "))

# Proceso
num = int(input("\nIntroduce un número (0, para salir): "))
while num != 0:
    if lower_range < num < upper_range:  # Pertenece al intervalo (num>lim_inf and num<lim_sup en otro lenguaje)
        sum_in_range += num
    else:  # No pertenece al intervalo
        numbers_out_range += 1
        # Número igual a alguno de los límites
        if num == lower_range or num == upper_range:
            there_are_numbers_at_the_limits = True
    num = int(input("Introduce un número (0, para salir): "))

# Resultados
print("\nRESULTADOS:")
print(f"La suma de los números dentro del intervalo es {sum_in_range}")
print(f"La cantidad de números fuera del intervalo es {numbers_out_range}")
if there_are_numbers_at_the_limits:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
