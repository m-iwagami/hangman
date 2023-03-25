import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(list(set(self.word)))
        self.list_of_guesses = []
        
#%%
    def check_guess(self, guess):
        guess = str.lower(guess)
        word_lower = str.lower(self.word)
        guess_count = word_lower.count(guess)

        if guess_count == 1:
            letter_index = word_lower.index(guess)
            self.word_guessed[letter_index] = guess
            self.num_letters -= 1

            print(f"Good guess! {guess} is in the word.")
            print(self.word_guessed)

        elif guess_count > 1:
            letter_indices = []

            letter_index = word_lower.index(guess)
            letter_indices.append(letter_index)
            count = 1

            while count < guess_count:
                letter_index = word_lower.index(guess, letter_indices[-1]+1)
                letter_indices.append(letter_index)
                count += 1

            for i in letter_indices:
                self.word_guessed[i] = guess
            
            self.num_letters -= 1

            print(f'Nice! {guess} is in the word!')
            print(f'{self.word_guessed}')

        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
    


    def ask_for_input(self):
     while True:
        guess = input("Enter a single letter ")
        if len(guess) != 1 or guess.isalpha() != True:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            continue
        self.list_of_guesses.append(str.lower(guess))    
        self.check_guess(guess)
        break


def play_game(word_list):
    
    game = Hangman(word_list, num_lives=5)

    while game.num_lives > 0 and game.word_guessed.count('_') > 0:
        game.ask_for_input()

    if game.num_lives == 0:
        print("You lost!")
    if game.word_guessed.count('_') == 0:
        print("Congratulations. You won the game!")

        
if __name__ == '__main__':
    word_list = ["apple"]
    play_game(word_list)


# %%
