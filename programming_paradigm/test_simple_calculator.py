import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before every test."""
        self.calc = SimpleCalculator()

    # -------------------------------
    # Tests for addition
    # -------------------------------
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    # -------------------------------
    # Tests for subtraction
    # -------------------------------
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # -------------------------------
    # Tests for multiplication
    # -------------------------------
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 6), -12)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    # -------------------------------
    # Tests for division
    # -------------------------------
    def test_division(self):
        # normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

        # edge cases
        self.assertIsNone(self.calc.divide(5, 0))  # divide by zero
        self.assertEqual(self.calc.divide(0, 5), 0)  # zero numerator

    # -----------------------------------------------------
    # Extra: check division with negative numbers
    # -----------------------------------------------------
    def test_division_negatives(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)


if __name__ == "__main__":
    unittest.main()
