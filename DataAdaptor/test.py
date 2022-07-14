# unit test case
import unittest
from test import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def file_method(self):
        """
        test function
        """
        inp = InputAdaptor()
        inputFunc = inp.file_upload('file-name',  'Aws')
        output_values = "Temp/file-name"  # output values for comparision
        # assertEqual() to check true of test value
        self.assertEqual(inputFunc, output_values)


if __name__ == '__main__':
    unittest.main()
