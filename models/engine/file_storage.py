#!/usr/bin/python3
""" FileStorage Module """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ FileStorage class for managing serialization and deserialization """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Retrieve all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Add a new object to storage """
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className + "." + id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """ Save objects to JSON file """
        filepath = FileStorage.__file_path
        data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """ Reload objects from JSON file """
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        elif "User" in key:
                            data[key] = User(**value)
                        elif "Place" in key:
                            data[key] = Place(**value)
                        elif "State" in key:
                            data[key] = State(**value)
                        elif "City" in key:
                            data[key] = City(**value)
                        elif "Amenity" in key:
                            data[key] = Amenity(**value)
                        elif "Review" in key:
                            data[key] = Review(**value)
            except Exception:
                pass
