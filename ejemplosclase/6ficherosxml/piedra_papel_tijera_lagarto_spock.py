"""
Implementación del juego piedra-papel-tijera-lagarto-Spock donde los resultados de las victorias se encuentran en un
archivo xml.

Este programa usará una pequeña IA teniendo en cuenta las últimas elecciones del adversario.
"""

import random
import sys
import xml.etree.ElementTree as ET
from enum import IntEnum
from statistics import mode


NUMBER_RECENT_ACTIONS = 5
VICTORIES_XML = "victories.xml"

victories = ET.parse(VICTORIES_XML).getroot()

class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


def main():
    game_history = []
    user_actions_history = []

    while True:
        try:
            user_action = get_user_action()
            user_actions_history.append(user_action)
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_actions_history, game_history)
        game_result = assess_game(user_action, computer_action)
        game_history.append(game_result)

        if not play_another_round():
            break

    show_game_history(game_history)


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def get_computer_action(user_actions_history, game_history):
    # No previous user actions => random computer choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()
    # Alternative AI functionality
    # Choice that would beat the user's most frequent recent choice
    else:
        most_frequent_recent_computer_action = GameAction(mode(user_actions_history[-NUMBER_RECENT_ACTIONS:]))
        computer_action = get_winner_action(most_frequent_recent_computer_action)

    print(f"Computer picked {computer_action.name}.")

    return computer_action


def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    # Search in Victories
    test_xpath = f"./victory[@choice='{user_action.name}'][@against='{computer_action.name}']"
    test_match = victories.find(test_xpath)

    # Game result
    if test_match is not None:  # Victory?
        game_result = GameResult.Victory
        text_result = "You won!"
    else:
        game_result = GameResult.Defeat
        text_result = "You lost!"
        test_xpath = f"./victory[@choice='{computer_action.name}'][@against='{user_action.name}']"
        test_match = victories.find(test_xpath)
        if test_match is None:
            exit_by_rules_incomplete()

    print(f"{test_match.text.strip()}. {text_result}")

    return game_result


def get_random_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)

    return computer_action


def get_winner_action(game_action):
    test_xpath = f"./victory[@against='{game_action.name}']"
    test_matches = victories.findall(test_xpath)
    choices = [test_match.attrib['choice'] for test_match in test_matches]
    try:
        winner_actions = [action for action in GameAction if action.name in choices]
        return random.choice(winner_actions)
    except IndexError:
        exit_by_rules_incomplete()


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def exit_by_rules_incomplete():
    print("Rules for wins are incomplete. Exiting...", file=sys.stderr)
    exit(1)


def show_game_history(game_history):
    print(f"\nTotal rounds: {len(game_history)}")
    print(f"You won in {game_history.count(GameResult.Victory)} rounds")
    print(f"You lost in {game_history.count(GameResult.Defeat)} rounds")
    print(f"you drew in {game_history.count(GameResult.Tie)} rounds")


if __name__ == "__main__":
    main()
