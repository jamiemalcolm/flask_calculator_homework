from modules.calculator import *

import unittest

class TestCalculatorFunctions(unittest.TestCase):
    
    def test_add_function_returns_10(self):
        returns_10 = add(5, 5)
        self.assertEqual(10, returns_10)