import unittest
from src import data_structures

class TestDataStructures(unittest.TestCase):

    def test_list(self):
        self.assertEqual(data_structures.list_example(), [1, 2, 3, 4, 5])

    def test_tuple(self):
        self.assertEqual(data_structures.tuple_example(), (1, 2, 3, 4, 5))

    def test_set(self):
        self.assertEqual(data_structures.set_example(), {1, 2, 3, 4, 5})

    def test_dict(self):
        self.assertEqual(data_structures.dict_example(), {'key1': 'value1', 'key2': 'value2'})

if __name__ == '__main__':
    unittest.main()