"""
Hangman Game
"""

import random
import time

def readwords():
    with open("words.txt") as file_in:
        words = []
        for x in file_in:
            words.append(x.strip("\n"))
    return words

def randomWord(wordList):
    return random.choice(wordList)

def play():
    name = input("What is your name? ")
    print("")
    hangman = input("Hello " + name + ", do you want to play hangman? ")
    print("")
    time.sleep(1)
    word = randomWord(readwords())
    numGuesses = input("Ok. How many guesses do you want? ")
    if numGuesses.isdigit():
        numGuesses = int(numGuesses)
    else:
        numGuesses = input("Please input a valid number." " Ok. How many guesses do you want? ")
    lettersGuessed = []
    correctGuesses = []

    while numGuesses > 0:
        gameOver = 0
        for x in word:
            if x in correctGuesses:
                print(x, end = "")
            else:
                print("_", end = "")
                gameOver += 1 
        if gameOver == 0:
            print(" Good Job! You won.")
            break
        guess = input(" What is your guess ")
        if guess not in word:
            if guess not in lettersGuessed:
                numGuesses -= 1
                lettersGuessed.append(guess)
                print("Wrong Answer")
                print("You have " + str(numGuesses) + " guesses left.")
                if numGuesses == 0:
                    print("Game Over")
                    print("The word was " + word + " .")
            elif guess in lettersGuessed:
                print("You already guessed that letter")
        else:
            correctGuesses.append(guess)
            print("Correct Answer!")
            
play()