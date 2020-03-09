import unittest
from HomeWork_3_6 import triangle


class TestTriangle(unittest.TestCase):

    def triangle_true1(self):
        res = triangle(1, 2, 2)
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()