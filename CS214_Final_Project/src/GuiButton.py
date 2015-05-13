'''
Created on May 9, 2015

@author: 1upde_000
'''

class GuiButton(object):
    '''
    A button that is displayed over the screen and can be clicked by the player
    '''


    def __init__(self, x, y, w, h, image):
        '''
        Constructor
        '''
        self._image = image
        self._x = x
        self._y = y
        self._w = w
        self._h = h
    def draw(self, gameDisplay):
        gameDisplay.blit(self._image, (self._x, self._y))
    

    def test(self, mouseX, mouseY):
        '''
        Returns true if mouseX and mouseY are within the button's bounds
        '''
        return mouseX < self._x + self._w and mouseX > self._x and mouseY > self._y and mouseY < self._y + self._h