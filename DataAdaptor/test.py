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
        testValue = input_values.ftp_upload(
            '3.139.88.10', 'ftpuser', 'ftpuser', '/Payal_Sample/', 'aws')
        # enter desired output
        message = "[Temp/0104426000.tif]"
        # assertEqual() to check true of test value
        self.assertEqual(testValue, message)


if __name__ == '__main__':
    unittest.main()
