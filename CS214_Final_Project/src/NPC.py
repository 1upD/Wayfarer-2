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


class NPC(Character):
    '''
    classdocs
    '''
    
    myType = "NPC"
    mySightRadius = 200
    myExperience = Experience()
    myPriorities = 0
    
    def __init__(self, x, y, w, h):
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
        
    def perceive(self, staticObjects, dynamicObjects):
        '''
        Receive: staticObjects, dynamicObjects, levelInfo
        Precondition: staticObjects is a list of StaticObject
                      dynamicObjects is a list of DynamicObject
                      levelInfo is a list containing the level name, x, and y PositionTest
        '''
        self.myExperience.perceive(staticObjects, dynamicObjects)

    def changeLocation(self, location):
        self.myExperience.changeLocation(location)        
        
    
    def step(self):
        Character.step(self)
        self.water_priority.update(self.water)
        self.food_priority.update(self.water)
        self.companionship_priority.update(self.loneliness)