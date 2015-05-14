'''
Created on Apr 14, 2015

@author: Derek Dik
'''

from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH
from src.StaticObject import StaticObject
from src.GameTimer import get_time
from math import floor

class Resource(StaticObject):
    '''
    Models a dispenser from which a user can refill water
    '''

    _type = "Resource"
    _resource_value = 0
    _color = [0, 0, 255]
    _color_deactived = [100, 100, 200]
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.last_use = -600
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        self._cooldown = 600
        self._sprite.set_rate(0)
    def get_water(self):
        game_time = get_time()
        if game_time - self.last_use > self._cooldown:
            self.last_use = game_time
            return self._resource_value
        else:
            return 0
    def draw(self, gameDisplay, draw):
        time_elapsed = get_time() - self.last_use
        if time_elapsed < self._cooldown:
            self._sprite.set_frame(floor(time_elapsed / 100))
            # I am going to cheat and put this logic in the draw loop. It will save a ton of step() calls
            # self._cooldown += 1
        else:
            self._sprite.set_frame(5)
        self._sprite.draw(gameDisplay, self._x, self._y)