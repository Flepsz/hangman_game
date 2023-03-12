from logic import *
from gamemodes import *


def main():
    print("Welcome to Hangman!")
    while True:
        level = get_level()
        if level == "nutella":
            play_nutella()
        elif level == "cafe_com_leite":
            play_cafe_com_leite()
        elif level == "raiz":
            play_raiz()
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
