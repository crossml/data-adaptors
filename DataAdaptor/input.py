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
        # checking if file is already exist in s3
        res = S3.meta.client.list_objects_v2(Bucket=S3_BUCKET_NAME,
                                             Prefix=INPUT_FILE_FOLDER +
                                             os.path.basename(local_file_path),
                                             MaxKeys=1)
        if ('Contents' in res) is True:
            print("file already exist in s3")
        else:
            # saving file to s3
            S3.meta.client.upload_file(
                local_file_path, S3_BUCKET_NAME, 'Temp/' + os.path.basename(local_file_path))
            print("Upload Successful", 'Temp/' +
                  os.path.basename(local_file_path))
            return 'Temp/' + os.path.basename(local_file_path)
    except Exception as error:
        print(error)


class InputAdaptor:
    """
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
