# unit test case
import unittest
from input import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def ftp_method(self):
        """
        ftp test function
        """
        input_values = InputAdaptor()
        # enter ftp host, username, password, ftp folder path, cloud name
        inputfunc = input_values.ftp_upload('', '', '', '', '')
        # enter list of output files present in ftp folder for comparision
        output_values = ""
        # assertEqual() to check true of test value
        self.assertEqual(inputfunc, output_values)


if __name__ == '__main__':
    unittest.main()
