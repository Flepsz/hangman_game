import random
import requests
import time


def play_nutella():
    print("Welcome to the Nutella mode!")
    print("You have 10 lives and hints available.")

    word_list = ["python", "java", "csharp", "go", "javascript", "php", "mysql", "rust", "ruby", "kotlin"]
    word = word_list[random.randint(0, len(word_list) - 1)]

    current_word = ["_" for letter in word]

    num_lives = 6
    guessed_letters = set()

    while "_" in current_word and num_lives > 0:
        print(" ".join(current_word))
        print("Lives:", num_lives)

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
            print("Correct!")
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("Incorrect!")
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)


def play_cafe_com_leite():
    print("Welcome to Café com Leite mode! You have 30 seconds to guess a computer-related word.")
    print("Here's your hint: it's a computer hardware component.")
    lives = 6
    word_list = ["mouse", "keyboard", "monitor", "printer", "scanner", "speaker", "router", "server", "cpu", "laptop",
                 "tablet", "smartphone", "hard drive", "ram", "graphics card", "motherboard", "power supply",
                 "optical drive", "flash drive", "joystick", "gamepad", "microphone", "headphones", "webcam"]
    word = word_list[random.randint(0, len(word_list) - 1)]

    current_word = ["_" for letter in word]

    num_lives = 6
    guessed_letters = set()

    start_time = time.time()

    while "_" in current_word and time.time() - start_time < 30 and num_lives > 0:
        print(" ".join(current_word))
        print("Lives:", num_lives)
        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("Incorrect!")
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")


def play_raiz():
    print("Welcome to the Raiz mode!")
    print("You have 20 seconds to guess the word.")

    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    word = response.json()[0]
    print(response.json())
    current_word = ["_" for letter in word]
    num_lives = 6
    guessed_letters = set()

    start_time = time.time()

    while "_" in current_word and time.time() - start_time < 20 and num_lives > 0:
        print(" ".join(current_word))
        print("Lives:", num_lives)
        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("Incorrect!")
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")
