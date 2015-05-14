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
    rate = 1
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
#            sprite.convert_alpha()
            print(line)
            self.sprite_list.append(sprite)
            self.total += 1
        
    def draw(self, gameDisplay, x, y):
        gameDisplay.blit(self.sprite_list[self.current], (x, y))
        self.current += self.rate
        if self.current == self.total:
            self.current = 0
            
    def draw_with_direction(self, gameDisplay, direction, x, y):
        gameDisplay.blit(rot_center(self.sprite_list[self.current], direction), (x, y))
        self.current += self.rate
        if self.current == self.total:
            self.current = 0 
            
    ''' Accessors and mutators'''
    def get_frame(self):
        return self.current
    def set_rate(self, rate):
        self.rate = rate
    def set_frame(self, frame):
        self.current = frame
    def is_animation_done(self):
        return self.current == self.total - 1


# Function from pygame.org         
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

