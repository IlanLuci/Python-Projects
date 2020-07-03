import constants as c
import pygame
import warnings
import time

warnings.filterwarnings("ignore", category = DeprecationWarning)

class Brick():
    def __init__(self):
        self.brick = pygame.image.load("brick.png").convert()
        self.brick_size = self.brick.get_rect()
        self.brick_length = self.brick_size.right - self.brick_size.left
        self.brick_height = self.brick_size.bottom - self.brick_size.top
    def build_bricks(self):
        self.bricklist = []
        brick_pos_x = 0
        shouldweoffset = True
        brick_pos_y = 40
        for x in range(c.BRICK_NUM):
            if brick_pos_x >= c.DISPLAYSIZEX:
                brick_pos_y += self.brick_height
                if shouldweoffset:
                    brick_pos_x = - self.brick_length / 2
                    shouldweoffset = False
                else:
                    shouldweoffset = True
                    brick_pos_x = 0
            self.bricklist.append(self.brick_size)
            self.bricklist[x] = self.bricklist[x].move(brick_pos_x, brick_pos_y)
            brick_pos_x += self.brick_length

class Main():
    def main(self):
        #pygame init
        pygame.init()
        pygame.display.set_caption("Atari Breakout")
        screen = pygame.display.set_mode((c.DISPLAYSIZEX, c.DISPLAYSIZEY))
        screen.fill((255, 255, 255))
        pygame.mouse.set_visible(0)
        pygame.key.set_repeat(1, 30)
        pygame.display.update()

        #load images
        circle = pygame.image.load("circle.png")
        circle_size = circle.get_rect()
        bat = pygame.image.load("bat.png")
        bat_size = circle.get_rect()

        #load sound
        sound = pygame.mixer.Sound("sound.wav")
        sound.set_volume(100)

        #general variables
        clock = pygame.time.Clock()
        fontStyle = pygame.font.SysFont("ariel", 30)

        #User variables
        score = 0
        num_lives = 5

        #speed and position
        speed_y = c.SPEED_Y
        speed_x = c.SPEED_X
        circle_size = circle_size.move((c.DISPLAYSIZEX - 50) / 2, (c.DISPLAYSIZEY - 50) / 2)
        bat_size = bat_size.move((c.DISPLAYSIZEX - 100) / 2, c.DISPLAYSIZEY - 50)

        brick = Brick()
        brick.build_bricks()

        while num_lives > 0:
            clock.tick(c.TICK_SPEED)
            #Events
            for x in pygame.event.get():
                #Quit If You Click X
                if x.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Movement
                if x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_LEFT and bat_size.left > 0:
                        bat_size = bat_size.move(-c.BAT_SPEED, 0)
                    elif x.key == pygame.K_RIGHT:
                        bat_size = bat_size.move(c.BAT_SPEED, 0)
                        if bat_size.right > c.DISPLAYSIZEX:
                            bat_size.right = c.DISPLAYSIZEX
            
            #Move Objects
            if circle_size.bottom >= bat_size.top and circle_size.center[0] >= bat_size.left and circle_size.center[0] <= bat_size.right + 50 and circle_size.bottom <= bat_size.bottom:
                batoffset = bat_size.center[0] - circle_size.center[0]
                if batoffset < 0:
                    speed_x = c.SPEED_X + 1
                if batoffset > 0:
                    speed_x = -c.SPEED_X - 1
                speed_y = -speed_y
                sound.play(0)
            circle_size = circle_size.move(speed_x, speed_y)
            if circle_size.left <= 0 or circle_size.right >= c.DISPLAYSIZEX:
                speed_x = -speed_x
                sound.play(0)
            if circle_size.top <= 0:
                speed_y = -speed_y
                sound.play(0)
            if circle_size.bottom >= c.DISPLAYSIZEY:
                num_lives -= 1
                circle_size.center = (c.DISPLAYSIZEX - 50) / 2, (c.DISPLAYSIZEY - 50) / 2
                speed_x = c.SPEED_X
                speed_y = c.SPEED_Y
                sound.play(0)
            collideelement = circle_size.collidelist(brick.bricklist)
            if collideelement != -1:
                if circle_size.center[0] < brick.bricklist[collideelement].left or circle_size.center[0] > brick.bricklist[collideelement].right:
                    speed_x = -speed_x
                else: 
                    speed_y = -speed_y
                brick.bricklist[collideelement : collideelement + 1] = []
                score += 1
                sound.play(0)
            
            #Update Objects
            screen.fill((255, 255, 255))
            if score >= c.BRICK_NUM:
                blit_win_message = fontStyle.render("You Win!", True, (0, 0, 0))
                screen.blit(blit_win_message, [c.DISPLAYSIZEX / 2 - 50, c.DISPLAYSIZEY / 2 - 15])
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
                quit()
            blitMessage1 = fontStyle.render("Your Score Is " + str(score), True, (0, 0, 0))
            screen.blit(blitMessage1, [c.MARGIN, c.MARGIN])
            blitMessage2 = fontStyle.render("You have " + str(num_lives) + " lives", True, (0, 0, 0))
            blitMessage2_size = blitMessage2.get_rect()
            screen.blit(blitMessage2, [c.DISPLAYSIZEX - blitMessage2_size.right - c.MARGIN, c.MARGIN])
            screen.blit(circle, circle_size)
            screen.blit(bat, bat_size)
            for x in range(len(brick.bricklist)):
                if brick.bricklist[x] != []:
                    screen.blit(brick.brick, brick.bricklist[x])
            pygame.display.update()

if __name__ == "__main__":
    game = Main()
    game.main()