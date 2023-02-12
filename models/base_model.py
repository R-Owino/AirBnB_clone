#!/usr/bin/python3
"""Module that defines the class BaseModel from which other classes inherit"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    BaseModel class

    Public instance attributes:
        id (string): unique id for each BaseModel instance

        created_at (datetime): assigns current datetime
        when an instance is created

        updated_at (datetime): assign with the current datetime
        when an instance is created and it is updated
        every time the object is changed
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance

        Args:
            *args (tuple): unused
            **kwargs (dict): key/value pairs of attributes
        """
        date_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, date_form)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary representation of a BaseModel instance.
        """
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict

    def __str__(self):
        """
        Prints [<class name>] (<self.id>) <self.__dict__>
        the string representation of a BaseModel instance
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
