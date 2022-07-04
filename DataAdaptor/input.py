"""
test
"""
import os
import boto3
# from config import EXTENSION_LIST

class InputAdaptor:
    """
    Input Adaptor class
    """

    def __init__(self):
        pass

    def file_adaptor(self,local_file_path, s3_bucket_name,s3_storage_file_path):
        """
        File Input Funtion
        """

        session = boto3.Session()
        s3 = session.resource('s3')
        try:
            extension = os.path.splitext(local_file_path)[-1].lower()
            if extension in EXTENSION_LIST:
                bucket = s3_bucket_name
                # print(local_file_path, cloud_name)
                s3.meta.client.upload_file(local_file_path, bucket, s3_storage_file_path)
                print("Upload Successful",s3_storage_file_path)
        except FileNotFoundError:
            print("file not found")
        