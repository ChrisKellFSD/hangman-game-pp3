import random
import os
from words_for_hangman import hangman_words


def hangman_word():
    word = random.choice(hangman_words)
    return word.upper()


def clear_terminal():
    """
    Clears the terminal
    """
    os.system(('cls' if os.name == 'nt' else 'clear'))


def main_title():
    print(
        """
.-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'                                                                                                          
        """
    )
    print(
        """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        """
    )


def play_game(word):
    chances = 7
    guesses = []
    guessed_word = []
    finished = False

    while not finished:
        for char in word:
            if char.lower() in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
        print("")
       
        guess = input(f"You have {chances} chances left. : ")
        guesses.append(guess)
        if guess.lower() not in word.lower():
            chances -= 1
            print("Unlucky! Try again!")
            if chances == 0:
                break
        if ''.join(guessed_word) == word:
            print("Well done! you have gussed the correct word")

        finished = True
        for char in word:
            if char not in guesses:
                finished = False

    if finished:
        print(f"Well done! You guessed {word} correctly!")
    else:
        print(f"Tough Luck. To ease your pain, it was {word}")


def run_game():
    """
    Runs the game
    """
    main_title()
    word = hangman_word()
    play_game(word)


run_game()