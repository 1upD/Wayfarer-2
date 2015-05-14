'''
Created on May 14, 2015

@author: Derek Dik
'''
from src.StaticObject import StaticObject

class EndTrigger(StaticObject):
    '''
    A special block that ends the game after the player steps on it
    '''
    
    def __init__(self, x, y):
        StaticObject.__init__(self, x, y)
        self._type = "Victory"
