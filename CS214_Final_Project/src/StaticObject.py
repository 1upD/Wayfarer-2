'''
Created on Apr 4, 2015

@author: 1upde_000
'''
from src.GameObject import GameObject
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT


class StaticObject(GameObject):
    '''
    classdocs
    '''
    _type = "Static Object"
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        
    
    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self._x = x
        self._y = y
        self._h = w
        self._y = h
        
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, 0, [self._x, self._y, self._w, self._h])