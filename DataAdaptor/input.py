"""
Input File
"""
import requests
import os
import boto3
import zipfile
from urllib.parse import urlparse
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
        
        
    def zip_upload(self, zip_file, cloud_name):
        '''
        zip file upload Function
        '''
        try:
            if zipfile.is_zipfile(zip_file):
                # checking given file is zip
                with zipfile.ZipFile(zip_file, "r") as zip_file_name:
                    # reading zip file
                    for file_name in zip_file_name.namelist():
                        # extracting files from zip
                        extension = os.path.splitext(file_name)[-1].lower()
                        if extension not in EXTENSION_LIST:
                            # checking if any invalid extension file in present in zip file
                            raise Exception("Sorry, invalid zip file")

                if cloud_name.lower() == 'aws':
                    #checking cloud name
                    upload_file_to_s3(zip_file)                    
                    return INPUT_FILE_FOLDER+zip_file

                else:
                    return ("Sorry, invalid cloud ")
            else:
                return ("Sorry, given File is not a zip file ")

    

    def url_upload(self, link, colud_name):
        """
        url file upload Function
        """
        try:
            # saving file in object from url
            url_object = requests.get(link, stream=True).raw
            file_name = os.path.basename(urlparse(link).path)
            # extracting file extension
            extension = os.path.splitext(file_name)[-1].lower()
            if extension in EXTENSION_LIST:
                # check file extension is valid from specified extension list
                if colud_name.lower() == 'aws':
                    # checking cloud name
                    S3.meta.client.upload_fileobj(
                        url_object, S3_BUCKET_NAME, INPUT_FILE_FOLDER + file_name)  # saving data to s3
                    return INPUT_FILE_FOLDER+file_name
                else:
                    return ('invalid cloud option')
            else:
                return ("invalid url")
        except IOError:
            return ("url not found")

    
    def file_upload(self, local_file_path, cloud_name):
        """
        File Input Funtion
        """
        try:
            extension = os.path.splitext(local_file_path)[-1].lower()
            if extension in EXTENSION_LIST:
                # check file extension is valid from specified extension list
                if cloud_name.lower() == 'aws':
                    # checking cloud name
                    # calling function to save data to s3
                    upload_file_to_s3(local_file_path)
                    return INPUT_FILE_FOLDER+local_file_path
                else:
                    raise Exception("Sorry, invalid cloud ")

        except FileNotFoundError:
            return ("file not found")
