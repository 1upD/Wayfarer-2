'''
Created on May 8, 2015

GameTimer.py is a module to count the frames passed by the main loop. 
It is used by objects which need to keep track of elapsed time when the
player transitions to a different room.

@author: Derek Dik
'''

game_time = 0

def count_step():
    global game_time
    game_time += 1
    
def get_time():
    return game_time