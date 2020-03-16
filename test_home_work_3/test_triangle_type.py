import unittest
from HomeWork_3_6 import TriangleType


class TestTriangleType(unittest.TestCase):

    def test_not_triangle(self):
        result = TriangleType(1, 0, 2)
        self.assertEqual(result, 'Not a triangle')
        self.assertNotEqual(result, 'Equilateral triangle')
        self.assertNotEqual(result, 'Versatile triangle')
        self.assertNotEqual(result, 'Isosceles triangle')


    def test_triangle_type1(self):
        result = TriangleType(3, 3, 3)
        self.assertEqual(result, 'Equilateral triangle')
        self.assertNotEqual(result, 'Not a triangle')
        self.assertNotEqual(result, 'Versatile triangle')
        self.assertNotEqual(result, 'Isosceles triangle')

    def test_triangle_type2_1(self):
        result = TriangleType(6, 4, 4)
        self.assertEqual(result, 'Isosceles triangle')

    def test_triangle_type2_2(self):
        result = TriangleType(5, 7, 5)
        self.assertEqual(result, 'Isosceles triangle')
        self.assertNotEqual(result, 'Not a triangle')
        self.assertNotEqual(result, 'Equilateral triangle')
        self.assertNotEqual(result, 'Versatile triangle')

    def test_triangle_type2_3(self):
        result = TriangleType(6, 6, 11)
        self.assertEqual(result, 'Isosceles triangle')

    def test_triangle_type3(self):
        result = TriangleType(4, 5, 3)
        self.assertEqual(result, 'Versatile triangle')
        self.assertNotEqual(result, 'Not a triangle')
        self.assertNotEqual(result, 'Equilateral triangle')
        self.assertNotEqual(result, 'Isosceles triangle')


if __name__ == "__main__":
    unittest.main()