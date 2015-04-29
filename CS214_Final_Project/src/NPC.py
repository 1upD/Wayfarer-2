'''
Created on Apr 14, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject
from src.StaticObject import StaticObject
from test.test_pyexpat import PositionTest
from src.Experience import Experience
from src.Character import Character
from src.Priorities import Priorities
from src.priority_variable import priority_variable
from src.Intelligence import Intelligence
from src.Globals import WINDOW_HEIGHT, WINDOW_WIDTH


class NPC(Character):
    '''
    classdocs
    '''
    
    myType = "NPC"
    mySightRadius = 200
    myPriorities = 0
    
    def __init__(self, x, y, w, h):
        '''
        Constructor
        '''
        self.myX = x
        self.myY = y
        self.myH = WINDOW_HEIGHT / 25
        self.myW = WINDOW_WIDTH / 25
        self.myDX = 0
        self.myDY = 0
        self.step_counter = 0
        self.water_priority = priority_variable(self.water)
        self.food_priority = priority_variable(self.food)
        self.companionship_priority = priority_variable(self.loneliness)
        goals = [[self.water_priority, True, 15, "Resource", 10],
                 [self.food_priority, True, 15, "Food", 9],
                 [self.companionship_priority, False, 6000, "NPC", 5]]
    
        self.myPriorities = Priorities(goals)    
        self.intelligence = Intelligence(self.myExperience, self.myPriorities, self.myW, self.myH)
    def perceive(self, staticObjects, dynamicObjects):
        '''
        Receive: staticObjects, dynamicObjects, levelInfo
        Precondition: staticObjects is a list of StaticObject
                      dynamicObjects is a list of DynamicObject
                      levelInfo is a list containing the level name, x, and y PositionTest
        '''
        self.myExperience.perceive(staticObjects, dynamicObjects, self.myX, self.myY, self.water, self.food, self.loneliness)
        
    
    def step(self):
        Character.step(self)
        self.water_priority.update(self.water)
        self.food_priority.update(self.water)
        self.companionship_priority.update(self.loneliness)
        self.step_counter += 1
        if self.step_counter == 9:
            move = self.intelligence.getMove()
            if move == 0:
                self.myDX = 2
            if move == 1:
                self.myDX = -2
            if move == 2:
                self.myDY = -2
            if move == 3:
                self.myDY = 2
            self.step_counter = 0
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [0, 255, 0], [self.myX, self.myY, self.myW, self.myH])   