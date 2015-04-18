'''
Created on Apr 14, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject
from src.StaticObject import StaticObject
from test.test_pyexpat import PositionTest

class Character(DynamicObject):
    '''
    classdocs
    '''

    resources = 3000
    myType = "NPC"
    mySightRadius = 200
    
    def __init__(self, params):
        '''
        Constructor
        '''


    def step(self):
        self.resources -= 1
        if self.resources < 0:
            self.destroy = True
        
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
        
    def collide(self, otherObject, collisionAngle):
        if otherObject.myType == "Resource":
            otherObject.destroy = True
            self.resources += 300
        
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
        
    def perceive(self, staticObjects, dynamicObjects, levelInfo):
        '''
        Receive: staticObjects, dynamicObjects, levelInfo
        Precondition: staticObjects is a list of StaticObject
                      dynamicObjects is a list of DynamicObject
                      levelInfo is a list containing the level name, x, and y PositionTest
        '''