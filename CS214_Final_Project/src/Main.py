'''
Created on Apr 23, 2015

@author: 1upde_000
'''
import src
from src import *
from src.Level import Level
from src.Bounce import Bounce

import pygame
from pygame.locals import *

from test.test_buffer import numpy_array
from src.GameObject import GameObject

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
OFFSET = 0

if __name__ == '__main__':
    # Initialize pygame
    pygame.init()
    # Create a new window, set to 
    gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Set the caption to be the title of the game
    pygame.display.set_caption("Dog Eat Dog")
    # Update the display
    pygame.display.flip()
    
    # Initialize an empty list to hold the levels
    levels = []
    
    # Open the map file to get all of the individual level files in the proper order
    map_file = open("map.dat", "r")
    
    # Initialize a counter
    i = 0
    # For each line of the map file
    for line in map_file:
        # Split the line into individual filenames
        files = line.split()
        # Create a list to hold the row of levels
        levelRow = [0] * len(files)
        # For each file in the line
        for j in range(0, len(files)):
            # Add a new level to the row
            levelRow[j] = Level(files[j], i, j)
        # Add the row of levels to the level list    
        levels.append(levelRow)
        # Tick
        i = i + 1 
    # Close the map file
    map_file.close()
    
    # Initialize coordinates for the current level
    currentLevelX = 0
    currentLevelY = 0
    # Initialize a variable to represent the level currently being drawn
    currentLevel = levels[0][0]
    
    # Initialize the player
    player = Player.Player(100, 100)
    currentLevel.resetPlayer(player)
    bounce = Bounce(200, 200)
    currentLevel.addDynamicObject(bounce)
    
    # Start the clock
    clock = pygame.time.Clock()
    
    '''
    Main loop
    '''
    gameExit = False
    while not gameExit:
        # Draw loop
        gameDisplay.fill((255, 255, 255))
        
        # Draw level
        currentLevel.draw(gameDisplay, pygame.draw)
            
        # Update the screen
        pygame.display.update()
            
        clock.tick(30)
        
        # Event loop
        for event in pygame.event.get():      
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == 119:
                    currentLevel.keyboardUp()
                if event.key == 97:
                    currentLevel.keyboardLeft()
                if event.key == 100:
                    currentLevel.keyboardRight()
                if event.key == 115:
                    currentLevel.keyboardDown()
    
            if event.type == pygame.KEYUP:
                # Up key
                if event.key == 119:
                    currentLevel.keyboardReleaseUp()            
                # Left key
                if event.key == 97:
                    currentLevel.keyboardReleaseLeft()            
                # Right key
                if event.key == 100:
                    currentLevel.keyboardReleaseRight()
                # Down key
                if event.key == 115:
                    currentLevel.keyboardReleaseDown()
                
                # P key
                if event.key == 112:
                    #Do nothing
                    p = 1
    
    
        # Step
        #currentLevel.step()
        
        for row in levels:
            for level in row:
                level.step()
                transitioningObjects = level.checkForTransition()
                for transitioningObject in transitioningObjects:
                    transition = transitioningObject[1]
                    if transitioningObject[1] != "None":
                        levelX = 0
                        levelY = 0
                        
                        for row in range(len(levels)):
                            for column in range(len(levels[row])):
                                if levels[row][column] == level:
                                    levelY = row
                                    levelX = column
                        
                        
                        if transition == "Up":
                            if transitioningObject[0].type() == "Player":
                                #player = currentLevel.extractPlayer()
                                currentLevelY -= 1
                                currentLevel = levels[currentLevelY][currentLevelX]
                                currentLevel.resetPlayer(player)
                            else:
                                levels[levelY - 1][levelX].addDynamicObject(transitioningObject[0])
                        elif transition == "Down":
                            if transitioningObject[0].type() == "Player":
                                #player = currentLevel.extractPlayer()
                                currentLevelY += 1
                                currentLevel = levels[currentLevelY][currentLevelX]
                                currentLevel.resetPlayer(player)
                            else:
                                levels[levelY + 1][levelX].addDynamicObject(transitioningObject[0])
                                
                        elif transition == "Left":
                            if transitioningObject[0].type() == "Player":
                                #player = currentLevel.extractPlayer()
                                currentLevelX -= 1
                                currentLevel = levels[currentLevelY][currentLevelX]
                                currentLevel.resetPlayer(player)
                            else:
                                levels[levelY][levelX - 1].addDynamicObject(transitioningObject[0])
                    
                        elif transition == "Right":
                            if transitioningObject[0].type() == "Player":
                                #player = currentLevel.extractPlayer()
                                currentLevelX += 1
                                currentLevel = levels[currentLevelY][currentLevelX]
                                currentLevel.resetPlayer(player)
                            else:
                                levels[levelY][levelX + 1].addDynamicObject(transitioningObject[0])
            
    
    '''
        transition = currentLevel.checkForTransition()
        if transition == "Up":
            player = currentLevel.extractPlayer()
            currentLevelY -= 1
            currentLevel = levels[currentLevelY][currentLevelX]
            currentLevel.resetPlayer(player)
        elif transition == "Down":
            player = currentLevel.extractPlayer()
            currentLevelY += 1
            currentLevel = levels[currentLevelY][currentLevelX]
            currentLevel.resetPlayer(player)
        elif transition == "Left":
            player = currentLevel.extractPlayer()
            currentLevelX -= 1
            currentLevel = levels[currentLevelY][currentLevelX]
            currentLevel.resetPlayer(player)
        elif transition == "Right":
            player = currentLevel.extractPlayer()
            currentLevelX += 1
            currentLevel = levels[currentLevelY][currentLevelX]
            currentLevel.resetPlayer(player)
    '''
        
    pygame.quit()
    quit
