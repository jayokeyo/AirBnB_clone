'''
FileStorage
'''
import json
from models.base_model import BaseModel
class FileStorage(BaseModel):
    '''
    Defines class FileStorage for conducting JSON dump and JSON load
    '''
    __file_path = "file.json"
    __objects = {}

