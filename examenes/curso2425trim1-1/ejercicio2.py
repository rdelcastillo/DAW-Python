"""
Programa que simule un juego de dados contra el ordenador, donde se acumulen puntos basados en el resultado de los
lanzamientos.

El usuario y el ordenador lanzan un dado (simulado por números aleatorios del 1 al 6). El usuario decide cuándo lanzar
el dado presionando Intro, y el resultado del ordenador se genera automáticamente.

Si el número en el dado del jugador es mayor que el del ordenador, el jugador gana la ronda y se acumulan puntos iguales
al número en su dado.

Si el número en el dado del ordenador es mayor, el ordenador gana la ronda y se acumulan puntos iguales al número en su
dado.

Si ambos números son iguales, se considera un empate y no se acumulan puntos.

Después de cada ronda, muestra el resultado de quién ganó y cuál fue el resultado de los dados.

Al finalizar el juego, muestra el total de puntos acumulados por el jugador y por el ordenador indicando quién
ha ganado.
"""
import random

print("JUEGO DE DADOS CONTRA EL ORDENADOR")
print("----------------------------------")

points_player = 0
points_computer = 0

while True:
    # Tirada del jugador/a
    input("Presiona Intro para lanzar tu dado: ")
    dice_player = random.randint(1, 6)
    print("Tu dado:", dice_player)

    # Tirada del ordenador
    dice_computer = random.randint(1, 6)
    print("Dado del ordenador:", dice_computer)

    # Vemos quién gana y acumulamos resultados
    if dice_player > dice_computer:
        print("¡Ganaste la ronda!")
        points_player += dice_player
    elif dice_computer > dice_player:
        print("El ordenador gana la ronda.")
        points_computer += dice_computer
    else:
        print("¡EMPATE!")

    # Mostramos la puntuación acumulada
    print("Puntos acumulados por ti:", points_player)
    print("Puntos acumulados por el ordenador:", points_computer, "\n")

    # ¿Seguimos?
    while True:
        keep_playing = input("¿Quieres lanzar de nuevo? (sí/no): ").lower()
        if keep_playing in ["sí", "no"]:
            break
        print("Respuesta errónea, contesta con sí o no.")
    print()

    if keep_playing == "no":
        break

# Mostramos los resultados finales
print("Fin del juego.")
if points_player > points_computer:
    print(f"Ganaste la partida {points_player} a {points_computer}.")
elif points_computer > points_player:
    print(f"Gana el ordenador {points_computer} a {points_player}.")
else:
    print(f"Habéis empatado a {points_player}.")
