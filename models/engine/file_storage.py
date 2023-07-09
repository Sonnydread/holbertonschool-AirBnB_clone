#!/usr/bin/python3
"""FileStorage class"""


import os.path
import json
from typing import List
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Settings 4 FileStorage"""
        return self.__objects

    def new(self, obj):
        """Settings 4 FileStorage"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Settings 4 FileStorage"""
        d1 = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                d1[key] = value.to_dict()
            f.write(json.dumps(d1))

    def reload(self):
        """Settings 4 FileStorage"""
        cls = ["BaseModel", "User", "State", "City",
               "Place", "State", "Amenity", "Review"]
        try:
            with open(self.__file_path, 'r') as f:
                dictio = json.loads(f.read())
            for key in dictio.keys():
                value = dictio[key]
                if value['__class__'] in cls:
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
