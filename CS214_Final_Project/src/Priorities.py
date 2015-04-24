'''
Created on Apr 22, 2015

@author: Derek Dik
'''

class Priorities(object):
    '''
    Stores goals an NPC will try to accomplish in order
    '''
    
    goals = []

    def __init__(self, goals):
        '''
        Constructor
        Parameters: goals is an ordered list of lists in the form [variable, greaterThan, limit, entityType, priority]
        '''
        for goal in goals:
            newGoal = Priorities.Goal(goal[0], goal[1], goal[2], goal[3], goal[4])
            self.goals.append(newGoal)
    
    class Goal(object):
        '''
        Subclass to represent a single goal
        A goal is a boolean expression, typically a variable inequality, which must be true
        '''
        var = []
        greaterThan = True
        limit = 0
        entity_type = ""
        
        def __init__(self, var, greaterThan, limit, entityType, priority):
            '''
            Constructor
            Parameters: var is a priority_variable
                        greaterThan is a bool describing whether or not the variable should be greater or less than the limit
                        limit is the value the variable cannot reach
                        
            WARNING: THIS ASSUMES PASS BY REFERENCE
            '''    
            self.var = var
            self.greaterThan = greaterThan
            self.limit = limit
            self.entity_type = entityType
            
        def evaluate(self):
            if self.greaterThan: 
                return self.var.get_value() > self.limit
            else:
                return self.var.get_value() < self.limit
            
        def optimize(self, newVar):
            if self.greaterThan:
                return newVar - self.var.get_value()
            else:
                return self.var.get_value() - newVar