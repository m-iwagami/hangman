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
        else:
            print(f"Sorry,{guess} is not in the word")
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


if __name__ == '__main__':
    word_list = ["apple"]
    hangman = Hangman(word_list)
    hangman.ask_for_input()
    print(hangman.word_guessed)
