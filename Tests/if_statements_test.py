import unittest
from even_odd import even_or_odd
from bonus import bonus_math


class MyTestCase(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual("11 is an odd number", even_or_odd(11))
        self.assertEqual("24 is an even number", even_or_odd(24))

    # In the space below, write a test function for bonus. Make sure to import the appropriate information
    # at the top of this file. Make sure to write three test cases.
    def test_bonus(self):
        # when you are ready to write your tests, go ahead and delete pass
        self.assertEqual(50000.0, bonus_math(50000,4))
        self.assertEqual(52500.0,bonus_math(50000,6))



if __name__ == '__main__':
    unittest.main()
