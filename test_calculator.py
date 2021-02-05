import unittest
import calculator

class TestCalculator(unittest.TestCase):

	def test_addition(self):
		result = calculator.addition(7, 3)
		self.assertEqual(result, 10)

	def test_subtraction(self):
		result = calculator.subtraction(4, 1)
		self.assertEqual(result, 3)

	def test_multiplication(self):
		result = calculator.multiplication(10, 13)
		self.assertEqual(result, 130)

	def test_division(self):
		result = calculator.division(6, 2)
		self.assertEqual(result, 3)

if __name__ == "__main__":
	unittest.main()
