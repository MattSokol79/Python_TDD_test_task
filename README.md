# TDD Task
- Create a test that checks whether the number 
divided by another number has a remainder of 0 
i.e. --> num % num2 == 0
- Create a class and method to write code to pass
- Create a test to check if the given values are 
positive i.e. --> if input -1 => FAIL, if input > 0 => PASS
- Create a method in the class to pass the test

### First create Test file
- Should have all the test conditions under the 
class methods
- So create the class which will test the functions
```python
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
        self.assertEqual(self.calc.modulus(4, 2), True) # Bool - True
        # Test if 4 % 2 == 0, if True, pass test, if False fail the test

    # Tests the non_zero method in parent
    def test_not_zero(self):
        self.assertEqual(self.calc.not_zero(4, 2), True) # Bool - True
        # Test if the input i.e. 4, 2 > 0, if True, pass test, False fail
```

### Create the code class to pass tests
- Create code which is expected to pass tests,
if it doesnt pass, refactor code:

```python
# This is the code file

# Creating the code class for the modulus/non_zero task
class Modulus_Calc:

    # Function that outputs True if no remainder when value1 % value2 i.e == 0
    def modulus(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    # Function that outputs True if both values are > 0, False if < 0
    def not_zero(self, value1, value2):
        if value1 and value2 > 0:
            return True
        else:
            return False
```

### To run Tests:
- In terminal `python -m pytest`
- For more detail `python -m pytest -v`
- Another way `python -m unittest -v`