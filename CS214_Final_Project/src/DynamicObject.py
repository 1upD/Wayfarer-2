'''
Created on Apr 4, 2015

@author: Derek Dik
'''
from src.GameObject import GameObject
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT

class DynamicObject(GameObject):
    '''
    Abstract class defining an object which has a step() function to be called every frame
    '''
    
    _last_x = 0
    _last_y = 0
    _dx = 0
    _dy = 0
    _collisions = [0, 0, 0, 0]
    destroy = False
       
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self._x = x
        self._y = y
        self._last_x = x
        self._last_y = y        
        self._h = w
        self._y = h
        
    def collide(self, otherObject, collisionAngle):
        '''
        Function to apply a collision to the object's collision vector
        '''
        if collisionAngle == "Right" and self._dx > 0:
            self._collisions[0] = 1
        if collisionAngle == "Left" and self._dx < 0:
            self._collisions[1] = 1
        if collisionAngle == "Top" and self._dy < 0:
            self._collisions[2] = 1
        if collisionAngle == "Bottom" and self._dy > 0:
            self._collisions[3] = 1
  
    def step(self):
        # If there is no collision, apply the object's x velocity
        if self._dx > 0 and self._collisions[0] == 0 or self._dx < 0 and self._collisions[1] == 0 or self._dx == 0:
            self._x += self._dx
        # If there is no collision, apply the object's y velocity
        if self._dy > 0 and self._collisions[3] == 0 or self._dy < 0 and self._collisions[2] == 0 or self._dy == 0:
            self._y += self._dy
        # Reset the collision vector
        self._collisions = [0, 0, 0, 0]
    
    def changeLocation(self, location):
        '''
        Do nothing
        '''
        
    def set_visible(self):
        '''
        Do nothing
        '''
        
    '''
    Accessors and mutators
    '''
    def getMyDX(self):
        return self._dx
    
    def getMyDY(self):
        return self._dy

    def setDY(self, speed):
            self._dy = speed
    
    def setDX(self, speed):
            self._dx = speed

    def setY(self, speed):
            self._y = speed
    
    def setX(self, speed):
            self._x = speed