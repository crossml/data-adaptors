# unit test case
import unittest
from input import InputAdaptor

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> bb27d4a48f36197265e7fe4155ece367de86d38b
=======
>>>>>>> bb27d4a48f36197265e7fe4155ece367de86d38b
class TestInputMethods(unittest.TestCase):
    """
    test class
    """

<<<<<<< HEAD
<<<<<<< HEAD
    def ftp_method(self):
        """
        ftp test function
        """
        input_values = InputAdaptor()
        # enter ftp host, username, password, ftp folder path, cloud name
        inputfunc = input_values.ftp_upload('', '', '', '', '')
        # enter list of output files present in ftp folder for comparision
        output_values = ""
=======
=======
>>>>>>> bb27d4a48f36197265e7fe4155ece367de86d38b
    def zip_method(self):
        """
        zip test function
        """
        inp = InputAdaptor()
        inputfunc = inp.zip_upload('', '') #enter zip file and cloud name
        # enter output file name for comparision
        output_values = ""


    def url_method(self):
        """
        url test function
        """
        input_values = InputAdaptor()
        inputfunc = input_values.url_upload(
            '', '')  # enter url and cloud name
        # enter output file name for comparision
        output_values = ""

    def file_method(self):
        """
        file test function
        """
        inp = InputAdaptor()
        inputfunc = inp.file_upload('',  '')  # enter file and cloud name
        output_values = ""  # enter output file name for comparision


<<<<<<< HEAD
>>>>>>> bb27d4a48f36197265e7fe4155ece367de86d38b
=======
>>>>>>> bb27d4a48f36197265e7fe4155ece367de86d38b
        # assertEqual() to check true of test value
        self.assertEqual(inputfunc, output_values)


if __name__ == '__main__':
    unittest.main()
