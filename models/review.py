#!/usr/bin/python3
'''
class Review
'''
from models.base_model import BaseModel
class Review(BaseModel):
    '''
    Defines attributes that identify a reviewer and their review
    '''
    place_id = ""
    user_id = ""
    text = ""
