import requests
import json

url_books = 'http://pulse-rest-testing.herokuapp.com/books/'
new_book = {
    'title': 'Rest API learning',
    'author': 'Serhio Brugeiro'
}
book_changes = {
    'title': 'Changed Book',
    'author': 'Serhio Brugeiro II'
}

book1 = requests.post(url_books, data=new_book)
url_books_list = requests.get(url_books).json()
book1_json = book1.json()
book1_json_id = book1_json['id']

print(f'1.1:  Status code:   {book1.status_code}   and saved book ID:   {book1_json_id}')

get_book1 = requests.get(url_books + str(book1_json_id))
print(f'1.2: {get_book1.json()}')

for i in url_books_list:
    if i['id'] == book1_json_id and i['title'] == new_book['title'] and i['author'] == new_book['author']:
        print('1.3:', i)

book2 = requests.put(url_books + str(book1_json_id), data=book_changes)
get_book2 = requests.get(url_books + str(book1_json_id))
print(f'1.4: status code - {book2.status_code} new book parameters: {get_book2.json()}')

url_books_list2 = requests.get(url_books).json()
for i in url_books_list2:
    if i['id'] == book1_json_id and i['title'] == book_changes['title'] and i['author'] == book_changes['author']:
        print('1.5:', i)

deleted_book = requests.delete(url_books + str(book1_json_id))
print('1.6:', deleted_book.status_code)
