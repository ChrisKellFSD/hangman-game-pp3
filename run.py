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

def run_game():
    main_title()

run_game()
        