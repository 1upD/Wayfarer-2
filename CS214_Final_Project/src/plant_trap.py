'''
Created on May 2, 2015

@author: Derek Dik
'''
from src.DynamicObject import DynamicObject
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT
from src.sprite import sprite

class plant_trap(DynamicObject):
    '''
    plant_trap models an enemy underground that springs up on contact with the player
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
        self.sprite = sprite("images\plant\plant.dat")
        self.sprite.set_rate(0)       
    def step(self):
        DynamicObject.step(self)
        if self._opacity > 0:
            self._opacity -= 1
            
    def set_visible(self):
        self.sprite.set_rate(1)
    def draw(self, gameDisplay, draw):
        self.sprite.draw(gameDisplay, self._x, self._y)
        if self.sprite.is_animation_done():
            self.sprite.set_rate(0)