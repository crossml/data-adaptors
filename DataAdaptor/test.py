# unit test case
import unittest
from test import InputAdaptor


class TestStringMethods(unittest.TestCase):
    """
    test class
    """

    def test_positive(self):
        """
        test function
        """
        inp = InputAdaptor()
        testValue = inp.file_upload('db.pdf',  'Aws')
        # enter desired output
        message = "Temp/db.pdf"
        # assertEqual() to check true of test value
        self.assertEqual(testValue, message)


if __name__ == '__main__':
    unittest.main()
