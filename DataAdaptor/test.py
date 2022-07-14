# unit test case
import unittest
from input import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def zip_method(self):
        """
        zip test function
        """
        inp = InputAdaptor()
        inputfunc = inp.zip_upload('', '') #enter zip file and cloud name
        # enter output file name for comparision
        output_values = ""
        # assertEqual() to check true of test value
        self.assertEqual(inputfunc, output_values)


if __name__ == '__main__':
    unittest.main()
