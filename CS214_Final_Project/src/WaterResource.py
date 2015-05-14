'''
Created on May 9, 2015

@author: Derek Dik
'''
from src.Resource import Resource
from src.Sprite import Sprite

class WaterResource(Resource):
    '''
    Subclass of resource to represent water
    '''

    _resource_value = 300
    _type = "water_resource"
    _sprite = Sprite("images/water/water.dat")
        