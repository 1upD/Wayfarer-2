'''
Created on May 9, 2015

@author: Derek Dik
'''

import pygame

from src.GuiButton import GuiButton

class StartMenu(object):
    '''
    Object to model a menu when the game is paused
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._background = pygame.image.load("images\\UI\\Title.png")
        self._start_button = GuiButton(250, 150, 200, 100, pygame.image.load("images\\UI\\StartButton.png"))
        self._quit_button = GuiButton(250, 350, 200, 100, pygame.image.load("images\\UI\\QuitButton.png"))       
    
    def draw(self, gameDisplay, mouseX, mouseY):
        # Draw the background
        gameDisplay.blit(self._background, (0, 0))
        # Draw the start button
        self._start_button.draw(gameDisplay)
        # Draw the quit button
        self._quit_button.draw(gameDisplay)
    
    def get_button(self, mouseX, mouseY):
        '''
        Function to check if the player has selected an option yet
        Returns 0 if no option has been selected
        Returns 1 if the user has clicked "start"
        Returns 2 if the user has clicked "quit"
        ''' 
        if self._start_button.test(mouseX, mouseY):
            return 1
        elif self._quit_button.test(mouseX, mouseY):
            return 2
            print("quit button pressed")
        else:
            return 0
        