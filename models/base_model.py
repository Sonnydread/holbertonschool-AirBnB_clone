#!/usr/bin/python3
"""BaseModel class"""


import json
import uuid
import models
import datetime


class BaseModel:
    """BaseModel attributes n methods"""
    def __init__(self, *args, **kwargs):
        """BaseModel attributes n methods"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for keys, value in kwargs.items():
                if keys == "__class__":
                    continue
                if keys == 'id':
                    self.id = value
                elif keys == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif keys == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
                else:
                    setattr(self, keys, value)

    def __str__(self):
        """BaseModel attributes n methods"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})"

    def save(self):
        """BaseModel attributes n methods"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """BaseModel attributes n methods"""
        return dict(self.__dict__, **{'__class__':
                    self.__class__.__name__, 'created_at':
                    self.created_at.isoformat(), 'updated_at':
                    self.updated_at.isoformat()})
