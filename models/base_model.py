#!/usr/bin/python3
""" defines a base model for Air BnB console"""


from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class for common attributes and methods for other classes
    """
    
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance
        
        Attributes:
        - id: str - unique identifier for instance
        - created_at: datetime - Date and time when the instance was created
        - updated_at: datetime - Date and time when the instance last updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, str):
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        
    def __str__(self):
        """
        Returns a string representation of the object
        
        Returns:
        - str: string representation of the object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        """
        Updating the refresh attribute with current datetime
        """
        from models.engine.file_storage import FileStorage
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary representation of the object
        
        Returns: dictionary: dictionary representation of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
