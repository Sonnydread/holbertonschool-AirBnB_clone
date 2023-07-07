#!/usr/bin/python3
"""BaseModel class"""


import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel attributes n methods"""
    def __init__(self, *args, **kwargs):
        """BaseModel attributes n methods"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'updated_at' or k == 'created_at':
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """BaseModel attributes n methods"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})"

    def save(self):
        """BaseModel attributes n methods"""
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """BaseModel attributes n methods"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
