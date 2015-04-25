'''
Created on Apr 24, 2015

@author: 1upde_000
'''
from pygame.midi import _init

class Intelligence(object):
    '''
    classdocs
    '''


    def __init__(self, experience, priorities):
        '''
        Constructor
        '''
        self.experience = experience
        self.priorities = priorities
    
    def getMove(self):
        position = Intelligence._position(self.experience.get_position()[0], self.experience.get_position()[1], self.experience.get_water(), self.experience.get_food())
        return self._search(position, 1000)[0]
        
    def _search(self, position, depth):
        result = [0, 0]
        # If depth is equal to zero, evaluate this position
        if depth == 0:
            return [0, self.evaluate(position)]
        # Initialize a variable for the best possible position
        best_value = -9999999999999
        best_move = 0

        # For each possible move
        for move in range(0, 3):
            # If the move can be made
            if self.legal_move(position, move):
                # Duplicate the position
                new_position = position.duplicate()
                # Test the move
                position.move(move)
                # The value of this move is the result of searching from this position with depth d - 1
                new_value = self._search(new_position, depth - 1)[1]
                # If this value is greater than the best value
                if new_value > best_value:
                    # Set best value to this value
                    best_move = new_value
                    # Set the best move to be this move
                    best_value = new_value
        # Return this move
        return [best_move, best_value]
    def legal_move(self, position, move):
        return True
    
    def evaluate(self, position):
        # Hard code needs for now, for testing purposes
        return position.water + position.food - position.loneliness
        
        
    class _position(object):
        x = 0
        y = 0
        water = 0
        food = 0
        loneliness = 0
        def __init__(self, x, y, food, water):
            self.x = x
            self.y = y
        
        def duplicate(self):
            new_position = Intelligence._position(self.x, self.y, self.food, self.water)
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