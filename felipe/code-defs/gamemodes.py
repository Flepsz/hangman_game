from logic import *


def play_nutella():
    print("Welcome to the {}Nutella{} mode!".format(color['yellow_bg'], color['r']))
    print("You have 10 lives and hints available.\n")
    print("Hint: it's a computer language!")

    word, hint_nutella = random_word_nutella()

    guessed_letters, current_word, start_time = play_game(word, 9999, 6, hint_nutella)

    user_input = get_user_input(guessed_letters)

    update_current_word(current_word, word, user_input)

    check_word_completion(current_word, word, start_time)


def play_cafe_com_leite():
    print("Welcome to {} Café com Leite {} mode! You have 30 seconds to guess a computer-related word."
          .format(color['cyan_bg'], color['r']))
    print("Hint: it's a computer hardware component.\n")

    word = random_word_cafe()

    guessed_letters, current_word, start_time = play_game(word, 30, 6)

    user_input = get_user_input(guessed_letters)

    update_current_word(current_word, word, user_input)

    check_word_completion(current_word, word, start_time)


def play_raiz():
    print("Welcome to the {} Raiz {} mode!".format(color['cyan_bg'], color['r']))
    print("You have 20 seconds to guess the word.\n")

    word, definition = random_word_raiz()

    guessed_letters, current_word, start_time = play_game(word, 20, 6, definition)

    user_input = get_user_input(guessed_letters)

    update_current_word(current_word, word, user_input)

    check_word_completion(current_word, word, start_time)
