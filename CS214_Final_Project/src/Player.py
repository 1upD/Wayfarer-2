'''
Created on Apr 5, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject
from src.Character import Character

class Player(Character):
    '''
    classdocs
    '''

    myType = "Player"
    
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
        draw.rect(gameDisplay, [255, 0, 0], [self.myX, self.myY, self.myW, self.myH])
        draw.rect(gameDisplay, [0, 255, 0, 100], [self.myX, self.myY, self.water / 60, self.myH])
        
        
    def changeLocation(self, location):
        ''' Dummy definition '''
        
    def perceive(self, staticObjects, dynamicObjects):
        ''' Dummy definition '''