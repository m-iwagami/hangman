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

    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")