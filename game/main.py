import os
import sys
from time import sleep
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))
    )
)
from game.company import Company


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
    while (choice < init or choice > end):
        print("Choice not valid.")
        try:
            choice = int(input("Your choice: "))
        except Exception:
            choice = 0
    return choice


def action_turn():
    return choose()


def display_turn(turn=0, company=None):
    os.system('clear')
    if company:
        print("-----------------------------")
        print(f"Company: {company.stats['name']}")
        print(f"{company.stats['age']} year(s) old, "
              f"{company.stats['fans']} fan(s), "
              f"{company.stats['rating']} star(s)."
        )
        print(f"Turn: {turn}")
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
        turn = 0
        while turn < 3:
            turn = display_turn(turn, player_company)
    return 0


if __name__ == '__main__':
    main()
