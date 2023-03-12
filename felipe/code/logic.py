import random


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
    print("Choose a difficulty level:\n1 - Nutella\n2 - Café com leite\n3 - Raiz")
    while True:
        choice = input("Enter the number of the difficulty level you want to play: ")
        if choice == "1":
            return "nutella"
        elif choice == "2":
            return "cafe_com_leite"
        elif choice == "3":
            return "raiz"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


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
