#!/usr/bin/python3
'''
class BaseModel
defines all common attributes/methods for other classes
'''
import datetime
import uuid
class BaseModel:
    '''
    BaseModel with attributes and methods inherited by other classes
    '''
    def __init__(self):
        '''
        creates new instance of the BaseModel
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    def __str__(self):
        '''
        defines how the returned string is printed out in stdout
        '''
        print([<class name>] (<self.id>) <self.__dict__>)
