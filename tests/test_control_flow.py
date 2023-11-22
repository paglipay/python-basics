import unittest
from src import control_flow

class TestControlFlow(unittest.TestCase):

    def test_if_else(self):
        self.assertEqual(control_flow.if_else(10), "10 is even")
        self.assertEqual(control_flow.if_else(9), "9 is odd")

    def test_for_loop(self):
        self.assertEqual(control_flow.for_loop([1, 2, 3, 4, 5]), 15)

    def test_while_loop(self):
        self.assertEqual(control_flow.while_loop(5), 15)

    def test_error_handling(self):
        self.assertEqual(control_flow.error_handling("10"), 10)
        self.assertRaises(ValueError, control_flow.error_handling, "ten")

if __name__ == '__main__':
    unittest.main()