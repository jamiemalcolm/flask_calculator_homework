from modules.calculator import *

import unittest

class TestCalculatorFunctions(unittest.TestCase):
    
    def test_add_function_returns_10(self):
        returns_10 = add(5, 5)
        self.assertEqual(10, returns_10)
    
    def test_add_returns_6000(self):
        returns_6000 = add(4031, 1969)
        self.assertEqual(6000, returns_6000)

    def test_subtract_returns_6(self):
        returns_6 = subtract(10, 4)
        self.assertEqual(6, returns_6)

    def test_divide_returns_2(self):
        returns_2 = divide(10, 5)
        self.assertEqual(2, returns_2)

    def test_multiply_returns_50(self):
        returns_50 = multiply(25, 2)
        self.assertEqual(50, returns_50)

    def test_squared_returns_4(self):
        returns_4 = squared(2)
        self.assertEqual(4, returns_4)

    def test_squared_returns_289(self):
        returns_289 = squared(17)
        self.assertEqual(289, returns_289)