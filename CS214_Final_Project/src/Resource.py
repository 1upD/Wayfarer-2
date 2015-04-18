'''
Created on Apr 14, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject

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
        self.myH = 50
        self.myW = 50
        
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [0, 0, 255], [self.myX, self.myY, self.myW, self.myH])