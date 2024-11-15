"""
Programa que simule el juego clásico "Piedra, papel o tijera" contra el ordenador.

Autor: Rafael del Castillo.
Fecha: 12/11/2024.
"""
import random

print("PIEDRA, PAPEL o TIJERA")
print("----------------------")

rounds_played = 0
rounds_won = 0
rounds_lost = 0

keep_playing = "sí"

while keep_playing == "sí":
    # Pedimos jugada al usuario y controlamos si hay error
    while True:
        player_choice = input("¿Piedra, papel o tijera? ").lower()
        if player_choice == "piedra" or player_choice == "papel" or player_choice == "tijera":
            break
        print("Entrada inválida. Elige entre piedra, papel o tijera.")

    # El ordenador hace su jugada
    computer_choice = random.choice(["piedra", "papel", "tijera"])
    print(f"El ordenador eligió {computer_choice}")

    rounds_played += 1

    # Averiguamos el ganador de la ronda
    if player_choice == computer_choice:
        print("Es un empate.")
    elif (player_choice == 'piedra' and computer_choice == 'tijera') or \
            (player_choice == 'tijera' and computer_choice == 'papel') or \
            (player_choice == 'papel' and computer_choice == 'piedra'):
        print("¡Has ganado!")
        rounds_won += 1
    else:
        print("Has perdido.")
        rounds_lost += 1

    # ¿Seguimos jugando?
    while True:
        keep_playing = input("\n¿Quieres jugar otra vez? (sí/no): ").lower()
        if keep_playing == "sí" or keep_playing == "no":
            break
        print("Respuesta errónea. Contesta sí o no.")
    print()

print(f"Fin del juego. Has jugado {rounds_played} rondas: {rounds_won} ganadas, {rounds_lost} perdidas, "
      f"{rounds_played-rounds_lost-rounds_won} empates.")