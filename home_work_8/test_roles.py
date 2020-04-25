import pytest
import requests


def test_role_create(base_role_url, role_list, auth):
    create = requests.post(base_role_url, data=role_list, auth=auth)
    assert create.status_code == 201
    role_list['id'] = create.json()['id']
    assert role_list == create.json()


def test_role_create_negative(base_role_url, role_list_negative, auth_session):
    create = auth_session.post(base_role_url, data=role_list_negative)
    assert create.status_code == 400
    role_list = auth_session.get(base_role_url).json()
    for role in role_list:
        role.pop('id')
    assert role_list_negative not in role_list


def test_role_read(post_role, base_role_url, role_data, auth):
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth)
    assert read.status_code == 200
    role_data['id'] = read.json()['id']
    assert role_data == read.json()


def test_role_edit(post_role, base_role_url, role_data_edit, auth):
    edit = requests.put(base_role_url + str(post_role.json()['id']), data=role_data_edit, auth=auth)
    assert edit.status_code == 200
    role_data_edit['id'] = edit.json()['id']
    role_data_edit['book'] = edit.json()['book']
    assert role_data_edit == edit.json()


def test_role_delete(post_role, base_role_url, role_data, auth_session):
    role_data['id'] = post_role.json()['id']
    delete = auth_session.delete(base_role_url + str(post_role.json()['id']))
    assert delete.status_code == 204
    read = auth_session.get(base_role_url + str(post_role.json()['id']))
    assert read.status_code == 404
    roles_list2 = auth_session.get(base_role_url).json()
    assert role_data not in roles_list2


def test_linked_book_from_deleted_role(post_role, base_role_url, base_book_url, book_data, auth_session):
    book = post_role.json()['book']
    book = book[-4:]
    book_json = auth_session.get(base_book_url + book).json()
    auth_session.delete(base_role_url + str(post_role.json()['id']))
    books_json = auth_session.get(base_book_url).json()

    assert book_json in books_json
