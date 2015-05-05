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

    animation_count = 91
    myType = "predator"
    def __init__(self, x, y):
        '''
        Constructor
        '''
        super()
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25 
        self.sprite = sprite("images\plant\plant.dat")
        
    def step(self):
        DynamicObject.step(self)
        if self._opacity > 0:
            self._opacity -= 1
            
    def set_visible(self):
        self.animation_count = 0
    def draw(self, gameDisplay, draw):
        if self.animation_count < 91:
            self.sprite.draw(gameDisplay, draw, self.myX, self.myY)
            self.animation_count += 1
            # draw.rect(gameDisplay, [255, 0, 0, self._opacity], [self.myX, self.myY, self.myW, self.myH]) 