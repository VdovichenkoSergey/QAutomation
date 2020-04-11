import unittest
import sys

from HomeWork_3_6 import is_year_leap
from HomeWork_3_6 import triangle

from HtmlTestRunner import HTMLTestRunner


class TestLeapYear(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = {'name': "Sergey"}
        print('setup of: ', cls.user['name'], {cls})

    @classmethod
    def tearDownClass(cls):
        print('Finish')

    # @unittest.skipIf(sys.platform.startswith('win'), 'нужна MacOS')
    def test_leap_year1(self):
        years_list = [2001, 2004, 2012]
        for year in years_list:
            with self.subTest(year):
                self.assertTrue(is_year_leap(year))

    @unittest.skipUnless(sys.platform.startswith('win'), 'нужна Win')
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

    def test_negative(self):
        with self.assertRaises(ValueError):
            is_year_leap('a') # негативный сценарий, проверяет что при аргументе 'a' должен вернуться ValueError


test1 = TestLeapYear("test_leap_year1")
# print(test1.run())

test2 = TestLeapYear("test_leap_year2")

suite1 = unittest.TestSuite([test1, test2]) # сьют для запуска тестов test1, test2

result = unittest.TestResult()
suite1.run(result)
print(result)

# suite2 = unittest.TestLoader().loadTestsFromTestCase(TestLeapYear) # сьют для запуска всех тестов с класса TestLeapYear
# result2 = unittest.TestResult()
# suite2.run(result2)
# print(result2)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="./")) # verbosity - расширенный отчет,
    # testRunner вывести отчет в другом виде, output="./" - запись в файл

