"""
Input File
"""

import ftplib
from contextlib import closing


class InputAdaptor:
    """
    Input Adaptor class
    """

    def __init__(self):
        pass

    def ftp_upload(self, ftp_host, username, password, ftp_folder_path, cloud_name):
        """
        ftp file upload function
        """
        try:
            with closing(ftplib.FTP()) as ftp:
                # connect to the FTP server
                ftp.connect(ftp_host, 21, 30*5)  # 5 mins timeout
                ftp.login(username, password)
                ftp.set_pasv(True)

                # get filenames within the directory
                filenames = ftp.nlst(ftp_folder_path)
                lst = []
                for filename in filenames:
                    # extrating particular filename from filenames
                    tmp_path = os.path.join('/tmp', os.path.basename(filename))
                    extension = os.path.splitext(tmp_path)[-1].lower()
                    if extension in EXTENSION_LIST:
                        # check if valid allowed extension
                        if not os.path.exists(tmp_path):
                            # check if file already exist in tmp folder
                            with open(tmp_path, 'wb') as f:
                                # writing file at /tmp folder
                                ftp.retrbinary('RETR %s' %
                                               filename, f.write)
                                if cloud_name.lower() == 'aws':
                                    # calling function to save data to s3
                                    s3_file = upload_file_to_s3(tmp_path)
                                    lst.append(s3_file) # appending s3's response to list
                                else:
                                    raise Exception("Sorry, invalid cloud ")
                        else:
                            return ("file already exist in tmp folder ")
                    else:
                        return ("Sorry, file format")
            return lst
        except Exception as error:
            return error
