"""
Input File
"""
import os
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
    try:
        # saving file to s3
        S3.meta.client.upload_file(
            local_file_path, S3_BUCKET_NAME, INPUT_FILE_FOLDER + os.path.basename(local_file_path))
        return INPUT_FILE_FOLDER + os.path.basename(local_file_path)
    except Exception as error:
        return error


class InputAdaptor:
    """
    Input Adaptor class
    """

    def __init__(self):
        pass

    def file_upload(self, local_file_path, cloud_name):
        """
        File Input Funtion
        """
        try:
            extension = os.path.splitext(local_file_path)[-1].lower()
            if extension in EXTENSION_LIST:
                if cloud_name.lower() == 'aws':
                    upload_file_to_s3(local_file_path)
                    return INPUT_FILE_FOLDER+local_file_path
                else:
                    raise Exception("Sorry, invalid cloud ")
        except FileNotFoundError:
            return ("file not found")
