'''
Created on May 14, 2015

@author: 1upde_000
'''
from src.StaticObject import StaticObject

class EndTrigger(StaticObject):
    '''
    A special block that ends the game after the player steps on it
    '''
    
    def __init__(self, x, y):
        StaticObject.__init__(self, x, y)
        _type = "Victory"
