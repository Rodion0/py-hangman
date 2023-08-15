import os
import time
import random
import json
import string

hangman_stages = [
    '''
            _________''',
    '''
                |
                |
                |
                |
                |
            ____|____''',
    ''' 
                |----
                |
                |
                |
                |
            ____|____''',
    '''     
                |----
                |   |
                |   
                |
                |
            ____|____''',
    '''
                |----
                |   |
                |   O
                |
                |
            ____|____''',
    ''' 
                |----
                |   |
                |   O
                |   |
                |
            ____|____''',
    ''' 
                |----
                |   |
                |   O
                |  /|\\
                |
            ____|____''',
    ''' 
                |----
                |   |
                |   O
                |  /|\\
                |  / \\
            ____|____''']


def get_random_word(list):
    word = random.choice(list)
    while (len(word) <= 2):
        word = random.choice(list)
    return word


def print_alphabet(previous_guesses):
    for char in string.ascii_lowercase:
        if char in previous_guesses:
            print('*', end=" ")
        elif char == 'm':
            print(char)
        else:
            print(char, end=" ")


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def init():
    with open("words_dictionary.json", "r") as read_file:
        data = json.load(read_file)
    word = get_random_word(list(data.keys()))
    return word


def main_game():
    passphrase = init()
    quit = False
    guessed_letters = ''.join([''+'_' for index in range(len(passphrase))])
    previous_guesses = []
    number_of_mistakes = 0
    print("Welcome to a simple game of hangman")
    wanna_play = input("Would you like to try your luck? y/n: ")
    if wanna_play == 'y':
        while (not quit):
            clear()
            if number_of_mistakes == len(hangman_stages) - 1:
                print(hangman_stages[number_of_mistakes])
                print(f"You lose! The word was {passphrase}")
                quit = True
                break
            elif guessed_letters == passphrase:
                print("You win!!!!!")
                quit = True
                break
            else:
                print("You will have 8 chances to choose the correct word. Otherwise you'll have to deal with the hangman. Type 'quit' to quit")
                print(hangman_stages[number_of_mistakes])
                print_alphabet(previous_guesses)
                print("\nYour current guesses: ", guessed_letters)
                guess = input("Please input a letter to guess: ")
                if guess.lower() == "quit":
                    quit = True
                elif len(guess) > 1 or not guess.isalpha():
                    print("[Error]: Please input a valid letter")
                    time.sleep(0.75)
                else:
                    if guess.lower() in previous_guesses:
                        print("You already guessed that!")
                        time.sleep(0.75)
                        continue
                    previous_guesses.append(guess.lower())
                    position = passphrase.find(guess.lower())
                    if position < 0:
                        print("Wrong Choice")
                        number_of_mistakes = number_of_mistakes + 1
                        time.sleep(0.75)
                    else:
                        if passphrase.count(guess.lower()) > 1:
                            positions = [pos for pos in range(
                                len(passphrase)) if passphrase.find(guess.lower(), pos) == pos]
                            for pos in positions:
                                guessed_letters = guessed_letters[:pos] + \
                                    guess.lower() + guessed_letters[pos + 1:]
                        else:
                            guessed_letters = guessed_letters[:passphrase.find(guess.lower(
                            ))] + guess.lower() + guessed_letters[passphrase.find(guess.lower()) + 1:]
    else:
        print("Probably the smart choice.")


if __name__ == "__main__":
    main_game()
