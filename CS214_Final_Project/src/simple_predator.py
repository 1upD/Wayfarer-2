'''
Created on Apr 29, 2015

@author: Derek Dik
'''
from src import DynamicObject
from _random import Random
from random import random, randint
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT

class simple_predator(DynamicObject.DynamicObject):
    '''
    models a simple creature that will move with random direction
    '''
    _type = "predator"
    move_counter = 0
    def __init__(self, x, y):
        '''
        Constructor
        '''
        super()
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25 
        self.myDY = randint(-2, 2)
        self.myDX = randint(-2, 2)       
        
    def step(self):
        DynamicObject.DynamicObject.step(self) 
        self.move_counter += 1
        if self.move_counter == 30:
            self.myDY = randint(-2, 2)
            self.myDX = randint(-2, 2)
            self.move_counter = 0
   
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [255, 0, 0], [self.myX, self.myY, self.myW, self.myH])  
        