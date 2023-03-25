# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

You have 5 attempts to guess a word related to fruits.
If you guess correctly, the "_"(under_score) will change it to the alphabet.
If you didn't guess correctly, your number of lives will decrease by 1
Please make sure to type single alphabet character, otherwise computer won't recognise your input.


#Hangman class has 2 parameter. (word_list, and num_lives)
There are few other attributes under the initialization 

There are 2 main methods called ask_for_input and check_guess
ask_for_input filters the player's input and make sure they haven't input the alphabet yet.
after that, check_guess filter following requirements
For example, 
   if len(guess) > 1 or guess.isalpha() != True:
   if the input is not alphabet, it won't play the game. 
   if the input is more than 1 character, it won't play the game.  


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list) #choose a random word from a list
        self.num_lives = num_lives
        self.word_guessed = ["_"]*len(self.word) #create blank underscores for the chosen word
        self.num_letters = len(list(set(self.word)))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = str.lower(guess)
        word_lower = str.lower(self.word)
        guess_count = word_lower.count(guess) #counting how many letters in the chosen word

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
                letter_index = word_lower.index(guess, letter_indices[-1]+1) #what is this "+1"??
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

