import unittest


class TestClass(unittest.TestCase):

    def setUp(self):
        print('\nsetup of ', self)

    def tearDown(self):
        print('\nteardown of ', self)

    def test_1(self):
        print('- test_1()')

    def test_2(self):
        print('- test_2()')


if __name__ == "__main__":
    unittest.main()