import random

word_list = ['apple', 'lemon', 'orange', 'strawberry', 'dragonfruit']
word = random.choice(word_list)
guess = input("Enter a single letter ")

while(True):
    len(guess) > 1 or guess.isalpha() != True
    print("Invalid letter. Please, enter a single alphabetical character.")
    if (len(guess) == 1 or guess.isalpha() == True):
        break
    

if guess in word:
    print(f"Good guess {guess} is in the word")
else:
    print(f"Sorry,{guess} is not in the word")