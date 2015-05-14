'''
Created on Apr 4, 2015

@author: Derek Dik
'''

import abc

class GameObject(object):
    __metaclass__ = abc.ABCMeta
    '''
    Abstract base class inherited by all entities within the game environment. 
    Stores data regarding bounding size, position, and type and provides the 
    collision algorithm for any game object.
    '''
    _x = 0
    _y = 0
    _h = 0
    _w = 0
    _type = "GameObject"
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = 16
        self._y = 16
    
    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self._x = x
        self._y = y
        self._h = w
        self._y = h
        
    
    def getX(self):
        return self._x
        
    def getY(self):
        return self._y
    
    def getW(self):
        return self._w
        
    def getH(self):
        return self._h
    
    def type(self):
        return self._type
    
    def testCollision(self, otherObject):
        if otherObject is not self: 
            x = self._x + self._dx
            y = self._y + self._dy
            #Bottom side collision
            if x - otherObject.getX() < self._w and otherObject.getY() - y < self._h and x - otherObject.getX() > -self._w and otherObject.getY() - y > 0:
                self.collide(otherObject, "Bottom")
            #Top side collision
            if x - otherObject.getX() < self._w:
                if -(otherObject.getY() - y) < otherObject.getH():
                    if x - otherObject.getX() > -self._w:
                        if otherObject.getY() - y < 0:
                            self.collide(otherObject, "Top")
            #Left side collision
            if x - otherObject.getX() < otherObject.getW() and abs(y - otherObject.getY()) < otherObject.getH() and x - otherObject.getX() > 0:
                self.collide(otherObject, "Left")
            #Left side collision
            if x - otherObject.getX() < 0 and -(x - otherObject.getX()) < self._w and abs(y - otherObject.getY()) < otherObject.getH():
                self.collide(otherObject, "Right")

    @abc.abstractmethod         
    def collide(self, otherObject, collisionAngle):
        '''
        Method to call after a collision occurs between this object and another GameObject
        '''
        return
    @abc.abstractmethod
    def step(self):
        '''
        Function to be called by the containing Level every frame
        '''
        return
    
    @abc.abstractmethod
    def draw(self, gameDisplay, draw):
        '''
        Draw function
        '''
        return