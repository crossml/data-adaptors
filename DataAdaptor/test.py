# unit test case
import unittest
from input import InputAdaptor


class TestStringMethods(unittest.TestCase):
    """
    test class
    """
    def test_positive(self):
        """
        test function
        """
        input_values = InputAdaptor()
        testValue = input_values.url_upload(
            'http://www.file.fyicenter.com/a/sample.tif', 'Aws')
        # enter desired output
        message = "Temp/sample.tif"
        # assertEqual() to check true of test value
        self.assertEqual(testValue, message)


if __name__ == '__main__':
    unittest.main()
