# unit test case
import unittest
from input import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def url_method(self):
        """
        url test function
        """
        input_values = InputAdaptor()
        inputfunc = input_values.url_upload(
            '', '')  # enter url and cloud name
        # enter output file name for comparision
        output_values = ""
        # assertEqual() to check true of test value
        self.assertEqual(inputfunc, output_values)


if __name__ == '__main__':
    unittest.main()
