"""
Snake Game 

design bg and UI
Random spawn apples on a grid 
snake that moves with arrow keys 
apples disapear and score increases by one when snake and apple colide
when the snake collides with the boundary or itself destroy the snake and end the game

Static objects:
	background
	apples
Dynamic Objects:
	snake 
"""

import pygame
import random
import time
import constants as c

pygame.init()
fontStyle = pygame.font.SysFont("ariel", 30)

pygame.display.set_caption("Snake")
screeen = pygame.display.set_mode((c.DISPLAYSIZE, c.DISPLAYSIZE))
pygame.display.update()
clock = pygame.time.Clock()

def update():
    gameOver = False
    gameTotallyOver = False
    score = 0
    startingX = c.DISPLAYSIZE / 2
    startingY = c.DISPLAYSIZE / 2
    xMovement = 0
    yMovement = 0
    applelocx = round(random.randrange(0 + c.SNAKESIZE, c.DISPLAYSIZE - c.SNAKESIZE) / 10.0) * 10.0
    applelocy = round(random.randrange(0 + c.SNAKESIZE, c.DISPLAYSIZE - c.SNAKESIZE) / 10.0) * 10.0
    snakeloc = []
    length_of_snake = 1
    while gameTotallyOver == False:
        while gameOver == True:
            uDed()
            for x in pygame.event.get():
                if x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_q:
                        gameOver = False
                        gameTotallyOver = True
                    elif x.key == pygame.K_p:
                        update()
                if x.type == pygame.QUIT:
                    gameOver = False
                    gameTotallyOver = True

        #Events
        for x in pygame.event.get():
            #Quit If You Click X
            if x.type == pygame.QUIT:
                gameTotallyOver = True
            #Movement
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_LEFT:
                    xMovement = -c.MOVE
                    yMovement = 0
                elif x.key == pygame.K_RIGHT:
                    xMovement = c.MOVE
                    yMovement = 0
                elif x.key == pygame.K_UP:
                    yMovement = -c.MOVE
                    xMovement = 0
                elif x.key == pygame.K_DOWN:
                    yMovement = c.MOVE
                    xMovement = 0

        #Die When Hit Wall
        if startingX < 0 or startingX > c.DISPLAYSIZE or startingY < 0 or startingY > c.DISPLAYSIZE:
            gameOver = True

        #Background Color
        screeen.fill(c.BLUE)

        #Move snake
        startingX = startingX + xMovement
        startingY = startingY + yMovement

        #Snake Array
        snakehead = [startingX, startingY]
        snakeloc.append(snakehead)
        if len(snakeloc) > length_of_snake:
            del snakeloc[0]
        
        #Snake Collision With Itself
        for x in snakeloc[:-1]:
            if snakehead == x:
                gameOver = True

        #Draw Snake
        drawsnake(snakeloc)

        #Draw Score
        drawscore(score)

        #Draw Apple
        pygame.draw.rect(screeen, c.RED, [applelocx, applelocy, c.SNAKESIZE, c.SNAKESIZE])

        #Update Display
        pygame.display.update()

        #Apple and Snake Collision 
        if abs(startingX-applelocx) <= 10 and abs(startingY-applelocy) <= 10:
            applelocx = round(random.randrange(0 + c.SNAKESIZE, c.DISPLAYSIZE - c.SNAKESIZE) / 10.0) * 10.0
            applelocy = round(random.randrange(0 + c.SNAKESIZE, c.DISPLAYSIZE - c.SNAKESIZE) / 10.0) * 10.0
            score += 1
            length_of_snake += 1

        clock.tick(c.SPEED)

    pygame.quit()
    quit()

def uDed():
    blitMessage = fontStyle.render("Game Over Press Q to quit or P to play again", True, c.BLACK)
    screeen.blit(blitMessage, [c.DISPLAYSIZE/4, c.DISPLAYSIZE/4])
    pygame.display.update()

def drawsnake(snakeloc):
    for x in snakeloc:
        pygame.draw.rect(screeen, c.GREEN, [x[0], x[1], c.SNAKESIZE, c.SNAKESIZE])

def drawscore(score):
    blitMessage = fontStyle.render("Score: " + str(score), True, c.BLACK)
    screeen.blit(blitMessage, [20,20])

update()
