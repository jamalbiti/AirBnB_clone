#!/usr/bin/env python3
"""
Module of the class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class State

    Attributes:
        name (str): string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
