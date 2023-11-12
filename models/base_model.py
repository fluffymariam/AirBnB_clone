#!/usr/bin/python3
"""
BaseModel Module

This module defines the BaseModel class.
"""
import models
import uuid
from datetime import datetime
#from models import storage

class BaseModel:
    """
    BaseModel Class

    Defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        When creating an instance from dict representation, pass the dict
        as **kwargs to reconstruct the object.
        """
        if kwargs:  # If kwargs is not empt, create an instance from dict rep
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert created_at and updated_at to datetime objects
                    parsed_datetime = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                            )
                    setattr(self, key, parsed_datetime)
                else:
                    setattr(self, key, value)
        else:  # If kwargs is empty, create new instance with new
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
        str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Updates the public attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
        dict: A dictionary containing all attributes of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
