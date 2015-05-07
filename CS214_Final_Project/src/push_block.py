'''
Created on Apr 29, 2015

@author: 1upde_000
'''
from src import DynamicObject
from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH

class push_block(DynamicObject.DynamicObject):
    '''
    models a block which can be moved by the player or by an NPC
    '''
    
    _type = "pushable"
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25 - 4
        self.myW = WINDOW_WIDTH / 25 - 4
        self.myDX = 0
        self.myDY = 0
    
    def step(self):
        DynamicObject.DynamicObject.step(self)
        self.myDY /= 2
        self.myDX /= 2
                
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, 100, [self.myX, self.myY, self.myW, self.myH])   