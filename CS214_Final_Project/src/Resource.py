'''
Created on Apr 14, 2015

@author: Derek Dik
'''

from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH, WATER_RESOURCE_VALUE
from src.StaticObject import StaticObject

class water_resource(StaticObject):
    '''
    Models a dispenser from which a user can refill water
    '''

    _type = "water_resource"
    resource_value = WATER_RESOURCE_VALUE
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        self.cooldown = 600
    def get_water(self):
        if self.cooldown == 600:
            self.cooldown = 0
            return self.resource_value
        else: 
            return 0
    def draw(self, gameDisplay, draw):
        if self.cooldown < 600:
            draw.rect(gameDisplay, [100, 100, 200], [self._x, self._y, self._w, self._h])
            # I am going to cheat and put this logic in the draw loop. It will save a ton of step() calls
            self.cooldown += 1
        else:
            draw.rect(gameDisplay, [0, 0, 255], [self._x, self._y, self._w, self._h])
            