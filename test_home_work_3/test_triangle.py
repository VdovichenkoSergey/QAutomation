import unittest
from HomeWork_3_6 import triangle


class TestTriangle(unittest.TestCase):

    def triangle_true1(self):
        a = 1
        b = 2
        c = 2
        res = triangle(a, b, c)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()