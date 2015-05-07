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
        self.water_priority = priority_variable(self._water)
        self.food_priority = priority_variable(self._food)
        self.companionship_priority = priority_variable(self._loneliness)
        goals = [[self.water_priority, True, 15, "Resource", 10],
                 [self.food_priority, True, 15, "Food", 9],
                 [self.companionship_priority, False, 6000, "NPC", 5]]
        self.myPriorities = Priorities(goals)    
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        self._dx = 5
        self._dy = 5


    def collide(self, otherObject, collisionAngle):
        if collisionAngle == "Right" and self._dx > 0:
            self._right_collision = 1
            self._dx = -self._dx
            #self.myDX = 0
            #self.myX = otherObject.getX() - self.myW
            
        if collisionAngle == "Left" and self._dx < 0:
            self._left_collision = 1
            self._dx = -self._dx
            #self.myDX = 0
            #self.myX = otherObject.getX() + otherObject.getW()
        if collisionAngle == "Top" and self._dy < 0:
            self._top_collision = 1
            self._dy = -self._dy
            #self.myDY = 0
            #self.myY = otherObject.getY() + otherObject.getH()
        if collisionAngle == "Bottom" and self._dy > 0:
            self._bottom_collision = 1
            self._dy = -self._dy
            #self.myDY = 0
            #self.myY = otherObject.getY() - self.myH
        self._collisions = [self._right_collision, self._left_collision, self._top_collision, self._bottom_collision]
        
        
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [0, 255, 0], [self._x, self._y, self._w, self._h])        