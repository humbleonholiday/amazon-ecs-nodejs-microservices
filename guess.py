#!/usr/bin/env python3.7

print("**********************************************")
print("welcome to the guessing numbers game!")
print("Guess the correct number from 0 to 100")
print("**********************************************")

print("Hello Harrison and Benjamin!")

import random

#if c else if q quit, else anything else repeat the question
play_game = input("Press (c) to continue or (q) to quit:")

while play_game != "q": 
    won = "no"
    #generate number
    print("Generating random number")
    correct_number=random.randint(0,100)
    print(correct_number)
    
    while won != "yes":
        my_guess = input("Type in your number:")

        while my_guess.isnumeric() != True: 
            my_guess = input("Please type an *integer* from 0 to 100:")

        if int(my_guess) == correct_number:
            print("Well done!")
            won = "yes"
            play_game=input("Press (c) to continue or (q) to quit:")
            print(play_game)
        else:
            if int(my_guess) < correct_number:
                print("unlucky, try a higher number")
            else:
                print("unlucky, try a lower number")


print("Quitting game, goodbye!")


