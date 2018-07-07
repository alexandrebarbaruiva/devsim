import os


def start_game():
    print("Welcome to DevSim")
    print("1. Play")
    print("2. Load")
    print("3. Quit")
    try:
        choice = int(input("Your choice: "))
    except Exception:
        choice = 0
    while (choice < 1 or choice > 3):
        print("Choice not valid.")
        try:
            choice = int(input("Your choice: "))
        except Exception:
            choice = 0
    return choice

def play_turn(turn):
    os.system('clear')
    print("-----------------------------")
    print("Turn: {}".format(turn))
    return turn + 1

if __name__ == '__main__':
    start_game()
