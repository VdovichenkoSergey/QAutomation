import unittest

from HomeWork_3_6 import triangle


class TestTriangle(unittest.TestCase):

    def triangle_true1(self):
        a = 1
        b = 2
        c = 2
        res = triangle(a, b, c)
        self.assertTrue(res)

    def triangle_false1(self):
        a = 1
        b = 0
        c = 2
        res = triangle(a, b, c)
        self.assertFalse(res)

    def triangle_false2(self):
        a = 5
        b = 3
        c = 2
        res = triangle(a, b, c)
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()