import random
import os
from words_for_hangman import hangman_words


def get_word():
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
                                                            +---+
.-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.       |   |
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |       O   |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |      /|\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'      / \  |
                                                                |  
                                                         =========                                   
        """
    )


def rules():
    """
    Display rules after the title
    """
    clear_terminal()
    print(
        """
            Thank you for choosing to play Hangman.
            You will be presented with a secret word.
            You must guess a letter each round.
            If you are correct, you will see the letter.
            If you are wrong, you will lose a live.
            You have as many goes as it takes for the man to be hanged.
            You can choose the difficulty level (Not yet!)
            \n
            Good luck and have fun!
            """
            )

    input("Press enter to return to the main menu\n")


def play(word):
    hangman_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    chances = 9
    print(display_hangman(chances))
    print(hangman_word)
    print("\n")
    while not guessed and chances > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear_terminal()
                print(f"You already guessed the letter: {guess}")
            elif guess not in word:
                clear_terminal()
                print(f"Unlucky, {guess} is not in the word.")
                chances -= 1
                guessed_letters.append(guess)
            else:
                clear_terminal()
                print(f"Great! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(hangman_word)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_as_list[index] = guess
                hangman_word = "".join(word_as_list)
                if "_" not in hangman_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                clear_terminal()
                print(f"Eh, you guessed {guess} already")
            elif guess != word:
                clear_terminal()
                print(f"Unlucky! but {guess} is not the word.")
                chances -= 1
                guessed_words.append(guess)
            else:
                clear_terminal()
                guessed = True
                hangman_word = word
        else:
            clear_terminal()
            print("Not a valid guess.")
        print(display_hangman(chances))
        print(hangman_word)
        print("\n")
    if guessed:
        clear_terminal()
        print("Congrats, you guessed the word! You win!")
        replay_game()
    else:
        clear_terminal()
        print("""
   ____                         ___                 _ 
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)
                                                      
        """)
        print("\n")
        print(f"To ease your pain, the word was {word}")
        replay_game()


def display_hangman(chances):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -------
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -------
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -------
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -------
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -------
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -------
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -------
                """,
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -------
                """,
                """
                   
                   |      
                   |      
                   |    
                   |      
                   |     
                   -------
                """,
                """
                   
                        
                         
                       
                         
                       
                   -------
                """
    ]
    return stages[chances]


def replay_game():
    while input("Play Again? (Y/N) ").upper() == "Y":
        clear_terminal()
        word = get_word()
        play(word)


def main():
    main_title()
    word = get_word()
    play(word)


if __name__ == "__main__":
    main()