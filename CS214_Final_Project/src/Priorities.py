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
        Parameters: goals is an ordered list of lists in the form [variable, bool, integer]
        '''
        for goal in goals:
            newGoal = Priorities.Goal([goal[0]], goal[1], goal[2])
            self.goals.append(newGoal)
    
    class Goal(object):
        '''
        Subclass to represent a single goal
        A goal is a boolean expression, typically a variable inequality, which must be true
        '''
        var = []
        greaterThan = True
        limit = 0
        
        def __init__(self, var, greaterThan, limit):
            '''
            Constructor
            Parameters: var is a list containing a variable
                        greaterThan is a bool describing whether or not the variable should be greater or less than the limit
                        limit is the value the variable cannot reach
                        
            WARNING: THIS ASSUMES PASS BY REFERENCE
            '''    
            self.var = var
            self.greaterThan = greaterThan
            self.limit = limit
            
        def evaluate(self):
            if self.greaterThan: 
                return self.var[0] > self.limit
            else:
                return self.var[0] < self.limit
            
        def optimize(self, newVar):
            if self.greaterThan:
                return newVar - self.var[0]
            else:
                return self.var[0] - newVar