"""
Este programa juega al piedra/papel/tijera contra el ordenador que usa números aleatorios para realizar la tirada.
Después de cada jugada pregunta al usuario si quiere continuar, en caso negativo se muestra el número de partidas
jugadas, las ganadas por cada jugador y las empatadas.

Algoritmo
---------
empates <-- 0
victorias <-- 0
pérdidas <-- 0
REPETIR
    PEDIR tirada_humano
    tirada_ordenador = ALEATORIO(1,3)

    gana_humano <-- Falso
    gana_ordenador <-- Falso
    SI tirada_ordenador == tirada_humano
        empates <-- empates + 1
    SINO SI tirada_humano == ROCA
        SI tirada_ordenador == PAPEL
            gana_ordenador <-- VERDADERO
        SINO
            gana_humano <-- VERDADERO
        FIN-SI
    SINO SI tirada_humano == PAPEL
        SI tirada_ordenador == ROCA
            gana_humano <-- VERDADERO
        SINO
            gana_ordenador <-- VERDADERO
        FIN-SI
    SINO
        SI tirada_ordenador == PAPEL
            gana_humano <-- VERDADERO
        SINO
            gana_ordenador <-- VERDADERO
        FIN-SI
    FIN-SI

    SI gana_humano
        victorias <-- victorias + 1
        ESCRIBIR "Ganaste!"
    SINO SI gana_ordenador
        pérdidas <-- pérdidas + 1
        ESCRIBIR "Perdiste!"
    SINO
        ESCRIBIR "Empate"
    FIN-SI

    PEDIR seguir
HASTA QUE seguir=="N"

ESCRIBIR_ESTADÍSTICAS
---------------------

Fecha: 25/11/2021
Autor: Rafael del Castillo
"""
import random

PAPER_COVER_ROCK = "Papel tapa a Piedra"
ROCK_CRUSHES_SCISSORS = "Piedra aplasta a Tijera"
SCISSORS_CUT_PAPER = "Tijera corta a Papel"
ROCK, PAPER, SCISSORS = 1, 2, 3
PLAY = ["Piedra", "Papel", "Tijera"]

tied_games, won_games, lost_games = 0, 0, 0

print("Batalla a piedra, papel y tijera")
print("--------------------------------")
while True:
    # Juega humano
    while True:
        human_play_str = input("\n¿Piedra (1), Papel (2) o Tijera (3)? ")
        if human_play_str.isdigit() and 1 <= int(human_play_str) <= 3:
            break
        print("Opción incorrecta, hay que introducir 1, 2 o 3.")
    human_play = int(human_play_str)

    # Juega ordenador
    computer_play = random.randint(1, 3)
    print("Ordenador juega:", PLAY[computer_play-1])

    # ¿Quién gana?
    human_win, computer_win = False, False
    if human_play == computer_play:
        tied_games += 1
    elif human_play == ROCK:
        if computer_play == PAPER:
            computer_win = True
            message = PAPER_COVER_ROCK
        else:
            human_win = True
            message = ROCK_CRUSHES_SCISSORS
    elif human_play == PAPER:
        if computer_play == ROCK:
            human_win = True
            message = PAPER_COVER_ROCK
        else:
            computer_win = True
            message = SCISSORS_CUT_PAPER
    else:
        if computer_play == ROCK:
            computer_win = True
            message = ROCK_CRUSHES_SCISSORS
        else:
            human_win = True
            message = SCISSORS_CUT_PAPER

    # Resultado
    if human_win:
        print("¡Ganaste!", message)
        won_games += 1
    elif computer_win:
        print("¡Perdiste!", message)
        lost_games += 1
    else:
        print("Empate.")

    # ¿Seguimos?
    while True:
        keep_playing = input("\n¿Seguimos jugando? (S/N) ").upper()
        if keep_playing in "SN":
            break
        print("Respuesta incorrecta, hay que contestar S o N")
    if keep_playing == "N":
        break

# Estadísticas
print("\nPartidas jugadas:  ", won_games + lost_games + tied_games)
print("Partidas ganadas:  ", won_games)
print("Partidas perdidas: ", lost_games)
print("Partidas empatadas:", tied_games)
