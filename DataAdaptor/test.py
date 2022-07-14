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
        inp = InputAdaptor()
        inputFunc = inp.zip_upload('zip-file-name', 'Aws')
        # output values for comparision
        output_values = "Temp/zip-file-name"
        # assertEqual() to check true of test value
        self.assertEqual(inputFunc, output_values)


if __name__ == '__main__':
    unittest.main()
