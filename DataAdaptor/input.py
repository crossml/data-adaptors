import os
from config import EXTENSION_LIST


class InputAdaptor:
    def __init__(self,):
        pass

    def fileAdaptor(local_file_path):
        try:
            extension = os.path.splitext(local_file_path)[-1].lower()
            if extension in EXTENSION_LIST:
                return ['valid File Extension']
            else:
                raise TypeError("invalid file extension")
        except FileNotFoundError:
            return False
