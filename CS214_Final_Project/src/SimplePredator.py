'''
Created on Apr 29, 2015

@author: Derek Dik
'''
from src import DynamicObject
from random import randint
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT
from src.Sprite import Sprite

class SimplePredator(DynamicObject.DynamicObject):
    '''
    models a simple creature that will move with random _direction
    '''
    _type = "predator"
    move_counter = 0
    def __init__(self, x, y):
        '''
        Constructor
        '''
        super()
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25 
        self._dy = randint(-2, 2)
        self._dx = randint(-2, 2)       
        self._sprite = Sprite("images\\bug\\bug.dat")  
        
    def step(self):
        DynamicObject.DynamicObject.step(self) 
        self.move_counter += 1
        if self.move_counter == 30:
            self._dy = randint(-2, 2)
            self._dx = randint(-2, 2)
            self.move_counter = 0
            
    def get_direction(self):
        # Choose a _direction based on object speed
        if self._dx > 0 and self._dy == 0:
            self._direction = 90
        elif self._dx > 0 and self._dy < 0:
            self._direction = 135
        elif self._dx == 0 and self._dy < 0:
            self._direction = 180
        elif self._dx < 0 and self._dy < 0:
            self._direction = 225
        elif self._dx < 0 and self._dy == 0:
            self._direction = 270
        elif self._dx < 0 and self._dy > 0:
            self._direction = 315
        elif self._dx == 0 and self._dy > 0:
            self._direction = 0
        elif self._dx > 0 and self._dy > 0:
            self._direction = 45
        return self._direction