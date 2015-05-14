'''
Created on May 9, 2015

@author: Derek Dik
'''
from src.Resource import Resource
from src.Sprite import Sprite

class FoodResource(Resource):
    '''
    Subclass of resource to represent food
    '''

    _resource_value = 150
    _type = "food_resource"
    _color = [0, 255, 0]
    _color_deactived = [100, 200, 100]
    _sprite = Sprite("images/foods/food.dat")