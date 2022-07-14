# unit test case
import unittest
from input import InputAdaptor


class TestInputMethods(unittest.TestCase):
    """
    test class
    """

    def url_method(self):
        """
        test function
        """
        input_values = InputAdaptor()
        inputFunc = input_values.url_upload(
            'file-url', 'Aws')
        #  output values for comparision
        output_values = "Temp/file-url-object-name"
        # assertEqual() to check true of test value
        self.assertEqual(inputFunc, output_values)


if __name__ == '__main__':
    unittest.main()
