'''
Created on Mar 15, 2015

@author: 1upde_000
'''

from test.test_buffer import numpy_array

from src.DynamicObject import DynamicObject
from src.GameObject import GameObject
from src.Globals import WINDOW_HEIGHT
from src.Player import Player
from src.Resource import water_resource
from src.StaticObject import StaticObject
from src.push_block import push_block
from src.prey_animal import prey_animal
from src.simple_predator import simple_predator
from src.plant_trap import plant_trap


class Level(object):
    '''
    classdocs
    '''
    
    myStaticObjects = []
    myDynamicObjects = []
    width = 0
    height = 0
    TILE_SIZE = WINDOW_HEIGHT / 25
    myDescription = ""

    
    def __init__(self, fileName, x, y):
        '''
        Constructor
        '''
        height = 0
        width = 0
        self._x = x
        self._y = y
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
                if val == "1" or val == "x":
                    newTile = StaticObject(self.TILE_SIZE * column, self.TILE_SIZE * row)
                    self.myStaticObjects.append(newTile)
                elif val == "2":
                    newResource  = water_resource(self.TILE_SIZE * column, self.TILE_SIZE * row) 
                #   self.myDynamicObjects.append(newResource)
                    self.myStaticObjects.append(newResource)
                elif val == "4":
                    new_push_block  = push_block(self.TILE_SIZE * column, self.TILE_SIZE * row) 
                    self.myDynamicObjects.append(new_push_block)
                elif val is "5":
                    new_prey_animal = prey_animal(self.TILE_SIZE * column, self.TILE_SIZE * row)
                    self.myDynamicObjects.append(new_prey_animal)
                elif val is "6":
                    new_predator = simple_predator(self.TILE_SIZE * column, self.TILE_SIZE * row)
                    self.myDynamicObjects.append(new_predator)
                elif val is "7":
                    new_plant = plant_trap(self.TILE_SIZE * column, self.TILE_SIZE * row)
                    # self.myDynamicObjects.append(new_plant)
                    self.myStaticObjects.append(new_plant)
                    
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
            if dynamicObject._type == "NPC":
                dynamicObject.perceive(self.myStaticObjects, self.myDynamicObjects)
            if dynamicObject.destroy:
                self.myDynamicObjects.remove(dynamicObject)

            
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
        dynamicObject.changeLocation([self._x, self._y])
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
        self.player.setDY(-4)
        
    def keyboardReleaseUp(self):
        self.player.setDY(0)

    def keyboardDown(self):
        self.player.setDY(4)
        
    def keyboardReleaseDown(self):
        self.player.setDY(0)

    def keyboardLeft(self):
        self.player.setDX(-4)
        
    def keyboardReleaseLeft(self):
        self.player.setDX(0)
        
    def keyboardRight(self):
        self.player.setDX(4)
        
    def keyboardReleaseRight(self):
        self.player.setDX(0)            