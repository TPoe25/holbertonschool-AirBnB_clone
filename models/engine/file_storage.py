#!/usr/bin/python3
""" defines the engine """

import json
import os
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        objectkey = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[objectkey] = obj

    def save(self):
        serialized_objs = {}
        for objectkey, obj in FileStorage.__objects.items():
            serialized_objs[objectkey] = obj.to_dict()
            
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)
            
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                serialized_objs = json.load(file)
                for objectkey, obj_dict in serialized_objs.items():
                    class_name, obj_id = objectkey.split(".")
                    class_obj = globals()[class_name]
                    
                    obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj = class_obj(**obj_dict)
                    self.new(obj)
        except FileNotFoundError:
            pass
