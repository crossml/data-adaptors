"""
Input File
"""
import os
import zipfile
from urllib.parse import urlparse
import requests
import boto3
from config import EXTENSION_LIST
from config import S3_BUCKET_NAME
from config import INPUT_FILE_FOLDER

SESSION = boto3.Session()
S3 = SESSION.resource('s3')


def upload_file_to_s3(local_file_path):
    """
    Upload File to s3
    """
    S3.meta.client.upload_file(
        local_file_path, S3_BUCKET_NAME, INPUT_FILE_FOLDER+local_file_path)


class InputAdaptor:
    """
    global session
    Input Adaptor class
    """

    def __init__(self):
        pass

    def file_upload(self, local_file_path, colud_name):
        """
        File Input Funtion
        """
        try:
            extension = os.path.splitext(local_file_path)[-1].lower()
            if extension in EXTENSION_LIST:
                if colud_name.lower() == 'aws':
                    upload_file_to_s3(local_file_path)
                    print("Upload Successful",
                          INPUT_FILE_FOLDER+local_file_path)
                else:
                    raise Exception("Sorry, invalid cloud ")
        except FileNotFoundError:
            print("file not found")

    def zip_upload(self, zip_file, cloud_name):
        '''
        zip file upload Function
        '''
        try:
            if zipfile.is_zipfile(zip_file):
                with zipfile.ZipFile(zip_file, "r") as zip_file_name:
                    for file_name in zip_file_name.namelist():
                        extension = os.path.splitext(file_name)[-1].lower()
                        if extension not in EXTENSION_LIST:
                            raise Exception("Sorry, invalid zip file")

                if cloud_name.lower() == 'aws':
                    upload_file_to_s3(zip_file)
                    print('upload success', INPUT_FILE_FOLDER+zip_file)
                else:
                    raise Exception("Sorry, invalid cloud ")
            else:
                raise Exception("Sorry, given File is not a zip file ")
        except FileNotFoundError:
            print("file not found")
