import unittest
from Lesson_5_Distance import Distance


class DistanceTests(unittest.TestCase):

    def test_default_values(self):
        res = Distance().dist()
        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()