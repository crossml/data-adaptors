# unit test case
import unittest
from test import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def file_method(self):
        """
        file test function
        """
        inp = InputAdaptor()
        inputfunc = inp.file_upload('',  '')  # enter file and cloud name
        output_values = ""  # enter output file name for comparision
        # assertEqual() to check true of test value
        self.assertEqual(inputfunc, output_values)


if __name__ == '__main__':
    unittest.main()
