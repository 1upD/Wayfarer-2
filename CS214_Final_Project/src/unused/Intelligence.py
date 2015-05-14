'''
Created on Apr 24, 2015

@author: Derek Dik
'''
from pygame.midi import _init

class Intelligence(object):
    '''
    Class to model an AI. Receives input from a Priorities and Experience and uses it to make decisions.
    '''


    def __init__(self, experience, priorities, w, h):
        '''
        Constructor
        '''
        self.experience = experience
        self.priorities = priorities
        self.w = w
        self.h = h

    def getMove(self, goal):
        position = Intelligence._position(self.experience.get_position()[0], self.experience.get_position()[1], self.w, self.h, self.experience.get_water(), self.experience.get_food(), self.experience.NearbyEntities, self.experience.get_loneliness())
        return self._search(position, 1, goal)[0]
    def getKey(self, item):
        return item[0]
    def _search(self, position, depth, goal):
        # If depth is equal to zero, evaluate this position
        if depth == 0:
            return [0, self.evaluate(position, goal), 0]
        # Initialize a variable for the best possible position
        best_value = 9999999999999
        best_move = 0
        best_depth = 0
        
        # For each possible move
        for move in range(0, 3):
            # If the move can be made
            if self.legal_move(position, move):
                # Duplicate the position
                new_position = position.duplicate()
                # Test the move
                new_position.move(move)
                # Set the best-first heuristic
                current_value = self.evaluate(new_position, goal)
                # The value of this move is the result of searching from this position with depth d - 1
                move_search = self._search(new_position, depth - 1, goal)
                new_value = move_search[1]
                # If this value is greater than the best value
                if new_value < best_value or new_value == best_value and current_value < best_value:
                    # Set best value to this value
                    best_move = move
                    # Set the best move to be this move
                    best_value = new_value
                        
        # Return this move
        return [best_move, best_value]
    def legal_move(self, position, move):
        # return False
        new_position = position.duplicate()
        new_position.move(move)
        legal = True
        for entity in self.experience.myObstacles:
            if new_position.collide(entity):
                legal = False
        return legal
    def evaluate(self, position, goal):
        return abs(position.x - goal [0]) + abs(position.y - 1)

    '''  
    def evaluate(self, position, goal):
        # Hard code needs for now, for testing purposes
        score = position._water
        
        for entity in position.dynamicObjects:
            if entity.type() == "Resource":
                score -= 100
        # return position.points
        return score
    '''
   
    class _position(object):
        x = 0
        y = 0
        _water = 0
        _food = 0
        _loneliness = 0
        points = 0
        def __init__(self, x, y, w, h, food, water, dynamicObjects, loneliness):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self._water = water
            self._food = food
            self._loneliness = loneliness
            self.dynamicObjects = list(dynamicObjects)
        def duplicate(self):
            new_position = Intelligence._position(self.x, self.y, self.w, self.h, self._food, self._water, self.dynamicObjects, self._loneliness)
            new_position.points = self.points
            return new_position
        
        def move(self, move):
            if move == 0:
                self.x += 18
            elif move == 1:
                self.x -= 18
            elif move == 2:
                self.y -= 18
            elif move == 3:
                self.y += 18
            self._water -= 18
            self._food -= 18
            self._loneliness += 18
            for entity in self.dynamicObjects:
                if self.collide(entity):
                    if entity.type() is "Resource":
                        self.dynamicObjects.remove(entity)
                        self._water += 300
                        self.points += 300
        def collide(self, entity):
            return abs(self.x - entity.getX()) < self.w and abs(self.y - entity.getY()) < self.h               