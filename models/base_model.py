#!/usr/bin/python3
"""
Module: base.py

Handles the foundation for creating model classes with consistent
attributes and methods.
"""

import datetime
import uuid

import models


class BaseModel:
    """
    Establishes a base class for defining model classes with common
    attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a model instance with its attributes.

        Prioritizes kwargs for potential dictionary-based object creation.
        """
        if kwargs:
            self._initialize_from_dict(kwargs)  # Refactored logic for clarity
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def _initialize_from_dict(self, kwargs):
        """
        Initializes attributes from a provided dictionary,
        handling date-time conversions appropriately.
        """
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            elif key in ('created_at', 'updated_at'):
                value = datetime.fromisoformat(value)
            setattr(self, key, value)

    def __str__(self):
        """
        Provides a user-friendly string representation of the model instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"  # Using f-strings

    def save(self):
        """
        Updates the 'updated_at' attribute and triggers model storage persistence.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the model instance,
        including class name and formatted date-time values.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = type(self).__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()

        return model_dict

