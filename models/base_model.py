#!/usr/bin/python3
"""
BaseModel class defines common attributes/methods for other classes,
handling initialization, serialization, and deserialization of instances
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Return string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """Update the public instance updated_at and save to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Return the dictionary representation of the instance"""
        to_dict = dict(self.__dict__)
        to_dict["__class__"] = self.__class__.__name__
        if not isinstance(to_dict["created_at"], str):
            to_dict["created_at"] = to_dict["created_at"].isoformat()
        if not isinstance(to_dict["updated_at"], str):
            to_dict["updated_at"] = to_dict["updated_at"].isoformat()
        return to_dict
