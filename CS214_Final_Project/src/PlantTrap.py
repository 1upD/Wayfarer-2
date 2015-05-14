'''
Created on May 2, 2015

@author: Derek Dik
'''
from src.DynamicObject import DynamicObject
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT
from src.Sprite import Sprite

class PlantTrap(DynamicObject):
    '''
    PlantTrap models an enemy underground that springs up on contact with the player
    '''

    _type = "predator"
    def __init__(self, x, y):
        '''
        Constructor
        '''
        super()
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25 
        self._sprite = Sprite("images\plant\plant.dat")
        self._sprite.set_rate(0)       
    def step(self):
        DynamicObject.step(self)
        if self._opacity > 0:
            self._opacity -= 1
            
    def set_visible(self):
        self._sprite.set_rate(1)
    def draw(self, gameDisplay, draw):
        self._sprite.draw(gameDisplay, self._x, self._y)
        if self._sprite.is_animation_done():
            self._sprite.set_rate(0)