import random
from words import word_list
import colorama
from colorama import Fore, Style

colorama.init()
def get_word():
    word = random.choice(word_list)
    return word.upper()


def game(word):
    word_completion = "_ " * len(word)
    guessed = False
    guessed_letters = []
    right_guessed_letters = []
    wrong_guessed_letters=[]
    guessed_letters_str = ""
    tries = 8
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input(f"Allowed Tries Left {tries}.Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                wrong_guessed_letters.append(guess)
            else:
                guessed_letters.append(guess)
                word_as_list = list(word_completion.replace(" ",""))
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = " ".join(word_as_list)
                right_guessed_letters.append(guess)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        guessed_letters_str = "".join((f"{Fore.GREEN}{row}" if row in right_guessed_letters else f"{Fore.RED}{row}"  for row in guessed_letters))
        print(f"Guessed Letters: {guessed_letters_str}{Style.RESET_ALL}")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_guessed_letters(guessed_letters,right_guessed_letters, wrong_guessed_letters):
    guessed_letters_str = ""
    for letter in guessed_letters:
        if letter in right_guessed_letters:
           guessed_letters_str =  guessed_letters_str.join(f"{Fore.GREEN}{letter}")
        elif letter in wrong_guessed_letters:
            guessed_letters_str = guessed_letters_str.join(f"{Fore.RED}{row} ")
        else:
            guessed_letters_str = guessed_letters_str.join(letter)
    return f"Guessed Letters: {guessed_letters_str}{Style.RESET_ALL}"

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # noose
                """
                   --------
                   |      |
                   |      
                   |    
                   |    
                   |     
                   -
                """,
                # upside L
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                #initial empty
                """
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        game(word)
    


if __name__ == "__main__":
    main()
