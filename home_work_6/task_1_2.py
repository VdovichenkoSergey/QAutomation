import requests
import json

'''This script will be delete old book (from previous run) and create new book'''

url_books = 'http://pulse-rest-testing.herokuapp.com/books/'
books_list = requests.get(url_books).json()

for i in books_list:
    if i['author'] == 'Serhio Brugeiro II':
        # print('deleted: ', i)
        requests.delete(url_books + str(i['id']))

book = {
    'title': 'The Greatest Showman',
    'author': 'Serhio Brugeiro II'
}

book_post = requests.post(url_books, data=book).json()
book_post_id = str(book_post['id'])

'''This script will be create new role for book which was created earlier and delete old role before it'''

url_roles = 'http://pulse-rest-testing.herokuapp.com/roles/'
roles_list = requests.get(url_roles).json()

for i in roles_list:
    if i['name'] == 'Antonio Pereiro':
        requests.delete(url_roles + str(i['id']))

new_role = {
    "name": "Antonio Pereiro",
    "type": "Seller",
    "level": 80,
    "book": url_books + book_post_id
}

role_post = requests.post(url_roles, data=new_role).json()
role_post_id = str(role_post['id'])

role_get = requests.get(url_roles + role_post_id)
print(f'status code: {role_get.status_code} | created role: {role_get.json()}')

roles_list = requests.get(url_roles).json()
for i in roles_list:
    if i['name'] == new_role['name']:
        print(i)

role_remark = {
    "name": "Antonio Pereiro II",
    "type": "Seller II",
    "level": 805,
    "book": url_books + book_post_id
}

role_changes = requests.put(url_roles + role_post_id, data=role_remark)
role_get = requests.get(url_roles + role_post_id)
print(f'status code: {role_get.status_code} | created role: {role_get.json()}')

roles_list = requests.get(url_roles).json()
for i in roles_list:
    if i['id'] == role_post['id'] and i['name'] == role_remark['name']:
        print(f'get role after changes: {i}')

for i in roles_list:
    if i['name'] == role_remark['name']:
        print(f'role removed: {i}')
        requests.delete(url_roles + str(i['id']))
