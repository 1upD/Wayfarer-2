'''
Created on Apr 5, 2015

@author: 1upde_000
'''
from src.DynamicObject import DynamicObject
from src.Character import Character
from src.Globals import WINDOW_HEIGHT
from src.Globals import WINDOW_WIDTH
from src.sprite import sprite

class Player(Character):
    '''
    classdocs
    '''

    _type = "Player"
    _direction = 0
    _victory = False
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._h = WINDOW_HEIGHT / 25
        self._w = WINDOW_WIDTH / 25
        self._sprite = sprite("images/player/walking.dat")

    def _init_(self, x, y, w, h):
        '''
        Second Constructor
        '''
        self._x = x
        self._y = y
        self._h = w
        self._y = h
    

    def draw(self, gameDisplay, draw):
        Character.draw(self, gameDisplay, draw)
        # Draw the H20 bar
        draw.rect(gameDisplay, [0, 0, 255, 100], [25, 25, self._water / 5, 5])
        # Display the food bar
        draw.rect(gameDisplay, [255, 255, 0, 100], [25, 30, self._food / 10, 5])
    def changeLocation(self, location):
        ''' Empty definition '''
        
    def perceive(self, staticObjects, dynamicObjects, x, y):
        ''' Empty definition '''
    
    def collide(self, otherObject, collisionAngle):
        Character.collide(self, otherObject, collisionAngle)
        if otherObject.type() is "Victory":
            _victory = True
    def has_won(self):
        return self._victory