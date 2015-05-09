'''
Created on May 8, 2015

@author: Derek Dik
'''

game_time = 0

def count_step():
    global game_time
    game_time += 1
    
def get_time():
    return game_time