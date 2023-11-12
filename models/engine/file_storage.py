#!/usr/bin/env python
"""Defines the FileStorage class"""
import json
from Base import BaseModel

class FileStorage:
    """Class that stores objects in JSON strings"""
    __file_path = "file.json"
    __objects = {}

    

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets new object in __objects dictionary"""
        k = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open (self.__file_path, "w") as file:
            json.dump(data, file)
    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                info = json.load(file)
                FileStorage.__objects = {}
                for k, v in info.items():
                    data = FileStorage.classes[v['__class__']](**v)
                    FileStorage.__objects[k] = data
        except FileNotFoundError:
            return
        

