import config
from botocore.exceptions import NoCredentialsError
import os
from config import extensions_list


class Input:
    def __init__(self,):
        self.local_file = 'db.pdf'
        self.s3_file = 'Temp/db3.pdf'
        self.bucket = config.AWS_S3_BUCKET
    def fileAdaptor(self,s3):
        try:
            ext = os.path.splitext(self.local_file)[-1].lower()
            if ext in extensions_list:
                s3.meta.client.upload_file(self.local_file, self.bucket, self.s3_file)
                print("Upload Successful")
                return self.s3_file
            else:
                print(self.local_file, "is an unknown file format.")

        except FileNotFoundError:
            return False
        except NoCredentialsError:
            return False
