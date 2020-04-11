import unittest
import requests
from HtmlTestRunner import HTMLTestRunner


class TestRoles(unittest.TestCase):

    def setUp(self):
        self.precondition_book = {
            'title': 'Winnie',
            'author': 'A. A. Milne'
        }
        self.book_url = 'http://pulse-rest-testing.herokuapp.com/books/'
        self.posted_book = requests.post(self.book_url, data=self.precondition_book)
        self.posted_book_json = self.posted_book.json()
        self.precondition_book['id'] = self.posted_book_json['id']
        self.book_id = str(self.posted_book_json['id'])
        self.base_url_roles = 'http://pulse-rest-testing.herokuapp.com/roles/'
        self.new_role_1 = {
            "name": "Sergey Vdovichenko",
            "type": "Shcoder",
            "level": 80,
            "book": "http://pulse-rest-testing.herokuapp.com/books/" + self.book_id
        }
        self.role_1 = requests.post(self.base_url_roles, data=self.new_role_1)
        self.role_1_json = self.role_1.json()
        self.new_role_1['id'] = self.role_1_json['id']

    def test_create_role_status(self):
        self.assertEqual(self.role_1.status_code, 201)

    def test_create_role_id(self):
        self.assertIn('id', self.role_1_json.keys())

    def test_create_role_body(self):
        self.assertEqual(self.new_role_1, self.role_1_json)

    def test_read_role(self):
        r_role = requests.get(self.base_url_roles + str(self.role_1_json['id']))
        r_role_json = r_role.json()
        check_list = [(r_role.status_code, 200), (self.new_role_1, r_role_json)]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_edit_role(self):
        role_changes = {
            "name": "Vdovichenko 2",
            "type": "Shcoder II",
            "level": 115,
            "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
        }
        role_edit = requests.put(self.base_url_roles + str(self.role_1_json['id']), data=role_changes)
        role_edit_json = role_edit.json()
        role_changes['id'] = role_edit_json['id']

        edit_check_list = [(role_edit.status_code, 200), (role_changes, role_edit_json), (self.new_role_1['id'], role_edit_json['id'])]
        for check in edit_check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_edit_level_negative(self):
        role_list = [
            {
                    "name": "Vdovichenko 2",
                    "type": "Shcoder II",
                    "level": 2147483648,
                    "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
                },
            {
                    "name": "Vdovichenko 2",
                    "type": "Shcoder II",
                    "level": -2147483649,
                    "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
                },
            {
                    "name": "Vdovichenko 2",
                    "type": "Shcoder II",
                    "level": '115',
                    "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
                },
            {
                    "name": "Vdovichenko 2",
                    "type": "Shcoder II",
                    "level": 'qwe',
                    "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
            }
        ]
        for role in role_list:
            role_edit = requests.put(self.base_url_roles + str(self.role_1_json['id']), data=role)
            with self.subTest(role):
                self.assertEqual(role_edit.status_code, 400)

    def test_edit_level(self):
        role_list = [
            {
                "name": "Vdovichenko 2",
                "type": "Shcoder II",
                "level": 2147483647,
                "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
            },
            {
                "name": "Vdovichenko 2",
                "type": "Shcoder II",
                "level": -2147483648,
                "book": "http://pulse-rest-testing.herokuapp.com/books/1560"
            },
        ]
        for role in role_list:
            role_edit = requests.put(self.base_url_roles + str(self.role_1_json['id']), data=role)
            role['id'] = role_edit.json()['id']
            with self.subTest(role):
                self.assertEqual(role_edit.status_code, 200)
                self.assertEqual(role, role_edit.json())

    def test_delete_role_status(self):
        role_delete = requests.delete(self.base_url_roles + str(self.role_1_json['id']))
        role_get = requests.get(self.base_url_roles + str(self.role_1_json['id']))
        book_get = requests.get(self.book_url + self.book_id)
        check_list = [(role_delete.status_code, 204), (role_get.status_code, 404), (book_get.status_code, 200)]
        for check in check_list:
            with self.subTest(check):
                self.assertEqual(*check)

    def test_delete_role_body(self):
        role_delete = requests.delete(self.base_url_roles + str(self.role_1_json['id']))
        role_get = requests.get(self.base_url_roles + str(self.role_1_json['id']))
        role_list_json = requests.get(self.base_url_roles).json()
        roles_id = [i['id'] for i in role_list_json]
        check_list = [(self.role_1_json, role_list_json), (self.role_1_json['id'], roles_id)]
        for check in check_list:
            with self.subTest(check):
                self.assertNotIn(*check)

    def test_linked_book_after_role_deleted(self):
        role_delete = requests.delete(self.base_url_roles + str(self.role_1_json['id']))
        book_get = requests.get(self.book_url + self.book_id)
        book_get_json = book_get.json()
        self.assertEqual(book_get.status_code, 200)
        self.assertEqual(book_get_json, self.posted_book_json)

    def tearDown(self):
        url_books = 'http://pulse-rest-testing.herokuapp.com/books/'
        books_list = requests.get(url_books).json()

        for book in books_list:
            if book['title'] == 'Winnie':
                requests.delete(url_books + str(book['id']))

        url_roles = 'http://pulse-rest-testing.herokuapp.com/roles/'
        roles_list = requests.get(url_roles).json()

        for role in roles_list:
            if role['name'] == 'Sergey Vdovichenko' or role['name'] == 'Vdovichenko 2':
                requests.delete(url_roles + str(role['id']))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="./"))