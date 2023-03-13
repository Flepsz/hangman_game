from gamemodes import *


def main():
    print("Welcome to Hangman Game!")
    while True:
        level = get_level()
        if level == "Nutella":
            play_nutella()
        elif level == "Café com leite":
            play_cafe_com_leite()
        elif level == "Raiz":
            play_raiz()
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
