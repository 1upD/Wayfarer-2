'''
Created on Apr 14, 2015

@author: Derek Dik
'''
from src.DynamicObject import DynamicObject
from src.StaticObject import StaticObject
from test.test_pyexpat import PositionTest
from src.Experience import Experience


class Character(DynamicObject):
    '''
    Superclass to define a dynamic object that represents a character
    '''

    # Instance variables
    _water = 3000
    _food = 6000
    _loneliness = 0
    _experience = Experience()    
    _damage_cooldown = 0
    _type = "NPC"
    _sight_radius = 200


    def step(self):
        DynamicObject.step(self)
        self._damage_cooldown += 1
        self._water -= 1
        self._food -= 1
        self._loneliness += 1
        if self._water < 0:
            self.destroy = True
        
        
    def collide(self, otherObject, collisionAngle):
        if otherObject is not self:
            if otherObject._type == "water_resource":
                self._water += otherObject.get_water()
            elif otherObject._type == "predator" and self._damage_cooldown > 30:
                self._water -= 300
                self._damage_cooldown = 0
                otherObject.set_visible()
                    
            if collisionAngle == "Right" and self._dx > 0:
                self._collisions[0] = 1
                if otherObject.type() is "pushable":
                    otherObject._dx = 2
            if collisionAngle == "Left" and self._dx < 0:
                self._collisions[1] = 1
                if otherObject.type() is "pushable":
                    otherObject._dx = -2
            if collisionAngle == "Top" and self._dy < 0:
                self._collisions[2] = 1
                if otherObject.type() is "pushable":
                    otherObject._dy = -2
            if collisionAngle == "Bottom" and self._dy > 0:
                self._collisions[3] = 1
                if otherObject.type() is "pushable":
                    otherObject._dy = 2
        
    def perceive(self, staticObjects, dynamicObjects, x, y):
        '''
        Stub
        '''

    def changeLocation(self, location):
        self._experience.changeLocation(location)        
        
    
    