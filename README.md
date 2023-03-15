# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

created a list with 5 fruits name and pick a random word
    word_list = ['apple', 'lemon', 'orange', 'strawberry', 'dragonfruit']
    word = random.choice(word_list)
    print(word)
a user input a single alphabet letter
    guess = input("Enter a single letter ")

return an alart message if the input was more than 1 word or non-alphabet character.

check_guess function changes the input to lower key alphabet
After that, if the alphabet is in the word, it prints "good guess",
if not, it prints out "sorry". 
If it's yes, 
        def check_guess(guess):
            guess = guess.lower()
            if guess in word:
                print(f"Good guess {guess} is in the word")
            else:
                print(f"Sorry,{guess} is not in the word")

ask_for_input function checks the input is a single letter,
and it run through the check_guess function.
if the input doesn't follow meet the requirement, it prints out "invalid message"

        def ask_for_input():
            while True:
                if len(guess) > 1 or guess.isalpha() != True:
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    break
                elif (len(guess) == 1 and guess.isalpha() == True):
                    check_guess(guess)
                    break
        ask_for_input() 


