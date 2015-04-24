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
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25
        
    
    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = w
        self.myY = h
        
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, 0, [self.myX, self.myY, self.myW, self.myH])