"""
2048
"""

#Update Colors

import pygame
import constants as c
import time
import math
import random

pygame.init()
fontStyle = pygame.font.SysFont("ariel", 30)
pygame.display.set_caption("2048")
screeen = pygame.display.set_mode((c.DISPLAYSIZEX, c.DISPLAYSIZEY))
pygame.display.update()
tilematrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
score = 0
screeen.fill(c.WHITE)

def main():
    gameover = False

    updatetilenums()
    updatetilenums()
    printmatrix()

    while gameover == False:

        #Events
        for x in pygame.event.get():
            #Quit If You Click X
            if x.type == pygame.QUIT:
                gameover = True
                pygame.quit()
                quit()
            if valturn() == True:
                if x.type == pygame.KEYDOWN:
                    rotatenum = arrowkeypress(x.key)
                    if rotatenum != None:
                        rotateMatrix(rotatenum)
                        shouldwemove = canmove()
                        if shouldwemove == True:
                            move()
                            merge()
                            updatetilenums()
                        rotateMatrix(4 - rotatenum)
                        printmatrix()
            else:
                uded()
        pygame.display.update()


def printmatrix():
    global score
    screeen.fill(c.WHITE)
    for x in range(c.MATRIXLENGTH):
        for y in range(c.MATRIXLENGTH):
            pygame.draw.rect(screeen, c.WHITE, [(c.DISPLAYSIZEX / c.MATRIXLENGTH) * x - 10, (c.DISPLAYSIZEX  / c.MATRIXLENGTH) * y + 90, c.DISPLAYSIZEX / c.MATRIXLENGTH + 20, c.DISPLAYSIZEX / c.MATRIXLENGTH + 20])
            pygame.draw.rect(screeen, c.getcolor(tilematrix[x][y]), [(c.DISPLAYSIZEX / c.MATRIXLENGTH) * x, (c.DISPLAYSIZEX  / c.MATRIXLENGTH) * y + 100,
            c.DISPLAYSIZEX / c.MATRIXLENGTH, c.DISPLAYSIZEX / c.MATRIXLENGTH])
            blitMessage = fontStyle.render(str(tilematrix[x][y]), True, c.WHITE)
            screeen.blit(blitMessage, [(c.DISPLAYSIZEX / c.MATRIXLENGTH) * x + c.MATRIXPADDINGX, (c.DISPLAYSIZEX  / c.MATRIXLENGTH) * y + c.MATRIXPADDINGY])

            #Draw Score text
            blitMessage1 = fontStyle.render("Your Score Is " + str(score), True, c.BLACK)
            screeen.blit(blitMessage1, [20, 20])

def updatetilenums():
    global tilematrix

    randnum = random.randint(0, c.MATRIXLENGTH - 1)
    randnum1 = random.randint(0, c.MATRIXLENGTH - 1)

    while tilematrix[randnum][randnum1] != 0:
        randnum = random.randint(0, c.MATRIXLENGTH - 1)
        randnum1 = random.randint(0, c.MATRIXLENGTH - 1)
    tilematrix[randnum][randnum1] = 2

def valturn():
    for x in range(c.MATRIXLENGTH):
        for y in range(c.MATRIXLENGTH):
            if tilematrix[x][y] == 0:
                return True
    for x in range(c.MATRIXLENGTH):
        for y in range(c.MATRIXLENGTH - 1):
            if tilematrix[x][y + 1] == tilematrix[x][y] or tilematrix[y + 1][x] == tilematrix[y][x]:
                return True
    return False

def arrowkeypress(key):
    if key == pygame.K_UP:
        rotations = 0
    elif key == pygame.K_LEFT:
        rotations = 1
    elif key == pygame.K_DOWN:
        rotations = 2
    elif key == pygame.K_RIGHT:
        rotations = 3
    else:
        rotations = None
    return rotations

def rotateMatrix(rotations):
    global tilematrix
    #Number Of Rotations
    for x in range(rotations):
        #Number Of Cycles
        for y in range(int(c.MATRIXLENGTH / 2)):
            #Loops for the length of current cycle
            for z in range(y, c.MATRIXLENGTH - y - 1):
                tempval1 = tilematrix[y][z]
                tempval2 = tilematrix[c.MATRIXLENGTH - 1 - z][y]
                tempval3 = tilematrix[c.MATRIXLENGTH - 1 - y][c.MATRIXLENGTH - 1 - z]
                tempval4 = tilematrix[z][c.MATRIXLENGTH - 1 - y]
                tilematrix[c.MATRIXLENGTH - 1 - z][y] = tempval1
                tilematrix[c.MATRIXLENGTH - 1 - y][c.MATRIXLENGTH - 1 - z] = tempval2
                tilematrix[z][c.MATRIXLENGTH - 1 - y] = tempval3
                tilematrix[y][z] = tempval4

def canmove():
    global tilematrix
    for x in range(c.MATRIXLENGTH):
        for y in range(1, c.MATRIXLENGTH):
            if tilematrix[x][y] != 0 and tilematrix[x][y - 1] == 0:
                return True
            elif tilematrix[x][y] == tilematrix[x][y - 1] and tilematrix[x][y] != 0:
                return True
    return False

def move():
    global tilematrix
    for x in range(c.MATRIXLENGTH):
        for y in range(c.MATRIXLENGTH - 1):
            while tilematrix[x][y] == 0 and sum(tilematrix[x][y:]) > 0:
                for z in range(y, c.MATRIXLENGTH - 1):
                    tilematrix[x][z] = tilematrix[x][z + 1]
                tilematrix[x][c.MATRIXLENGTH - 1] = 0

def merge():
    global tilematrix
    global score
    for x in range(c.MATRIXLENGTH):
        for y in range(c.MATRIXLENGTH - 1):
            if tilematrix[x][y] == tilematrix[x][y + 1] and tilematrix[x][y] != 0:
                tilematrix[x][y] = tilematrix[x][y] * 2
                tilematrix[x][y + 1] = 0
                score += tilematrix[x][y]
                move()

def uded():
    global score
    blitMessage = fontStyle.render("Hehe You Lost.", True, c.BLACK)
    screeen.blit(blitMessage, [130,50])
    blitMessage2 = fontStyle.render("You Only Got A Score Of " + str(score), True, c.BLACK)
    screeen.blit(blitMessage2, [55,70])

main()