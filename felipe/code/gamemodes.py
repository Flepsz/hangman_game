import random
import requests
import time
from logic import color


def play_nutella():
    print("Welcome to the 💩 {}Nutella{} 💩 mode!".format(color['yellow_bg'], color['r']))
    print("You have 10 lives and hints available.\n")

    word_list = ["python", "java", "csharp", "go", "javascript", "php", "mysql", "rust", "ruby", "kotlin"]
    word = word_list[random.randint(0, len(word_list) - 1)]

    current_word = ["_" for letter in word]

    num_lives = 6
    guessed_letters = set()

    while "_" in current_word and num_lives > 0:
        print(" ".join(current_word))
        print("{}Lives{}: {}{}{}".format(color['red_bg'], color['r'], color['red'], num_lives, color['r']))

        if num_lives == 5:
            print("Hint: it's a computer language!")
        elif num_lives == 2:
            print("Hint: it's a back-end language!")

        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("{}Correct!{}\n".format(color['green'], color['r']))
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("{}Incorrect!{}\n".format(color['red'], color['r']))
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
        print("Word: {}".format(word))
    else:
        print("Game over! The word was: {}".format(word))


def play_cafe_com_leite():
    print("Welcome to 🍼{} Café com Leite {}🍼 mode! You have 30 seconds to guess a computer-related word."
          .format(color['cyan_bg'], color['r']))
    print("Here's your hint: it's a computer hardware component.\n")

    word_list = ["mouse", "keyboard", "monitor", "printer", "scanner", "speaker", "router", "server", "cpu", "laptop",
                 "ram", "motherboard", "joystick", "gamepad", "microphone", "headphones", "webcam"]
    word = word_list[random.randint(0, len(word_list) - 1)]

    current_word = ["_" for letter in word]
    num_lives = 6
    guessed_letters = set()

    start_time = time.time()

    while "_" in current_word and time.time() - start_time < 30 and num_lives > 0:
        print(" ".join(current_word))
        print("{}Lives{}: {}{}{}".format(color['red_bg'], color['r'], color['red'], num_lives, color['r']))
        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("{}Correct!{}\n".format(color['green'], color['r']))
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("{}Incorrect!{}\n".format(color['red'], color['r']))
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")


def play_raiz():
    print("Welcome to the 🤯{} Raiz {}🤯 mode!".format(color['white_bg'], color['r']))
    print("You have 20 seconds to guess the word.\n")

    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    word = response.json()[0]
    current_word = ["_" for letter in word]
    num_lives = 6
    guessed_letters = set()

    start_time = time.time()

    while "_" in current_word and time.time() - start_time < 20 and num_lives > 0:
        print(" ".join(current_word))
        print("{}Lives{}: {}{}{}".format(color['red_bg'], color['r'], color['red'], num_lives, color['r']))
        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("{}Correct!{}\n".format(color['green'], color['r']))
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("{}Incorrect!{}\n".format(color['red'], color['r']))
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")
