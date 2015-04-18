'''
Created on Apr 4, 2015

@author: 1upde_000
'''
from src.GameObject import GameObject


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
        self.myH = 50
        self.myW = 50
        
    
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