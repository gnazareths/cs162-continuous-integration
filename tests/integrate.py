import os
import unittest

class Tests(unittest.TestCase):

    def is_integer(self):
        int_type = type(7)
        assert int_type == int

if __name__ == "__main__":
    unittest.main()
