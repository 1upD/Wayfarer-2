'''
Created on Apr 23, 2015

@author: 1upde_000
'''

class priority_variable(object):
    '''
    stores an immutable object to be read by another object and updates it periodically
    '''

    _value = 0
    def __init__(self, initial_value):
        '''
        Constructor
        '''
        self._value = initial_value
    
    def update(self, new_value):
        self._value = new_value
        
    def get_value(self):
        return self._value
        