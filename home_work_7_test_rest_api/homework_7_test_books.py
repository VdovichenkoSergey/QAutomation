import unittest
import requests
from HtmlTestRunner import HTMLTestRunner


class TestBooks(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {
            'title': 'Winnie-The-Pooh and All, All, All',
            'author': 'A. A. Milne'
        }
        self.new_book = requests.post(self.base_url + 'books/', data=self.book)
        self.new_book_json = self.new_book.json()
        self.book['id'] = self.new_book_json['id']
        self.book_id = str(self.new_book_json['id'])
        self.read = requests.get(self.base_url + 'books/' + self.book_id)
        self.book_edit = {
            'title': 'II Winnie II',
            'author': 'II A. A. Milne II'
        }

    def test_create_book_status(self):
        self.assertEqual(self.new_book.status_code, 201)

    def test_create_book_id(self):
        self.assertIn('id', self.new_book_json.keys())

    def test_create_book_body(self):
        self.assertEqual(self.new_book_json, self.book)

    def test_read_book_status(self):
        self.assertEqual(self.read.status_code, 200)

    def test_read_book_body(self):
        read_json = self.read.json()
        self.assertEqual(read_json, self.book)

    def test_edit_book(self):
        new_book_edit = requests.put(self.base_url + 'books/' + self.book_id, data=self.book_edit)
        edit_json = new_book_edit.json()
        self.book_edit['id'] = edit_json['id']
        test_list = [(new_book_edit.status_code, 200), (sorted(edit_json), sorted(self.book_edit))]
        for test in test_list:
            with self.subTest(test):
                self.assertEqual(test[0], test[1])

    def test_delete_book(self):
        book_json = requests.get(self.base_url + 'books/' + self.book_id).json()
        book_delete = requests.delete(self.base_url + 'books/' + self.book_id)
        book_get = requests.get(self.base_url + 'books/' + self.book_id)
        book_list_json = requests.get(self.base_url + 'books/').json()
        list_id = [i['id'] for i in book_list_json]
        self.assertEqual(book_delete.status_code, 204)
        self.assertEqual(book_get.status_code, 404)
        self.assertNotIn(book_json, book_list_json)
        self.assertNotIn(book_json['id'], list_id)

    def tearDown(self):
        url_books = 'http://pulse-rest-testing.herokuapp.com/books/'
        books_list = requests.get(url_books).json()

        for book in books_list:
            if book['title'] == 'Winnie-The-Pooh and All, All, All' or book['title'] == 'II Winnie II':
                requests.delete(url_books + str(book['id']))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="./"))