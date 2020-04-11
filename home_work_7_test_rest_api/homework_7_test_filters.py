import unittest
import requests
from HtmlTestRunner import HTMLTestRunner


class TestFilters(unittest.TestCase):

    def setUp(self):
        self.url_roles = 'http://pulse-rest-testing.herokuapp.com/roles/'
        self.book_id = '?book_id='
        self.type = '?type='
        self.level = '?level='
        self.level_lt = '?level__lt='
        self.level_lte = '?level__lte='
        self.level_gt = '?level__gt='
        self.level_gte = '?level__gte='

        self.book = {
            "id": 1560,
            "title": "Winnie Remarks II",
            "author": "A. A. Milne II"
        }

        self.role_1 = {
            "id": 426,
            "name": "Vdovichenko 2",
            "type": "Shcoder II",
            "level": 567,
            "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
        }

        self.role_2 = {
            "id": 427,
            "name": "Vdovichenko 2",
            "type": "Shcoder II",
            "level": 115,
            "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
        }

        self.role_3 = {
            "id": 428,
            "name": "Vdovichenko 2",
            "type": "Dude",
            "level": 115,
            "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
        }

        self.role_4 = {
            "id": 429,
            "name": "Vdovichenko 2",
            "type": "Dude",
            "level": 80,
            "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
        }

    def test_book_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        book_1560 = [role for role in roles_list_json if role['book'] == 'http://pulse-rest-testing.herokuapp.com/books/1560']
        books = requests.get(self.url_roles + self.book_id + '1560')
        check_list = [(books.status_code, 200), (book_1560, books.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_type_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        type_dude = [role for role in roles_list_json if role['type'] == 'Dude']
        types = requests.get(self.url_roles + self.type + 'Dude')
        check_list = [(types.status_code, 200), (type_dude, types.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_level_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        level_115 = [role for role in roles_list_json if role['level'] == 115]
        level = requests.get(self.url_roles + self.level + '115')

        check_list = [(level.status_code, 200), (level_115, level.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_level_lt_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        level_lt1 = [role for role in roles_list_json if role['level'] < 115]
        level_lt2 = requests.get(self.url_roles + self.level_lt + '115')

        check_list = [(level_lt2.status_code, 200), (len(level_lt1), len(level_lt2.json())), (level_lt1, level_lt2.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_level_lte_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        level_lte1 = [role for role in roles_list_json if role['level'] <= 115]
        level_lte2 = requests.get(self.url_roles + self.level_lte + '115')

        check_list = [(level_lte2.status_code, 200), (len(level_lte1), len(level_lte2.json())), (level_lte1, level_lte2.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_level_gt_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        level_gt1 = [role for role in roles_list_json if role['level'] > 115]
        level_gt2 = requests.get(self.url_roles + self.level_gt + '115')

        check_list = [(level_gt2.status_code, 200), (len(level_gt1), len(level_gt2.json())), (level_gt1, level_gt2.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_level_gte_filter(self):
        roles_list_json = requests.get(self.url_roles).json()
        level_gte1 = [role for role in roles_list_json if role['level'] >= 115]
        level_gte2 = requests.get(self.url_roles + self.level_gte + '115')

        check_list = [(level_gte2.status_code, 200), (len(level_gte1), len(level_gte2.json())), (level_gte1, level_gte2.json())]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_combo_lt_gt(self):
        roles_list_json = requests.get(self.url_roles).json()
        level_lt_gt1 = [role for role in roles_list_json if role['level'] in range(81, 115)] #> 80 and role['level'] < 115]
        level_lt_gt2 = requests.get(self.url_roles + self.level_gt + '80' + '&level__lt=115')

        check_list = [
            (level_lt_gt2.status_code, 200),
            (len(level_lt_gt1), len(level_lt_gt2.json())),
            (level_lt_gt1, level_lt_gt2.json())
        ]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_combo_lte_gte(self):
        roles_list_json = requests.get(self.url_roles).json()
        combo1 = [
            role for role in roles_list_json
            if role['level'] in range(80, 568) and role['type'] == 'Shcoder II'
            and role['book'] == 'http://pulse-rest-testing.herokuapp.com/books/1560'
        ]
        combo2 = requests.get(self.url_roles +
                                self.level_gte + '80' +
                                '&level__lte=567' +
                                '&type=Shcoder II' +
                                '&book_id=1560')

        check_list = [
            (combo2.status_code, 200),
            (len(combo1), len(combo2.json())),
            (combo1, combo2.json())
        ]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)


if __name__ == "__main__":
    unittest.main()  # verbosity=2, testRunner=HTMLTestRunner(output="./")