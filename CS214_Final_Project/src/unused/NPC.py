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
from src.Graph import Graph


class NPC(Character):
    '''
    classdocs
    '''
    
    _type = "NPC"
    _sight_radius = 200
    myPriorities = 0
    
    def __init__(self, x, y, w, h):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        self._dx = 0
        self._dy = 0
        self.step_counter = 0
        self.water_priority = priority_variable(self._water)
        self.food_priority = priority_variable(self._food)
        self.companionship_priority = priority_variable(self._loneliness)
        goals = [[self.water_priority, True, 15, "Resource", 10],
                 [self.food_priority, True, 15, "Food", 9],
                 [self.companionship_priority, False, 6000, "NPC", 5]]
    
        self.myPriorities = Priorities(goals)    
        # self.intelligence = Intelligence(self._experience, self.myPriorities, self._w, self._h)
        self.has_graph = False
        
    def perceive(self, staticObjects, dynamicObjects):
        '''
        Receive: staticObjects, dynamicObjects, levelInfo
        Precondition: staticObjects is a list of StaticObject
                      dynamicObjects is a list of DynamicObject
                      levelInfo is a list containing the level name, x, and y PositionTest
        '''
        self._experience.perceive(staticObjects, dynamicObjects, self._x, self._y, self._water, self._food, self._loneliness)
        if self.has_graph is False:
            self.graph = Graph(staticObjects)
            self.has_graph = True
    def step(self):
        Character.step(self)
        self.water_priority.update(self._water)
        self.food_priority.update(self._water)
        self.companionship_priority.update(self._loneliness)
        self.step_counter += 1
        if self.step_counter == 9:
            if self._experience.sees_player():
#                move = self.intelligence.getMove(self._experience.get_player_location())
                move = self.graph.BFS(self._x, self._y, self._experience.get_player_location()[0], self._experience.get_player_location()[1])
                if move == 0:
                    self._dx = 2
                if move == 1:
                    self._dx = -2
                if move == 2:
                    self._dy = -2
                if move == 3:
                    self._dy = 2
            self.step_counter = 0
    def draw(self, gameDisplay, draw):
        draw.rect(gameDisplay, [0, 255, 0], [self._x, self._y, self._w, self._h])   