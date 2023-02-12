#!/usr/bin/python3
"""Defines a class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Initializes a new city

    Attributes:
        state_id (str): unique state identifier State.id
        name (str): name of the city
    """

    state_id = ""
    name = ""
