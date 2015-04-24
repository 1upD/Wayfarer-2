'''
Created on Apr 14, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject
from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH

class Resource(DynamicObject):
    '''
    classdocs
    '''

    myType = "Resource"
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25
        
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [0, 0, 255], [self.myX, self.myY, self.myW, self.myH])