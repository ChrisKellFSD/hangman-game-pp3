import random
from words_for_hangman import hangman_words


def hangman_word():
    word = random.choice(hangman_words)
    return word.upper


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

def welcome_message():
    user = None

    while True:
        user = input('Hello. What is your name? \n')

        if not user.isalpha():
            print('Please use alphabetic characters only.')
            continue
        else:
            print('welcome '+username 'Lets play Hangman')
            break


def play_game(word):
    chances = 7
    guesses = []
    finished = False

    while not finished:
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print(" ", end=" ")
        print("")
        
        guess = input(f"You have {chances} chances left, Guess again :")
        guesses.append(guess)
        if guess not in word:
            chances -= 1
            if chances == 0:
                break

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