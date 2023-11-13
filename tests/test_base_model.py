#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelDict(unittest.TestCase):
    def test_init_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

        # Check if datetime objects are properly converted from strings
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertEqual(type(my_new_model.updated_at), datetime)

        # Check if other attributes are equal
        self.assertEqual(my_model.__class__, my_new_model.__class__)

        # Check if __str__ representation is the same
        self.assertEqual(str(my_model), str(my_new_model))

    def test_instance_equality(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        # Check if the instances are not the same
        self.assertFalse(my_model is my_new_model)

if __name__ == '__main__':
    unittest.main()
