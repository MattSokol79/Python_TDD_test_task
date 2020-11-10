# This is the test file

# Import all the relevant files and modulues required for testing
from tdd_task import Modulus_Calc
import unittest
import pytest # always pip install pytest beforehand

# Create the class to write tests
# unittest.TestCase works with unittest framework as a parent class
class Calctest(unittest.TestCase):

    # Creating an object of the class
    calc = Modulus_Calc()

    # Tests the modulus method in parent
    def test_modulus(self):
        self.assertEqual(self.calc.modulus(4, 2), 0) # Bool - True
        # Test if 4 % 2 == 0, if True, pass test, if False fail the test

    # Tests the non_zero method in parent
    def test_not_zero(self):
        self.assertEqual(self.calc.not_zero(4, 2), True) # Bool - True
        # Test if the input i.e. 4, 2 > 0, if True, pass test, False fail