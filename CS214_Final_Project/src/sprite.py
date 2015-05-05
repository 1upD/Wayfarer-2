'''
Created on May 2, 2015

@author: 1upde_000
'''
import pygame
import os

class sprite(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Object to store images and display them as an animation
        '''
        self.sprite_list = []
        sprite_file = open(fileName, "r")
        self.total = 0
        self.current = 0
        for line in sprite_file:
            line = line.strip('\n')
#            sprite = pygame.image.load("images\\player\\Walkk0000.png")
            sprite = pygame.image.load(line)
            sprite.convert_alpha()
            print(line)
            self.sprite_list.append(sprite)
            self.total += 1
        
    def draw(self, gameDisplay, draw, x, y):
        gameDisplay.blit(self.sprite_list[self.current], (x, y))
        self.current += 1
        if self.current == self.total:
            self.current = 0