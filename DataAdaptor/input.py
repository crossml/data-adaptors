"""
Input File
"""

from urllib.parse import urlparse
import requests


class InputAdaptor:
    """
    Input Adaptor class
    """

    def url_upload(self, link, colud_name):
        """
        url file upload Function
        """
        try:
            url_object = requests.get(link, stream=True).raw
            file_name = os.path.basename(urlparse(link).path)
            extension = os.path.splitext(file_name)[-1].lower()
            if extension in EXTENSION_LIST:
                if colud_name.lower() == 'aws':
                    S3.meta.client.upload_fileobj(
                        url_object, S3_BUCKET_NAME, INPUT_FILE_FOLDER + file_name)
                    return INPUT_FILE_FOLDER+file_name
                else:
                    return ('invalid cloud option')
            else:
                return ("invalid url")
        except IOError:
            return ("url not found")
