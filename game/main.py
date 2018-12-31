import os
import sys
from random import random
from time import sleep
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))
    )
)
from game.company import Company
from game.software import Software


def start_game():
    print("Welcome to DevSim")
    print("1. New Game")
    print("2. Load")
    print("3. Quit")
    return choose()


def choose(init=1, end=3):
    try:
        choice = int(input("Your choice: "))
    except Exception:
        choice = 0
    while choice < init or choice > end:
        print("Choice not valid.")
        try:
            choice = int(input("Your choice: "))
        except Exception:
            choice = 0
    return choice


def run_turn(player_company):
    """

    :type player_company: Company
    """
    game = True
    turn = 0
    while game:
        turn = display_turn(turn, player_company)
        action_turn(player_company)
        if turn >= 4:
            game = decide_players_fate()


def action_turn(player_company):
    print(f"1. Create software\n"
          f"2. Program\n"
          f"3. Hire new employee")
    chosen = choose()
    if chosen == 1:
        soft_name = input("What is the software's name? ")
        player_company.stats["software"].append(Software(name=soft_name))
        print("Software starting development now.")
    elif chosen == 2:
        pass
    else:
        pass
    return 1


def display_turn(turn=0, company=None):
    os.system('clear')
    if company:
        print("-----------------------------\n"
              f"Company: {company.stats['name']}\n"
              f"{company.stats['age']} year(s) old, "
              f"{company.stats['fans']} fan(s), "
              f"{company.stats['rating']} star(s).\n"
              f"Products released: {len(company.stats['software'])}\n"
              f"Turn: {turn}")
        print("-----------------------------")
        sleep(1)
    return turn + 1


def set_up_player(sleep_time=0):
    print("Welcome to DevSim!\n")
    print("This is a world very much like yours,")
    print("Where ethics and good principles should")
    print("rule the software world.\n")
    sleep(sleep_time)
    company_name = input("What is your company's name? ")
    sleep(sleep_time)
    return company_name


def main():
    a = start_game()
    if a == 1:
        player_company = Company(set_up_player())
        print(player_company.stats)
        run_turn(player_company)
    if a == 3:
        return 0
    return 0


def decide_players_fate():
    if random() > 0.3:
        win_game()
    lose_game()
    return False


def win_game():
    print(
        "You have dominated the software industry.\n"
        "Congratulations!!! The game is finally over!"
    )
    return 0


def lose_game():
    print(
        "You have been bested by your fellow colleagues.\n"
        "Good luck next time."
    )
    return 0


if __name__ == '__main__':
    main()
