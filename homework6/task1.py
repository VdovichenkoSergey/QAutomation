# Тестовое приложение с REST API  http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
# •	Создаёт персонажа POST /roles/, вы запоминаете его id.
# •	Проверяете, что он создался и доступен по ссылке GET /roles/[id]
# •	Проверяете, что он есть в списке пользователей по GET /roles/
# •	Изменяете этого пользователя методом PUT roles/[id]/
# •	Проверяете, что он изменился и доступен по ссылке /roles/[id]
# •	Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
# •	Удаляете этого пользователя методом DELETE roles/[id]
# Второй скрипт: тоже самое с книгами
import requests
base_url = "http://pulse-rest-testing.herokuapp.com/"
new_role = {
    "name": "Nika",
    "type": "god",
    "level": 666,
    "book": None
}
role = requests.post(base_url+'roles/', data=new_role)
r_dict = role.json()
print(role.status_code, r_dict)
get_role = requests.get(f"{base_url}roles/{r_dict['id']}")
print(get_role.json())
new_role['id'] = r_dict['id']
get_roles = requests.get(base_url+'roles/', params=new_role)
print(get_roles.status_code, get_roles.url)
new_params = {
    "name": "Nika edited",
    "level": 10500,
    "type": "godness",
    "book": None
}
edit_role = requests.put(f"{base_url}roles/{r_dict['id']}", data=new_params)
print(edit_role.status_code, edit_role.json())
get_edited_role = requests.get(f"{base_url}roles/{r_dict['id']}")
print(get_edited_role.json())
new_params['id'] = r_dict['id']
get_edited_roles = requests.get(base_url+'roles/', params=new_params)
print(get_edited_roles.status_code, get_edited_roles.url)
delete_role = requests.delete(f"{base_url}roles/{r_dict['id']}")
print(requests.get(f"{base_url}roles/{r_dict['id']}"))
new_book = {
    "title": "Idiot",
    "author": "Dostoevsky"
}
book = requests.post(base_url+'books/', data=new_book)
b_dict = book.json()
print(book.status_code, b_dict)
new_book['id'] = b_dict['id']
get_book = requests.get(f"{base_url}books/{b_dict['id']}")
print(get_book.json())
get_books = requests.get(base_url+'books/', params=new_book)
print(get_books.status_code, get_books.url)
edited_book = {
    "title": "Idiot edited",
    "author": "No name"
}
edit_book = requests.put(f"{base_url}books/{b_dict['id']}", data=edited_book)
print(edit_book.status_code, edit_book.json())
get_edited_book = requests.get(f"{base_url}books/{b_dict['id']}")
print(get_edited_book.json())
edited_book['id'] = b_dict['id']
get_edited_books = requests.get(base_url+'books/', params=edited_book)
print(get_edited_books.status_code, get_edited_books.url)
delete_book = requests.delete(f"{base_url}books/{b_dict['id']}")
print(requests.get(f"{base_url}books/{b_dict['id']}"))
