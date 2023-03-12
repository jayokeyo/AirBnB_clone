#!/usr/bin/python3
'''
class BaseModel
defines all common attributes/methods for other classes
'''
import models
import datetime
import uuid
class BaseModel:
    '''
    BaseModel with attributes and methods inherited by other classes
    '''
    def __init__(self, *args, **kwargs):
        '''
        creates new instance of the BaseModel
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if (len(kwargs != 0)):
            for key, value in kwargs.items():
                if (key == "created_at" or key == "updated_at"):
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        '''
        defines how the returned string is printed out in stdout
        '''
        return "{}({}){}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the attribute updated_at with the current datetime value
        '''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all defined attributes of an object
        '''
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
