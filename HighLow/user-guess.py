"""
Name: High Low

Purpose: Computer thinks of random number from 1-100 and the user will guess 
what it is. Than the computer will say 'too high' or 'too low'

You need a variable for the number than a funtion where the computer makes up a 
random number than the computer asks the user what number they guess and the user imputs
it the computer compares that with the actual number and says 'too high' or 'too low'
depending on comparison results than the user can guess again until they get it right 
(if statement)
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