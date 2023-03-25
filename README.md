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

KNOWN Error
These two functions are not working
list_of_guesses
word_gussed 

