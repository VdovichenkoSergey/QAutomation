import requests
import unittest


class TestCreateBooks(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'

    def tearDown(self):
        if hasattr():
            self.book_id

    def test_create_book(self):
        book_data = {
            'title': 'Star Wars',
            'author': 'Lukas'
        }
        r = requests.post(self.base_url+'books/', data=book_data)
        self.assertEqual(r.status_code, 201)
        r_body = r.json()
        self.assertIn('id', r_body.keys())

        print(book_data)

        # solution 3: remove id from r_body
        self.book_id = r_body.pop('id')
        self.assertEqual(book_data, r_body)


        # solutoin 1:
        # for key in book_data:
        #     self.assertEqual(book_data[key], r_body[key])

        # solution 2: add id to book_data
        # book_data['id'] = r_body['id']
        # print(book_data)
        # self.assertEqual(book_data, r_body)


if __name__ == "__main__":
    unittest.main()