# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from CharDesign import *
import pyghelpers
import pausef


# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30
ENEMY_MAX = 5


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption("ARE YOU READY PLAYER ONE?")
 
# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0,0), "pictures/8bit_background.jpg")
playerOne = player(window, 550)

# 5 - Initialize variables
renewal = pyghelpers.Timer(5)
renewal.start()

advances = pyghelpers.Timer(5)
advances.start()

enemy_x_cord_start = 200
enemies = []


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    keyList = pygame.key.get_pressed()

    if keyList[K_RIGHT]:
        playerOne.update("right")

    if keyList[K_LEFT]:
        playerOne.update("left")

    time_for_renewal = renewal.update()
    #print(time.getTime())

    if len(enemies) != ENEMY_MAX and time_for_renewal:
        enemy_x_cord_start -= 100
        new_enemy = Enemy(window, enemy_x_cord_start)
        enemies.append(new_enemy)
        renewal.start()

    shouldAdvance = advances.update()

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the screen
    
    # 10 - Draw all screen elements
    background.draw()
    
    for enemy in enemies:
        if shouldAdvance:
            enemy.advance()
            advances.start()
        enemy.draw()
        
    playerOne.draw()

    
    # 11 - Update the screen
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
