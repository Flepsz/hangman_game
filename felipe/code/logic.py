import random

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


def get_word(words):
    return random.choice(words)


def check_letter(letter, word, hidden_word):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
        return True
    else:
        return False


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


def display_game(hidden_word, guessed_letters, remaining_lives):
    print(" ".join(hidden_word))
    print("Guessed letters: {}".format(', '.join(guessed_letters)))
    print("Lives remaining: {}".format(remaining_lives))


def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:
            return guess
        else:
            print("Invalid guess. Please enter a single letter that hasn't been guessed yet.")


def check_game_over(hidden_word, remaining_lives):
    if "_" not in hidden_word:
        print("Congratulations, you won!")
        return True
    elif remaining_lives == 0:
        print("Sorry, you lost. The word was:", "".join(hidden_word))
        return True
    else:
        return False
