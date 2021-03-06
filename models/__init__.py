#!/usr/bin/python3
"""initiallizer"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


all_cls = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}

storage = FileStorage()
storage.reload()
