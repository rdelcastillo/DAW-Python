import random

"""
*
  * 6. Números aleatorios
  * 
  * 14. Escribe un programa que piense un número al azar entre 0 y 100. El usuario debe
  *     adivinarlo y tiene para ello 5 oportunidades. Después de cada intento fallido, el
  *     programa dirá cuántas oportunidades quedan y si el número introducido es menor o 
  *     mayor que el que ha pensado.
  *
  * @author Luis José Sánchez
"""

oportunidades = 5
minimo = 0
maximo = 100
acertado = False

print("Piensa un número del 0 al 100. Intentaré adivinarlo en 5 intentos.")
input("Pulsa la tecla INTRO cuando estés preparado.") # Ojo!!!! ¿salto de línea previo?

while True:
    numero_pensado = int(random.random() * (maximo - minimo) + minimo)
    print(f"¿Es el {numero_pensado}?") #Original: print("¿Es el " + numeroPensado + "?")
    mayor_menor_o_igual = int(input("El número que estás pensando es 1) mayor 2) menor 3) el mismo: "))
    oportunidades -= 1

    if ( (mayor_menor_o_igual == 1) and (oportunidades > 0)):
        minimo = numero_pensado + 1
    
    if ( (mayor_menor_o_igual == 2) and (oportunidades > 0)):
        maximo = numero_pensado - 1
    
    if mayor_menor_o_igual == 3:
        acertado = True
        print("¡Bien! ¡he acertado!")
    if not (not acertado and (oportunidades > 0)): break

if not acertado:
    print("Vaya, no he conseguido acertar el número.")
