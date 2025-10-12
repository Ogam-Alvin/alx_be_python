import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        """Test addition with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1000, 999), 1999)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """Test subtraction with positive, negative, and zero values."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(100, 200), -100)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """Test multiplication with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # --- Division Tests ---
    def test_division(self):
        """Test division with positive, negative, and zero values."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)  # float test

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_with_zero_numerator(self):
        """Test dividing zero by a number."""
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == '__main__':
    unittest.main()
