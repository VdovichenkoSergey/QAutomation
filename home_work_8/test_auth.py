import pytest
import requests
from home_work_8.conftest import wrong_auth_list

'''book auth without credentials'''


def test_book_no_auth_create(base_book_url, book_data):
    create = requests.post(base_book_url, data=book_data)
    assert create.status_code == 401
    assert create.json() == {'detail': 'Authentication credentials were not provided.'}


def test_book_no_auth_read(post_book_with_auth, base_book_url, book_data):
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']))
    assert read.status_code == 200
    assert read.json()['author'] == book_data['author']
    assert read.json()['title'] == book_data['title']


def test_book_no_auth_edit(post_book_with_auth, base_book_url, book_data, book_data_edit):
    edit = requests.put(base_book_url + str(post_book_with_auth.json()['id']), data=book_data_edit)
    assert edit.status_code == 401
    assert edit.json() == {'detail': 'Authentication credentials were not provided.'}


def test_book_no_auth_delete(post_book_with_auth, base_book_url):
    delete = requests.delete(base_book_url + str(post_book_with_auth.json()['id']))
    assert delete.status_code == 401
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']))
    assert read.status_code == 200
    assert read.json() == post_book_with_auth.json()


'''role auth without credentials'''


def test_role_no_auth_create(base_role_url, role_data):
    create = requests.post(base_role_url, data=role_data)
    assert create.status_code == 403
    assert create.json() == {'detail': 'Authentication credentials were not provided.'}


def test_role_no_auth_read(post_role, base_role_url):
    read = requests.get(base_role_url + str(post_role.json()['id']))
    assert read.status_code == 403
    assert read.json() == {'detail': 'Authentication credentials were not provided.'}


def test_role_no_auth_edit(post_role, base_role_url, role_data_edit):
    edit = requests.put(base_role_url + str(post_role.json()['id']), data=role_data_edit)
    assert edit.status_code == 403
    assert edit.json() == {'detail': 'Authentication credentials were not provided.'}


def test_role_no_auth_delete(post_role, base_role_url, auth, role_data):
    delete = requests.delete(base_role_url + str(post_role.json()['id']))
    assert delete.status_code == 403
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth)
    assert read.status_code == 200
    role_data['id'] = post_role.json()['id']
    print(role_data)
    print(post_role.json())
    assert role_data == read.json()


'''book auth with wrong credentials'''

wa_list = [
    ('secret', 'tester'),
    ('tester', 'tester'),
    ('secret', 'secret'),
    ('tester1', 'secret'),
    ('tester', 'secret1')
]


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_book_create_wrong_auth(base_book_url, book_data, auth2):
    create = requests.post(base_book_url, data=book_data, auth=auth2)
    assert create.status_code == 401
    assert create.json() == {'detail': 'Invalid username/password.'}


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_book_read_wrong_auth(post_book_with_auth, base_book_url, book_data, auth2):
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']), auth=auth2)
    assert read.status_code == 401
    assert read.json() == {'detail': 'Invalid username/password.'}


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_book_edit_wrong_auth(post_book_with_auth, base_book_url, book_data, book_data_edit, auth2):
    edit = requests.put(base_book_url + str(post_book_with_auth.json()['id']), data=book_data_edit, auth=auth2)
    assert edit.status_code == 401
    assert edit.json() == {'detail': 'Invalid username/password.'}


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_book_delete_wrong_auth(post_book_with_auth, base_book_url, book_data, book_data_edit, auth2):
    delete = requests.delete(base_book_url + str(post_book_with_auth.json()['id']), auth=auth2)
    assert delete.status_code == 401
    assert delete.json() == {'detail': 'Invalid username/password.'}
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']))
    assert read.status_code == 200
    assert read.json() == post_book_with_auth.json()


'''role auth with wrong credentials'''


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_role_create_wrong_auth(base_role_url, role_data, auth2):
    create = requests.post(base_role_url, data=role_data, auth=auth2)
    assert create.status_code == 403
    assert create.json() == {'detail': 'Invalid username/password.'}


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_role_read_wrong_auth(post_role, base_role_url, auth2):
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth2)
    assert read.status_code == 403
    assert read.json() == {'detail': 'Invalid username/password.'}


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_role_edit_wrong_auth(post_role, base_role_url, role_data_edit, auth2):
    edit = requests.put(base_role_url + str(post_role.json()['id']), data=role_data_edit, auth=auth2)
    assert edit.status_code == 403
    assert edit.json() == {'detail': 'Invalid username/password.'}


@pytest.mark.parametrize('auth2', wa_list, ids=[str(i) for i in wa_list])
def test_role_delete_wrong_auth(post_role, base_role_url, auth, role_data, auth2):
    delete = requests.delete(base_role_url + str(post_role.json()['id']), auth=auth2)
    assert delete.status_code == 403
    assert delete.json() == {'detail': 'Invalid username/password.'}
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth)
    assert read.status_code == 200
    assert read.json() == post_role.json()
