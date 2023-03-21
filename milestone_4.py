class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.num_letters = num_letters
        self.word_guessed = word_guessed
        self.list_of_guesses = list_of_guesses


import random

word_list = ['apple', 'lemon', 'orange', 'strawberry', 'dragonfruit']
word = random.choice(word_list)
guess = input("Enter a single letter ")

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess {guess} is in the word")
    else:
        print(f"Sorry,{guess} is not in the word")

def ask_for_input():
    while True:
        if len(guess) > 1 or guess.isalpha() != True:
            print("Invalid letter. Please, enter a single alphabetical character.")
            break
        elif (len(guess) == 1 and guess.isalpha() == True):
            check_guess(guess)
            break
ask_for_input

