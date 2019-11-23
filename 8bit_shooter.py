# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from CharDesign import *

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30
Y_MIN = 350
Y_MAX = 50
X_MIN = 20
X_MAX = 750
MOVE = 4

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption("ARE YOU READY PLAYER ONE?")
 
# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0,0), "pictures/8bit_background.jpg")
playerOne = player(window, 300, Y_MIN)
enemy1 = enemy(window, 100, Y_MIN)

# 5 - Initialize variables
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
            playerOne.x_cord += MOVE
            if playerOne.x_cord > X_MAX:
                playerOne.x_cord = X_MAX
            print("X POSITION", playerOne.x_cord)
        

    if keyList[K_LEFT]:
            playerOne.x_cord -= MOVE
            if playerOne.x_cord < X_MIN:
                playerOne.x_cord = X_MIN
            print("X POSITION", playerOne.x_cord)

    # 8 - Do any "per frame" actions
    playerOne.update()
    
    # 9 - Clear the screen
    #window.fill(BLACK)
    
    # 10 - Draw all screen elements
    background.draw()
    playerOne.draw()
    enemy1.draw()
    
    # 11 - Update the screen
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount




