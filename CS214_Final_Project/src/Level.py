'''
Created on Mar 15, 2015

@author: 1upde_000
'''

from test.test_buffer import numpy_array
from src.GameObject import GameObject
from src.StaticObject import StaticObject
from src.Player import Player
from src.DynamicObject import DynamicObject
from src.Resource import Resource

class Level(object):
    '''
    classdocs
    '''
    
    myStaticObjects = []
    myDynamicObjects = []
    width = 0
    height = 0
    TILE_SIZE = 50
    
    def __init__(self, fileName):
        '''
        Constructor
        '''
        height = 0
        width = 0
        self.myStaticObjects = []
        self.myDynamicObjects = []
        file = open(fileName, "r")
        tiles = []
        for line in file:
            height += 1
            width = 0
            words = line.split()
            tileRow = []
            for tile in words:
                width += 1
                tileRow.append(tile)
            tiles.append(tileRow)
        
        file.close()
        
        for row in range(0, height):
            for column in range(0, width):
                val = tiles[row][column]
                if val == "1":
                    newTile = StaticObject(self.TILE_SIZE * column, self.TILE_SIZE * row)
                    self.myStaticObjects.append(newTile)
                if val == "2":
                    newResource  = Resource(self.TILE_SIZE * column, self.TILE_SIZE * row) 
                    self.myDynamicObjects.append(newResource)
        self.height = height * self.TILE_SIZE
        self.width = width * self.TILE_SIZE

    def __oldinit__(self, tiles, width, height):
        '''
        Constructor
        '''
        self.myDynamicObjects.append(self.player)
        
        for row in range(0, height):
            for column in range(0, width):
                val = tiles[row][column]
                if val == 1:
                    newTile = StaticObject(50 * column, 50 * row)
                    self.myStaticObjects.append(newTile)
                
        
    def draw(self, gameDisplay, draw):
        for staticObject in self.myStaticObjects:
            staticObject.draw(gameDisplay, draw)
        for dynamicObject in self.myDynamicObjects:
            dynamicObject.draw(gameDisplay, draw)
            
    def step(self):   
            
        #Test collisions
        for dynamicObject in self.myDynamicObjects:
            for staticObject in self.myStaticObjects:
                dynamicObject.testCollision(staticObject)
            for otherObject in self.myDynamicObjects:
                dynamicObject.testCollision(otherObject)      

        #Step
        for dynamicObject in self.myDynamicObjects:
            dynamicObject.step()
            if dynamicObject.destroy:
                self.myDynamicObjects.remove(dynamicObject)
       # if dynamicObject.myType == "NPC":
       #     dynamicObject.perceive(self.myStaticObjects, self.myDynamicObjects)
            
    def checkForTransition(self):
        transitioningObjects = []
        for dynamicObject in self.myDynamicObjects:
            transitioningObject = [dynamicObject]
            if dynamicObject.getX() > self.width:
                transitioningObject.append("Right")
                transitioningObjects.append(transitioningObject)
                self.myDynamicObjects.remove(dynamicObject)                
            elif dynamicObject.getX() < 0:
                transitioningObject.append("Left")
                transitioningObjects.append(transitioningObject)
                self.myDynamicObjects.remove(dynamicObject)
            elif dynamicObject.getY() < 0:
                transitioningObject.append("Up")
                self.myDynamicObjects.remove(dynamicObject)
                transitioningObjects.append(transitioningObject)
            elif dynamicObject.getY() > self.height:
                transitioningObject.append("Down")
                transitioningObjects.append(transitioningObject)
                self.myDynamicObjects.remove(dynamicObject)
            else:
                transitioningObject.append(0)
                transitioningObject.append("None")
        return transitioningObjects
    def checkForPlayerTransition(self):
        if self.player.getX() > self.width:
            return "Right"
        elif self.player.getX() < 0:
            return "Left"
        elif self.player.getY() < 0:
            return "Up"
        elif self.player.getY() > self.height:
            return "Down"
        else:
            return "None"
        
    '''
    def extractPlayer(self):
        #Finish this next!
        self.myDynamicObjects.remove(self.player)
        return self.player
    '''
    def addDynamicObject(self, dynamicObject):
        self.myDynamicObjects.append(dynamicObject)
        if dynamicObject.getX() > self.width:
            dynamicObject.setX(0)
        elif dynamicObject.getX() < 0:
            dynamicObject.setX(self.width - self.TILE_SIZE)
        elif dynamicObject.getY() < 0:
            dynamicObject.setY(self.height - self.TILE_SIZE)
        elif dynamicObject.getY() > self.height:
            dynamicObject.setY(0)
        
               
    def resetPlayer(self, player):
        self.player = player
        self.addDynamicObject(player)
        
        
    def keyboardUp(self):
        self.player.setDY(-10)
        
    def keyboardReleaseUp(self):
        self.player.setDY(0)

    def keyboardDown(self):
        self.player.setDY(10)
        
    def keyboardReleaseDown(self):
        self.player.setDY(0)

    def keyboardLeft(self):
        self.player.setDX(-10)
        
    def keyboardReleaseLeft(self):
        self.player.setDX(0)
        
    def keyboardRight(self):
        self.player.setDX(10)
        
    def keyboardReleaseRight(self):
        self.player.setDX(0)            