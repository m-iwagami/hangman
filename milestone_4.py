import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list['apple', 'lemon', 'orange', 'strawberry', 'dragonfruit']
        self.num_lives = num_lives
        self.word = list(random.choice(self.word_list).lower)
        self.num_letters = len(set(self.word))
        self.word_guessed = ["_"]*len(self.word)
        self.list_of_guesses = []
