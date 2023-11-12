#!/usr/bin/python3

"""This module implements the FileStorage class"""

import json
import models


class FileStorage():
    '''FileStorage class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects and saves them to a JSON file"""
        json_object = {}

        for key in FileStorage.__objects:
            json_object[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                info = json.load(file)
                FileStorage.__objects = {}
                for k, v in info.items():
                    class_name = v.get('__class__')
                    if class_name:
                        model_class = getattr(models, class_name, None)
                        if model_class:
                            obj = model_class(**v)
                            FileStorage.__objects[k] = obj
        except FileNotFoundError:
            return

