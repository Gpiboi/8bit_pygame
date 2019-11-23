from time import time
from pygwidgets import *

class Character:

    def __init__(self):
        pass

    def attacked(self):
        self.life -= 5

    def draw(self):
        self.image.draw()

    def update(self):
        self.image = Image(self.window, (self.x_cord, self.y_cord), self.picture)
        return self.image

class enemy(Character):


    def __init__(self, window, x_cord, y_cord):
        self.health = 20
        self.picture = "pictures/8bit_enemy.png"
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.window = window
        self.image = Image(self.window, (self.x_cord, self.y_cord), self.picture)

class player(Character):


    def __init__(self, window, x_cord, y_cord):
        #self.username = username
        self.health = 50
        self.picture = "pictures/8bit_player.png"
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.window = window
        self.image = Image(self.window, (self.x_cord, self.y_cord), self.picture)

