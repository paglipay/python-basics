import unittest
import sys
sys.path.append('../src')
import modules

class TestModules(unittest.TestCase):

    def test_import(self):
        # Test if the module is imported correctly
        self.assertIsNotNone(modules)

    # Add more tests here to check the functionality of your modules

if __name__ == '__main__':
    unittest.main()