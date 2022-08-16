import random
import os
from words_for_hangman import hangman_words


class style:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def get_word():
    word = random.choice(hangman_words)
    return word.upper()


def main_title():
    print(
        style.BLUE + 
        """
                                                            +---+
.-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.       |   |
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |       O   |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |      /|\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'      / \  |
                                                                |  
                                                         =========                                   
        """ + style.END.center(40))


def clear_terminal():
    """
    Clears the terminal
    """
    os.system(('cls' if os.name == 'nt' else 'clear'))
    main_title()
    print("\n")


def main_menu():
    """
    Display a welcome title and navigate to start the game or see rules
    """
    clear_terminal()
    option_1 = "1: Play Hangman"
    option_1_cnt = option_1.center(60)
    print(option_1_cnt)
    option_2 = "2: How to Play"
    option_2_cnt = option_2.center(60)
    print(option_2_cnt)
    print("\n")
    while True:
        player_choice = input("Please select 1 or 2: ".center(60))
        if player_choice == "1":
            play_game()
        elif player_choice == "2":
            rules()
        else:
            print("To proceed, please choose either 1 or 2")


def rules():
    """
    Display rules after the title
    """
    clear_terminal()
    print(
        style.YELLOW +
        """
          +--HOW TO PLAY---------------------------------------------------+
          |                                                                |
          |  Thank you for choosing to play Hangman.                       |
          |  You will be presented with a secret word.                     |
          |  You must guess a letter each round.                           |
          |  If you are correct, you will see the letter.                  |
          |  If you are wrong, you will lose a life.                       |
          |  You have as many goes as it takes for the man to be hanged.   |
          |                                                                |
          |  Good luck and have fun!                                       |
          |                                                                |
          +----------------------------------------------------------------+
          """ + style.END
            )

    input(style.BOLD + "Press any key return to the main menu \n" + style.END)
    main_menu()


def play(word):
    hangman_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    chances = 9
    clear_terminal()
    print(hangman_sketch(chances))
    print(hangman_word)
    print("\n")
    while not guessed and chances > 0:
        print(f"Guessed Letters: {guessed_letters}")
        print(f"Chances left: {chances}")
        print("\n")
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear_terminal()
            elif guess not in word:
                clear_terminal()
                print(f"Unlucky, {guess} is not in the word.")
                chances -= 1
                guessed_letters.append(guess)
            else:
                clear_terminal()
                print(f"Great! {guess} is in the word!")
                guessed_letters.append(guess)
                word_list = list(hangman_word)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_list[index] = guess
                hangman_word = "".join(word_list)
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
        print(hangman_sketch(chances))
        print(hangman_word)
        print("\n")
    if guessed:
        clear_terminal()
        game_win()
        print(f"Congrats, you guessed the word {word}")
        replay_game()
    else:
        clear_terminal()
        game_over()
        print("\n")
        print(f"To ease your pain, the word was {word}")
        replay_game()


def hangman_sketch(chances):
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


def game_win():
    print(style.GREEN +
          """
 __        __   _ _   ____                   _ 
 \ \      / /__| | | |  _ \  ___  _ __   ___| |
  \ \ /\ / / _ \ | | | | | |/ _ \| '_ \ / _ \ |
   \ V  V /  __/ | | | |_| | (_) | | | |  __/_|
    \_/\_/ \___|_|_| |____/ \___/|_| |_|\___(_)
                                                                                             
        """ + style.END)


def game_over():
    print(style.RED +
          """
   ____                         ___                 _ 
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)
                                                      
        """ + style.END)


def replay_game():
    while True:
        response = input("Would you like to play again? Y/N ").upper()
        if response == "Y":
            play_game()
        elif response == "N":
            main_menu()
        else:
            print("You must press Y or N")


def play_game():
    clear_terminal()
    word = get_word()
    play(word)


main_title()
main_menu()
