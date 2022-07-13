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
        except FileNotFoundError:
            return ("file not found")
