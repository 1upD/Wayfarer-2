'''
Created on Apr 29, 2015

@author: Derek Dik
'''
from src import DynamicObject
from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH
from src.Sprite import Sprite

class PushBlock(DynamicObject.DynamicObject):
    '''
    models a block which can be moved by the player or by an NPC
    '''
    
    _type = "pushable"
    _sprite = Sprite("images\\block\\block.dat")
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25 - 4
        self._w = WINDOW_WIDTH / 25 - 4
        self._dx = 0
        self._dy = 0
    
    def step(self):
        DynamicObject.DynamicObject.step(self)
        self._dy /= 2
        self._dx /= 2
                
    def draw(self, gameDisplay, draw):
        self._sprite.draw(gameDisplay, self._x, self._y)   