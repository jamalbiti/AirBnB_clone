#!/usr/bin/env python3
"""
Module of te class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User

    Attributes:
        email (str): The email address
        password (str): The password
        first_name (str): The first name
        last_name (str): The last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
