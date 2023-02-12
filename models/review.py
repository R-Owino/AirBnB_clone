#!/usr/bin/python3
"""Defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Initalizes a new review instance

    Attributes:
        place_id (str): Place_id
        user_id (str): User_id
        text (str): textual review
    """

    place_id = ""
    user_id = ""
    text = ""
