#!/usr/bin/env python

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.engine.file_storage import classes

storage = FileStorage()
storage.FileStorage.classes = {"BaseModel": BaseModel}
storage.reload()
