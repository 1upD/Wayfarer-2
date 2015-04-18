'''
Created on Apr 12, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject

class Bounce(DynamicObject):
    '''
    classdocs
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = 50
        self.myW = 50
        self.myDX = 20
        self.myDY = 20

    def collide(self, otherObject, collisionAngle):
        if collisionAngle == "Right" and self.myDX > 0:
            self.rightCollision = 1
            self.myDX = -self.myDX
            #self.myDX = 0
            #self.myX = otherObject.getX() - self.myW
            
        if collisionAngle == "Left" and self.myDX < 0:
            self.leftCollision = 1
            self.myDX = -self.myDX
            #self.myDX = 0
            #self.myX = otherObject.getX() + otherObject.getW()
        if collisionAngle == "Top" and self.myDY < 0:
            self.topCollision = 1
            self.myDY = -self.myDY
            #self.myDY = 0
            #self.myY = otherObject.getY() + otherObject.getH()
        if collisionAngle == "Bottom" and self.myDY > 0:
            self.bottomCollision = 1
            self.myDY = -self.myDY
            #self.myDY = 0
            #self.myY = otherObject.getY() - self.myH
        self.myCollisions = [self.rightCollision, self.leftCollision, self.topCollision, self.bottomCollision]
        
        
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [0, 255, 0], [self.myX, self.myY, self.myW, self.myH])        