guess = input("Enter a single letter ")


while(True):
    if len(guess) > 1 or guess.isalpha() != True:
     print("Invalid letter. Please, enter a single alphabetical character.")
    else:
       len(guess) == 1 and guess.isalpha() == True
       break 
    