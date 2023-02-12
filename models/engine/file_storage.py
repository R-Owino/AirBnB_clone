#!/usr/bin/python3
"""
Module that defines a class FileStorage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances

    Private class attributes:
        __file_path (str): path to JSON file
        __objects (dict): stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized = {
                key: val.to_dict()
                for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists

        Raises:
            FileNotFound error if file does not exist
        """
        try:
            deserialized = {}
            with open(FileStorage.__file_path, 'r') as f:
                deserialized = json.loads(f.read())
            FileStorage.__objects = {
                    key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserialized.items()}
        except FileNotFoundError:
            return
