import random

word_list = ['apple', 'lemon', 'orange', 'strawberry', 'dragonfruit']
word = random.choice(word_list)
print(word)
guess = input("Enter a single letter ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


