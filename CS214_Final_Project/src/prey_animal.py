'''
Created on Apr 29, 2015

@author: Derek Dik
'''
from src import DynamicObject
from _random import Random
from random import random, randint
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT
from src.sprite import sprite

class prey_animal(DynamicObject.DynamicObject):
    '''
    models a simple creature that will move with random direction
    '''

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
        self._sprite = sprite("images\\swarm\\swarm.dat")  
        
    def step(self):
        DynamicObject.DynamicObject.step(self) 
        self.move_counter += 1
        if self.move_counter == 30:
            self._dy = randint(-2, 2)
            self._dx = randint(-2, 2)
            self.move_counter = 0