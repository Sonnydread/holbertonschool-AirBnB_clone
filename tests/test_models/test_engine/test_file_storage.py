"""Testing file storage engine"""
import unittest
import models
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """Testing file storage engine"""

    def test_FileStorage(self):
        f1 = FileStorage()
        self.assertAlmostEqual(f1._FileStorage__file_path, "file.json")
        self.assertIsInstance(f1._FileStorage__objects, dict)

    def test_all(self):
        f2 = FileStorage()
        self.assertAlmostEqual(f2.all(), f2._FileStorage__objects)

    def test_new(self):
        b1 = BaseModel()
        self.assertIn(f"BaseModel.{b1.id}", models.storage.all().keys())

    def test_save(self):
        self.assertRaises(TypeError, models.storage.save, None)

    def test_reload(self):
        bm = BaseModel()
        models.storage.save()
        self.assertAlmostEqual(os.path.exists("file.json"), True)

        file_path = FileStorage._FileStorage__file_path
        os.remove(file_path)

        models.storage._FileStorage__objects.clear()
        self.assertAlmostEqual(os.path.exists("file.json"), False)
        self.assertAlmostEqual(models.storage.reload(), None)
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 0)

        models.storage.new(BaseModel())
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 1)
        self.assertAlmostEqual(os.path.exists("file.json"), False)
        models.storage.save()
        if os.path.exists("file.json"):
            with open("file.json", 'r')as f:
                letras = len(f.read())
        self.assertAlmostEqual(os.path.exists("file.json"), True)
        models.storage.new(BaseModel())
        models.storage.reload()
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 2)
        if os.path.exists("file.json"):
            with open("file.json", 'r')as f:
                letras2 = len(f.read())
        self.assertAlmostEqual(letras, letras2)
        os.remove('file.json')
        obj = User()
        models.storage.save()
        models.storage.reload()
        all_ = models.storage.all()
        self.assertIsInstance(all_, dict)
