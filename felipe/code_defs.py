import random
import requests
import time

color = {
    # Regular colors
    'black': '\33[30m',
    'red': '\33[31m',
    'green': '\33[32m',
    'yellow': '\33[33m',
    'blue': '\33[34m',
    'magenta': '\33[35m',
    'cyan': '\33[36m',
    'white': '\33[37m',

    # Background colors
    'black_bg': '\33[40m',
    'red_bg': '\33[41m',
    'green_bg': '\33[42m',
    'yellow_bg': '\33[43m',
    'blue_bg': '\33[44m',
    'magenta_bg': '\33[45m',
    'cyan_bg': '\33[46m',
    'white_bg': '\33[47m',

    # Modifiers
    'bold': '\33[1m',
    'underline': '\33[4m',
    'invert': '\33[7m',

    # Reset
    'r': '\33[m'
}


def random_word_nutella():
    word_list = ["python", "java", "csharp", "go", "javascript", "php", "mysql", "rust", "ruby", "kotlin"]
    hint_nutella = "Hint: it's a back-end language!"
    word = word_list[random.randint(0, len(word_list) - 1)]
    return word, hint_nutella


def random_word_cafe():
    word_list = ["mouse", "keyboard", "monitor", "printer", "scanner", "speaker", "router", "server", "cpu", "laptop",
                 "ram", "motherboard", "joystick", "gamepad", "microphone", "headphones", "webcam"]
    word = word_list[random.randint(0, len(word_list) - 1)]
    return word


def random_word_raiz():
    word = str
    definition = str
    while True:
        try:
            url = "https://random-word-api.herokuapp.com/word?number=1"
            response = requests.get(url)
            word = response.json()[0]

            url2 = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response2 = requests.get(url2)
            definition = response2.json()[0]['meanings'][0]['definitions'][0]['definition']
            break
        except KeyError as e:
            continue

    return word, definition


def play_game(word, time_set, num_lives, hint):
    start_time = time.time()
    current_word = list("_" * len(word))
    guessed_letters = set()

    while "_" in current_word and time.time() - start_time < time_set and num_lives > 0:
        print(" ".join(current_word))
        print("{}Lives{}: {}{}{}".format(color['red_bg'], color['r'], color['red'], num_lives, color['r']))
        user_input = get_user_input(guessed_letters)
        guessed_letters.add(user_input)

        if num_lives == 3:
            print(hint)

        if user_input in word:
            print("{}Correct!{}\n".format(color['green'], color['r']))
        else:
            num_lives -= 1
            print("{}Incorrect!{}\n".format(color['red'], color['r']))

    return guessed_letters, current_word


def get_user_input(guessed_letters):
    user_input = input("Guess a letter: ").lower()
    while not user_input.isalpha() or len(user_input) != 1 or user_input in guessed_letters:
        if user_input in guessed_letters:
            print("You already guessed that letter!")
        else:
            print("Invalid input.")
        user_input = input("Guess a letter: ").lower()
    return user_input


def update_current_word(current_word, word, user_input):
    for i in range(len(word)):
        if word[i] == user_input:
            current_word[i] = user_input


def check_word_completion(current_word, word, start_time):
    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")


def get_level():
    import inquirer
    questions = [
        inquirer.List('modes',
                      message="Choose the difficulty level",
                      choices=['Nutella', 'Café com leite', 'Raiz'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['modes']
