import random


class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 5
        self.word = list(random.choice(self.word_list).lower)
        self.num_letters = len(set(self.word))
        self.word_guessed = ["_"]*len(self.word)
        self.list_of_guesses = []

        print(f"The mystery word has:  {len(self.word)} characters")
        print(f"{self.word_guessed}")
        pass


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

