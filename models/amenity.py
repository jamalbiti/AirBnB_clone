#!/usr/bin/env python3
"""
Module for the class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity

    Attributes:
        name (str): string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
