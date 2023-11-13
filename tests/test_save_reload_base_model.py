#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
import os


class TestSaveReloadBaseModel(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_reload_base_model(self):
        all_objs_before = storage.all()

        print("-- Reloaded objects --")
        for obj_id in all_objs_before.keys():
            obj = all_objs_before[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

        all_objs_after = storage.all()
        self.assertIn(my_model, all_objs_after.values())


if __name__ == '__main__':
    unittest.main()
