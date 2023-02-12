#!/usr/bin/python3
"""Defines a class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Initializes a new amenity instance

    Attributes:
        name (str): name of the amenity
    """
    name = ""
