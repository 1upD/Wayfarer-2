'''
Created on May 14, 2015

@author: Derek Dik
'''

import pygame

import sys

from src.Level import Level
from src.Player import Player
from src.Globals import WINDOW_WIDTH, WINDOW_HEIGHT
from src.GameTimer import count_step
from src.PauseMenu import PauseMenu
from src.StartMenu import StartMenu
from src.GameOverMenu import GameOverMenu
from pygame.constants import FULLSCREEN, HWSURFACE, RESIZABLE
from src.VictoryMenu import VictoryMenu


if __name__ == '__main__':
    pass
    # Set the game state to the start menu
    game_state = 0
    
    # Initialize pygame
    pygame.init()
    # Create a new window, set to 
    gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), FULLSCREEN | HWSURFACE | RESIZABLE)
    # Set the caption to be the title of the game
    pygame.display.set_caption("Wayfarer 2")
    # Update the display
    pygame.display.flip()
    
    # Initialize a start menu
    start_menu = StartMenu()
    
    # Initialize a pause menu
    pause_menu = PauseMenu()
    
    # Initialize a game over menu
    game_over_menu = GameOverMenu()
    
    # Initialize a victory menu
    game_finished_menu = VictoryMenu()
    
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
            levelRow[j] = Level("maps\\" + files[j], i, j)
        # Add the row of levels to the level list    
        levels.append(levelRow)
        # Tick
        i = i + 1 
    # Close the map file
    map_file.close()
    
    # Initialize coordinates for the current level
    currentLevelX = 2
    currentLevelY = 1
    # Initialize a variable to represent the level currently being drawn
    currentLevel = levels[1][2]
    
    # Initialize the player
    player = Player(100, 100)
    currentLevel.resetPlayer(player)
    
    # Start the clock
    clock = pygame.time.Clock()
    
    '''
    Main loop
    '''
    gameExit = False
    while not gameExit:
        # If the game is on the main menu
        if game_state == 0:
            # Get the current mouse position
            mouse_pos = pygame.mouse.get_pos()
             
            # Draw the menu
            start_menu.draw(gameDisplay, mouse_pos[0], mouse_pos[1])
            
            # For each pygame event
            for event in pygame.event.get():
                # Find the mouse button event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check which menu button was clicked on
                    button_clicked = start_menu.get_button(mouse_pos[0], mouse_pos[1])
                    # If button 1 was clicked
                    if button_clicked == 1:
                        # Return to game
                        game_state = 1
                    # If button 2 was clicked
                    elif button_clicked == 2:
                        # Exit the game
                        gameExit = True
            # Update the screen
            pygame.display.update()
        
            # Tick the clock by one frame        
            clock.tick(30)
        # If the game is running
        elif game_state == 1:
            # Is the game over?
            if currentLevel.is_game_over():
                game_state = 3
            # Has the player won?
            if currentLevel.is_game_won():
                game_state = 4
            # Increment the time by 1
            count_step()
            
            # Draw loop
            gameDisplay.fill((255, 255, 255))
            
            # Draw level
            currentLevel.draw(gameDisplay, pygame.draw)
                
            # Update the screen
            pygame.display.update()
        
            # Tick the clock by one frame        
            clock.tick(30)
            
            # Event loop
            for event in pygame.event.get():   
                # Quit event
                if event.type == pygame.QUIT:
                    gameExit = True
                # Keyboard down event
                if event.type == pygame.KEYDOWN:
                    if event.key == 119:
                        currentLevel.keyboardUp()
                    if event.key == 97:
                        currentLevel.keyboardLeft()
                    if event.key == 100:
                        currentLevel.keyboardRight()
                    if event.key == 115:
                        currentLevel.keyboardDown()
                    if event.key == 27:
                        game_state = 2
                # Keyboard up event
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
            level = currentLevel
            # Run the level for one frame
            level.step()
            ''' Handle transitions for the room '''
            # Get all objects moving from the current room to another
            transitioningObjects = level.checkForTransition()
            # For each object
            for transitioningObject in transitioningObjects:
                # Get the direction of the transition
                transition = transitioningObject[1]
                # If there is a transition
                if transition != "None":
                    # Set the coordinates to (0,0)
                    levelX = 0
                    levelY = 0
                    # For each row of rooms
                    for row in range(len(levels)):
                        # For each room within the row
                        for column in range(len(levels[row])):
                            # If the room at this position is the current level
                            if levels[row][column] == level:
                                # Initialize variables to store the coordinates of this level
                                levelY = row
                                levelX = column
                    
                    # If the transition direction is "Up"
                    if transition == "Up":
                        # If the object is the player
                        if transitioningObject[0].type() == "Player":
                            # Update the current level coordinates
                            currentLevelY -= 1
                            currentLevel = levels[currentLevelY][currentLevelX]
                            currentLevel.resetPlayer(player)
                        # Otherwise
                        else:
                            # Add the object to the proper level
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
        # If the game is currently paused
        elif game_state == 2:
            # Get the current mouse position
            mouse_pos = pygame.mouse.get_pos()
            
            # Draw the level
            currentLevel.draw(gameDisplay, pygame.draw)
             
            # Draw the menu
            pause_menu.draw(gameDisplay, mouse_pos[0], mouse_pos[1])
            
            # For each pygame event
            for event in pygame.event.get():
                # Find the mouse button event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check which menu button was clicked on
                    button_clicked = pause_menu.get_button(mouse_pos[0], mouse_pos[1])
                    # If button 1 was clicked
                    if button_clicked == 1:
                        # Return to game
                        game_state = 1
                    # If button 2 was clicked
                    elif button_clicked == 2:
                        # Exit the game
                        gameExit = True
            # Update the screen
            pygame.display.update()
        
            # Tick the clock by one frame        
            clock.tick(30)
            
        # If the player dies
        elif game_state == 3:
            # Get the current mouse position
            mouse_pos = pygame.mouse.get_pos()
                     
            # Draw the menu
            game_over_menu.draw(gameDisplay, mouse_pos[0], mouse_pos[1])
            
            # For each pygame event
            for event in pygame.event.get():
                # Find the mouse button event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check which menu button was clicked on
                    button_clicked = game_over_menu.get_button(mouse_pos[0], mouse_pos[1])
                    # If button 1 was clicked
                    if button_clicked == 1:
                        # Exit the game
                        gameExit = True
            # Update the screen
            pygame.display.update()
        
            # Tick the clock by one frame        
            clock.tick(30) 
            
                    # If the player dies
        elif game_state == 4:
            # Get the current mouse position
            mouse_pos = pygame.mouse.get_pos()
            
            # Draw the menu
            game_finished_menu(gameDisplay, mouse_pos[0], mouse_pos[1])
            
            # For each pygame event
            for event in pygame.event.get():
                # Find the mouse button event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check which menu button was clicked on
                    button_clicked = game_finished_menu.get_button(mouse_pos[0], mouse_pos[1])
                    # If button 1 was clicked
                    if button_clicked == 1:
                        # Exit the game
                        gameExit = True
            # Update the screen
            pygame.display.update()
        
            # Tick the clock by one frame        
            clock.tick(30)         
    sys.exit()