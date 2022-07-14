# unit test case
import unittest
from input import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def ftp_method(self):
        """
        test function
        """
        input_values = InputAdaptor()
        inputFunc = input_values.ftp_upload(
            '3.139.88.10', 'ftpuser', 'ftpuser', '/Payal_Sample/', 'aws')
        # output values for comparision
        output_values = "['list-of-input-files']"
        # assertEqual() to check true of test value
        self.assertEqual(inputFunc, output_values)


if __name__ == '__main__':
    unittest.main()
