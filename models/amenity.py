#!/usr/bin/pyhton3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amentiy.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
