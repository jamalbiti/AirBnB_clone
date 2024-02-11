#!/usr/bin/env python3
"""
Module of the class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class Place

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name
        description (str): A description
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The max number of guests
        price_by_night (int): The price per night
        latitude (float): The latitude coordinate
        longitude (float): The longitude coordinate
        amenity_ids (str): Amenity IDs associated
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
