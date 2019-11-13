"""import module"""
import unittest
import calc_arithmetic



class Test(unittest.TestCase):
    """main class of the program"""

    def test_addition(self):
        """calculating the positive addition value"""
        self.assertEqual(calc_arithmetic.addition(2, 3), 5)

    def test_subtraction(self):
        """calculating the subtraction value"""
        self.assertEqual(calc_arithmetic.subtraction(5, 3), 2)

    def test_multipy(self):
        """calculating the multiplication """
        self.assertEqual(calc_arithmetic.multiply(5, 3), 15)
    def test_divide(self):
        """calculating the divition"""
        self.assertEqual(calc_arithmetic.divide(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
