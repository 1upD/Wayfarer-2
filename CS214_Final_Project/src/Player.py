'''
Created on Apr 5, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject
from src.Character import Character
from src.Globals import WINDOW_HEIGHT
from src.Globals import WINDOW_WIDTH
from src.sprite import sprite

class Player(Character):
    '''
    classdocs
    '''

    _type = "Player"
    direction = 0
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        self.sprite = sprite("images/player/walking.dat")

    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self._x = x
        self._y = y
        self._h = w
        self._y = h
    

    def draw(self, gameDisplay, draw):
        # Choose a direction based on player speed
        if self._dx > 0 and self._dy == 0:
            self.direction = 0
        elif self._dx > 0 and self._dy < 0:
            self.direction = 45
        elif self._dx == 0 and self._dy < 0:
            self.direction = 90
        elif self._dx < 0 and self._dy < 0:
            self.direction = 135
        elif self._dx < 0 and self._dy == 0:
            self.direction = 180
        elif self._dx < 0 and self._dy > 0:
            self.direction = 225
        elif self._dx == 0 and self._dy > 0:
            self.direction = 270
        elif self._dx > 0 and self._dy > 0:
            self.direction = 315
        
        # Set sprite speed
        if self._dx == 0 and self._dy == 0:
            self.sprite.set_rate(0)
        else:
            self.sprite.set_rate(1)
        # Draw the sprite
        self.sprite.draw_with_direction(gameDisplay, self.direction, self._x, self._y)

        # Draw the H20 bar
        draw.rect(gameDisplay, [0, 0, 255, 100], [25, 25, self._water / 5, 10])
        
    def changeLocation(self, location):
        ''' Dummy definition '''
        
    def perceive(self, staticObjects, dynamicObjects, x, y):
        ''' Dummy definition '''
