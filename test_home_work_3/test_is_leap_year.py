import unittest
from HomeWork_3_6 import is_year_leap
from HomeWork_3_6 import triangle


class TestLeapYear(unittest.TestCase):

    def test_leap_year1(self):
        year = 2000
        res = is_year_leap(year)
        self.assertTrue(res)

    def test_leap_year2(self):
        year = 996
        res = is_year_leap(year)
        self.assertTrue(res)

    def test_notleap_year(self):
        year = 1900
        res = is_year_leap(year)
        self.assertFalse(res)

    def test_zero_year(self):
        year = 0
        res = is_year_leap(year)
        self.assertFalse(res)


# class TestTriangle(unittest.TestCase):
    def triangle_true1(self):
        a = 1
        b = 2
        c = 2
        res = triangle(a, b, c)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()