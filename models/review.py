#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class represents a review for a place """

    place_id = ""
    user_id = ""
    text = ""
