'''
Created on Apr 4, 2015

@author: 1upde_000
'''

class GameObject(object):
    '''
    classdocs
    '''
    myX = 0
    myY = 0
    myH = 0
    myW = 0
    myType = "GameObject"
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = 16
        self.myY = 16
    
    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = w
        self.myY = h
        
    
    def getX(self):
        return self.myX
        
    def getY(self):
        return self.myY
    
    def getW(self):
        return self.myW
        
    def getH(self):
        return self.myH
    
    def type(self):
        return self.myType
    
    def testCollision(self, otherObject):
        if otherObject is not self: 
            x = self.myX + self.myDX
            y = self.myY + self.myDY
            #Bottom side collision
            if x - otherObject.getX() < self.myW and otherObject.getY() - y < self.myH and x - otherObject.getX() > -self.myW and otherObject.getY() - y > 0:
                self.collide(otherObject, "Bottom")
            #Top side collision
            if x - otherObject.getX() < self.myW:
                if -(otherObject.getY() - y) < otherObject.getH():
                    if x - otherObject.getX() > -self.myW:
                        if otherObject.getY() - y < 0:
                            self.collide(otherObject, "Top")
            #Left side collision
            if x - otherObject.getX() < otherObject.getW() and abs(y - otherObject.getY()) < otherObject.getH() and x - otherObject.getX() > 0:
                self.collide(otherObject, "Left")
            #Left side collision
            if x - otherObject.getX() < 0 and -(x - otherObject.getX()) < self.myW and abs(y - otherObject.getY()) < otherObject.getH():
                self.collide(otherObject, "Right")

        '''
        if otherObject != self: 
            #Bottom side collision
            if self.myX - otherObject.getX() < self.myW and otherObject.getY() - self.myY < self.myH and self.myX - otherObject.getX() > -self.myW and otherObject.getY() - self.myY > 0:
                self.collide(otherObject, "Bottom")
            #Top side collision
            if self.myX - otherObject.getX() < self.myW:
                if -(otherObject.getY() - self.myY) < otherObject.getH():
                    if self.myX - otherObject.getX() > -self.myW:
                        if otherObject.getY() - self.myY < 0:
                            self.collide(otherObject, "Top")
            #Left side collision
            if self.myX - otherObject.getX() < otherObject.getW() and abs(self.myY - otherObject.getY()) < otherObject.getH() and self.myX - otherObject.getX() > 0:
                self.collide(otherObject, "Left")
            #Left side collision
            if self.myX - otherObject.getX() < 0 and -(self.myX - otherObject.getX()) < self.myW and abs(self.myY - otherObject.getY()) < otherObject.getH():
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