'''
Created on Apr 12, 2015

@author: 1upde_000
'''
from src.Character import Character
from src.DynamicObject import DynamicObject
from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH
from src.NPC import NPC
from src.Priorities import Priorities
from src.priority_variable import priority_variable


class Bounce(NPC):
    '''
    classdocs
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.water_priority = priority_variable(self.water)
        self.food_priority = priority_variable(self.food)
        self.companionship_priority = priority_variable(self.loneliness)
        goals = [[self.water_priority, True, 15, "Resource", 10],
                 [self.food_priority, True, 15, "Food", 9],
                 [self.companionship_priority, False, 6000, "NPC", 5]]
        self.myPriorities = Priorities(goals)    
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25
        self.myDX = 5
        self.myDY = 5


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