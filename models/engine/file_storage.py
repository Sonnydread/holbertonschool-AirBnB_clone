#!/usr/bin/python3
"""FileStorage class"""


import os.path
import json
from typing import List


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Settings 4 FileStorage"""
        return self.__objects

    def new(self, obj):
        """Settings 4 FileStorage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Settings 4 FileStorage"""
        with open(self.__file_path, 'w') as fe:
            dict_ = {k: v.to_dict() for k, v in self.__objects.items()}
            fe.write(json.dumps(dict_))

    def reload(self):
        """Settings 4 FileStorage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fe:
                dict_ = json.loads(fe.read())
            for k in dict_.keys():
                value = dict_[k]
                self.__objects[k] = eval(value['__class__'])(**value)
        else:
            pass
