from time import time
from pygwidgets import *

Y_MIN = 350
Y_MAX = 50
X_MIN = 20
X_MAX = 750
MOVE = 4

class Character:

    def __init__(self):
        pass

    def attacked(self):
        self.health -= 5

    def draw(self):
        self.image.draw()
        

class Enemy(Character):

    #MAX WINDOW FOR ENEMY OBJECTS
    x_max = 400

    def __init__(self, window, x):
        self.health = 20
        self.max = Enemy.x_max
        self.picture = "pictures/8bit_enemy.png"
        self.x = x
        self.y = Y_MIN
        self.window = window
        self.image = Image(self.window, (self.x, self.y), self.picture)
        Enemy.x_max -= 100
        

    def advance(self):
        self.x += 50
        if self.x > self.max:
            self.x = self.max
            
        self.image.setLoc((self.x, self.y))

    def death(self):
        if self.health < 0:
            Enemy.x_max += 100
            return True
        

class player(Character):


    def __init__(self, window, x):
        #self.username = username
        self.health = 50
        self.picture = "pictures/8bit_player.png"
        self.x = x
        self.y = Y_MIN
        self.window = window
        self.image = Image(self.window, (self.x, self.y), self.picture)

    def update(self, leftOrRight):
        if leftOrRight == 'right':
            self.x += MOVE
            if self.x > X_MAX:
                self.x = X_MAX
            #print("X POSITION", self.x_cord)
        else:
            self.x -= MOVE
            if self.x < X_MIN:
                self.x = X_MIN
            #print("X POSITION", self.x_cord)
                
        self.image.setLoc((self.x, self.y))


class Bullet(Character):

    def __init__(self, window, x):
        self.picture = "pictures/8bit_bullet.png"
        self.window = window
        self.x = x
        self.y = Y_MIN + 30
        self.startLoc = (self.x, self.y)
        self.image = Image(self.window, self.startLoc, self.picture)

    def update(self):
        
        self.x -= 10
        self.image.setLoc((self.x,self.y))
        
    @property
    def offScreen(self):
        return self.x < X_MIN
