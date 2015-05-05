'''
Created on Apr 4, 2015

@author: Derek Dik
'''
from src.GameObject import GameObject
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT

class DynamicObject(GameObject):
    '''
    classdocs
    '''
    myLastX = 0
    myLastY = 0
    myDX = 0
    myDY = 0
    myCollisions = [0, 0, 0, 0]
    rightCollision = 0
    leftCollision = 0
    topCollision = 0
    bottomCollision = 0
    destroy = False
       
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25
    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self.myX = x
        self.myY = y
        self.myLastX = x
        self.myLastY = y        
        self.myH = w
        self.myY = h
    
    def getMyDX(self):
        return self.myDX
    
    def getMyDY(self):
        return self.myDY
    
    def collide(self, otherObject, collisionAngle):
        if collisionAngle == "Right" and self.myDX > 0:
            self.rightCollision = 1
            #self.myDX = 0
            #self.myX = otherObject.getX() - self.myW
            
        if collisionAngle == "Left" and self.myDX < 0:
            self.leftCollision = 1
            #self.myDX = 0
            #self.myX = otherObject.getX() + otherObject.getW()
        if collisionAngle == "Top" and self.myDY < 0:
            self.topCollision = 1
            #self.myDY = 0
            #self.myY = otherObject.getY() + otherObject.getH()
        if collisionAngle == "Bottom" and self.myDY > 0:
            self.bottomCollision = 1
            #self.myDY = 0
            #self.myY = otherObject.getY() - self.myH
        self.myCollisions = [self.rightCollision, self.leftCollision, self.topCollision, self.bottomCollision]

    def setDY(self, speed):
            self.myDY = speed
    
    def setDX(self, speed):
            self.myDX = speed

    def setY(self, speed):
            self.myY = speed
    
    def setX(self, speed):
            self.myX = speed
  
    def step(self):
        if self.myDX > 0 and self.myCollisions[0] == 0 or self.myDX < 0 and self.myCollisions[1] == 0 or self.myDX == 0:
            self.myLastX = self.myX
            self.myX += self.myDX
        #else:
            #self.myX = self.myLastX
        if self.myDY > 0 and self.myCollisions[3] == 0 or self.myDY < 0 and self.myCollisions[2] == 0 or self.myDY == 0:
            self.myLastY = self.myY
            self.myY += self.myDY
        #else:
            #self.myY = self.myLastY
        self.rightCollision = 0
        self.leftCollision = 0
        self.topCollision = 0
        self.bottomCollision = 0
        self.myCollisions = [self.rightCollision, self.leftCollision, self.topCollision, self.bottomCollision]
    
    def changeLocation(self, location):
        ''' Abstract definition '''
        
    def set_visible(self):
        '''Dummy definition'''