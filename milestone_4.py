import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = list(random.choice(self.word_list).lower)
        self.num_lives = num_lives
        self.word_guessed = []
        for i in xrange(len(self.word)):
            self.word_guessed.append('-')
        self.num_letters = len(set(self.word)) - self.word_guessed
        self.list_of_guesses = []
