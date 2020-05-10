"""
Name: High Low

Purpose: Computer guesses number that user is thinking about
"""

def highLow(minimum, maximum):  
    computerCorrect = False
    guesses = 1
    while not computerCorrect:
        meanvar = int((minimum + maximum) / 2)
        userInput = input("My guess is: " + str(meanvar) + " Too Low(tl) Too High(th) or Just Right(jr)")
        if userInput == "tl":
            minimum = meanvar
        elif userInput == "th":
            maximum = meanvar
        elif userInput == "jr":
            computerCorrect = True
        else:
            print("Please only use tl, th, or jr")
        guesses += 1 
    print("Correct! Good Job!")
    print("It took " + str(guesses) + " Guesses")
#main function
def main():
    #asks the user for the minimun number they want to use
    minimum = int(input("What is the minumum value?"))
    #asks the user for the maximum number they want to use
    maximum = int(input("What is the maximum value?"))
    highLow(minimum, maximum)

    again = input("Play again? y/n")

    while again == "y":
        highLow(minimum, maximum)
        again = input("Play again? y/n")
    print("Ok")
#starts main function
main()