import pytest
import requests


def test_book_create(base_book_url, book_list, auth_session):  # parametrization
    create = auth_session.post(base_book_url, data=book_list)
    assert create.status_code == 201
    book_list['id'] = create.json()['id']
    assert book_list == create.json()


def test_book_read(post_book_with_auth, base_book_url, book_data, auth):
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']), auth=auth)
    assert read.status_code == 200
    book_data['id'] = read.json()['id']
    assert book_data == read.json()


def test_book_edit(post_book_with_auth, base_book_url, book_data_edit, auth):
    edit = requests.put(base_book_url + str(post_book_with_auth.json()['id']), data=book_data_edit, auth=auth)
    assert edit.status_code == 200
    book_data_edit['id'] = post_book_with_auth.json()['id']
    assert book_data_edit == edit.json()


def test_book_delete(post_book_with_auth, base_book_url, book_data, auth):
    book_data['id'] = post_book_with_auth.json()['id']
    delete = requests.delete(base_book_url + str(post_book_with_auth.json()['id']), auth=auth)
    assert delete.status_code == 204
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']))
    assert read.status_code == 404
    books_list = requests.get(base_book_url).json()
    assert book_data not in books_list
    print(books_list)
    print(book_data)
