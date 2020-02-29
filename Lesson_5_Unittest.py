import unittest

from HomeWork_3_6 import is_year_leap

class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        year = 2000
        res = is_year_leap(year)
        self.assertTrue(res)

    def test_zero_year(self):
        year = 0
        res = is_year_leap(year)
        self.assertFalse(res)

unittest.main()