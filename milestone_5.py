import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_guessed = ["_"]*len(self.word)
        # for i in range(len(self.word)):
        #     self.word_guessed.append('_')
        self.num_letters = len(list(set(self.word)))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
               if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses.append(guess)

    def ask_for_input(self):
     while True:
        guess = input("Enter a single letter ")
        if len(guess) != 1 or guess.isalpha() != True:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            break


def play_game(word_list):
    num_lives = 5
    game = Hangman
    game(word_list, num_lives) 

    while(True):
        if num_lives == 0:
            print("You lost!")
        elif Hangman.num_letters > 0:
            Hangman.ask_for_input() 
        elif num_lives != 0 and not Hangman.num_letters >= 0 :
            print("Congratulations. You won the game!")




word_list = ["apple"]
hangman = Hangman(word_list)
play_game(["apple"])
    