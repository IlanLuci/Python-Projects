"""
Name: Guess the number

Purpose: Computer thinks of random number from 1-100 and the user will guess 
what it is. Than the computer will say 'too high' or 'too low'
"""


#imports the random library
import random

#sets the variable num to a random integer
num = random.randint(1, 101)

correct = False

while correct == False:
    userInput = input("Guess The Number")

    if userInput == num:
        correct = True 
    elif userInput > num:
        print("Too High")
    else:
        print("Too Low")

print("You're Correct!")