import os
from config import EXTENSION_LIST


class InputAdaptor:
    def __init__(self,):
        pass

    def fileAdaptor(self,local_file_path,cloud_name):
        try:
            extension = os.path.splitext(local_file_path)[-1].lower()
            if extension in EXTENSION_LIST:
                return (local_file_path,cloud_name)
            else:
                raise TypeError("invalid file extension")
        except FileNotFoundError:   
            return ("file not found")
