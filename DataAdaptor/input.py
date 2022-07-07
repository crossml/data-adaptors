"""
Input File
"""
import zipfile


class InputAdaptor:
    """
    Input Adaptor class
    """

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
