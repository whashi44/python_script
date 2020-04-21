import unittest
import calc

# First create a class, and inherit from unittest
# And allow the capability
class TestCalc(unittest.TestCase):

    # represent which test to perform, we want to check if the add() function is working properly
    # all of the test needs to be named properly so that it starts with test_
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 14)
        self.assertEqual(calc.add(10, 5), 14)


if __name__ == "__main__":
    unittest.main()
