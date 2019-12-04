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
DEBUG = False


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

pBullets = []


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:        
            pygame.quit()  
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pBullets.append( Bullet(window, playerOne.x) )
                

    keyList = pygame.key.get_pressed()

    if keyList[K_RIGHT]:
        playerOne.update("right")

    if keyList[K_LEFT]:
        playerOne.update("left")

    time_for_renewal = renewal.update()

    #------------------Enemy Spawn-------------------
    if len(enemies) < ENEMY_MAX and time_for_renewal:
        enemy_x_cord_start -= 100
        new_enemy = Enemy(window, enemy_x_cord_start)
        enemies.append(new_enemy)
        renewal.start()


    # 8 - Do any "per frame" actions
    if len(enemies) > 1 and len(pBullets) > 1:
        print("Loc (enemy):", enemies[0].x, "; loc (bullet):", pBullets[0].x)
        if pBullets[0].x == enemies[0].x:
                print("!!!Cross!!!")
                enemies[0].attacked()
                print(enemies[0].health)
                del pBullets[0]
                del bullet
                continue
        
    # 9 - Clear the screen
    
    # 10 - Draw all screen elements
    background.draw()

    shouldAdvance = advances.update()
    
    for enemy in enemies:
        if shouldAdvance:
            enemy.advance()
            advances.start()
        #------Enemy dies------
        if enemy.death():
            enemies.remove(enemy)
            del enemy
            ENEMY_MAX -= 1
            enemy_x_cord_start = enemies[-1].x + 100
            renewal.start()
            continue
        enemy.draw()
        
    playerOne.draw()

    for bullet in pBullets:
        bullet.update()
        bullet.draw()

        if bullet.offScreen:
            pBullets.remove(bullet)
            del bullet
            
            

    if DEBUG:   print(len(pBullets))
    
    
    # 11 - Update the screen
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
