import unittest
from src import basics

class TestBasics(unittest.TestCase):

    def test_variables(self):
        self.assertEqual(basics.my_variable, 'Hello, World!')

    def test_data_types(self):
        self.assertIsInstance(basics.my_int, int)
        self.assertIsInstance(basics.my_float, float)
        self.assertIsInstance(basics.my_bool, bool)
        self.assertIsInstance(basics.my_str, str)

    def test_operators(self):
        self.assertEqual(basics.add(1, 2), 3)
        self.assertEqual(basics.subtract(5, 3), 2)
        self.assertEqual(basics.multiply(2, 3), 6)
        self.assertEqual(basics.divide(6, 2), 3)

if __name__ == '__main__':
    unittest.main()