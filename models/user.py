#!/usr/bin/python3
'''
Class User
'''
from models.base_model import BaseModel
class User(BaseModel):
    '''
    Defines class User with attributes that describe the application user
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

