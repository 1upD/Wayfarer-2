'''
Created on Apr 14, 2015

@author: Derek Dik
'''

from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH, water_resource_value
from src.StaticObject import StaticObject

class water_resource(StaticObject):
    '''
    Models a dispenser from which a user can refill water
    '''

    myType = "water_resource"
    resource_value = water_resource_value
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25
        self.cooldown = 600
    def get_water(self):
        if self.cooldown == 600:
            self.cooldown = 0
            return self.resource_value
        else: 
            return 0
    def draw(self, gameDisplay, draw):
        if self.cooldown < 600:
            draw.rect(gameDisplay, [100, 100, 200], [self.myX, self.myY, self.myW, self.myH])
            # I am going to cheat and put this logic in the draw loop. It will save a ton of step() calls
            self.cooldown += 1
        else:
            draw.rect(gameDisplay, [0, 0, 255], [self.myX, self.myY, self.myW, self.myH])
            