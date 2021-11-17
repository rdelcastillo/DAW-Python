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
Variación del programa anterior donde usaremos una implementación del ciclo
ITERAR para evitar pedir dos veces los límites del intervalo.
"""

# Inicializamos
contador_fuera_del_intervalo = 0    # cuenta los números introducidos fuera del intervalo
igual_limites_intervalo = False     # interruptor que nos dice si hemos introducido algún extremo
suma_dentro_intervalo = 0           # suma los números introducidos dentro del intervalo

# Pido el intervalo y me aseguro que el lim_inf introducido es menor que el lim_sup
while True:
    lim_inf = int(input("Introduce el límite inferior del intervalo: "))
    lim_sup = int(input("Introduce el límite superior del intervalo: "))
    if lim_inf <= lim_sup:
        break
    print("El límite inferior no puede ser mayor al superior.")
    print("VUELVE a introducir los límites.\n")

# Proceso
num = int(input("\nIntroduce un número (0, para salir): "))
while num != 0:
    if lim_inf < num < lim_sup:  # Pertenece al intervalo (num>lim_inf and num<lim_sup en otro lenguaje)
        suma_dentro_intervalo += num
    else:  # No pertenece al intervalo
        contador_fuera_del_intervalo += 1
        # Número igual a alguno de los límites
        if num == lim_inf or num == lim_sup:
            igual_limites_intervalo = True
    num = int(input("Introduce un número (0, para salir): "))

# Resultados
print("\nRESULTADOS:")
print(f"La suma de los números dentro del intervalo es {suma_dentro_intervalo}")
print(f"La cantidad de números fuera del intervalo es {contador_fuera_del_intervalo}")
if igual_limites_intervalo:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
