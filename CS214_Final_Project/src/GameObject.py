'''
Created on Apr 4, 2015

@author: 1upde_000
'''

class GameObject(object):
    '''
    classdocs
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

        '''
        if otherObject != self: 
            #Bottom side collision
            if self._x - otherObject.getX() < self._w and otherObject.getY() - self._y < self._h and self._x - otherObject.getX() > -self._w and otherObject.getY() - self._y > 0:
                self.collide(otherObject, "Bottom")
            #Top side collision
            if self._x - otherObject.getX() < self._w:
                if -(otherObject.getY() - self._y) < otherObject.getH():
                    if self._x - otherObject.getX() > -self._w:
                        if otherObject.getY() - self._y < 0:
                            self.collide(otherObject, "Top")
            #Left side collision
            if self._x - otherObject.getX() < otherObject.getW() and abs(self._y - otherObject.getY()) < otherObject.getH() and self._x - otherObject.getX() > 0:
                self.collide(otherObject, "Left")
            #Left side collision
            if self._x - otherObject.getX() < 0 and -(self._x - otherObject.getX()) < self._w and abs(self._y - otherObject.getY()) < otherObject.getH():
                self.collide(otherObject, "Right")
        
    '''              
    def collide(self, otherObject, collisionAngle):
        '''
        Abstract definition
        '''
    
    def step(self):
        '''
        Abstract definition
        '''
        
    def draw(self, gameDisplay, draw):
        '''
        Abstract definition
        '''