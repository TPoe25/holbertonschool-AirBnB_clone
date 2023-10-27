#!/bin/usr/python3
""" defines the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class for the users email, password, first_name, last_name
    
    """
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
