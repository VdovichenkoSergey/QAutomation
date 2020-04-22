import pytest
import requests

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


def test_book_no_auth_edit(post_book_with_auth, base_book_url, book_data_edit):
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
    assert role_data == read.json()


'''book auth with wrong credentials'''


def test_book_create_wrong_auth(base_book_url, wrong_auth_list, book_data):
    create = requests.post(base_book_url, data=book_data, auth=wrong_auth_list)
    assert create.status_code == 401
    assert create.json() == {'detail': 'Invalid username/password.'}


def test_book_read_wrong_auth(post_book_with_auth, base_book_url, wrong_auth_list):
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']), auth=wrong_auth_list)
    assert read.status_code == 401
    assert read.json() == {'detail': 'Invalid username/password.'}


#
#
def test_book_edit_wrong_auth(post_book_with_auth, base_book_url, wrong_auth_list, book_data_edit):
    edit = requests.put(base_book_url + str(post_book_with_auth.json()['id']), data=book_data_edit,
                        auth=wrong_auth_list)
    assert edit.status_code == 401
    assert edit.json() == {'detail': 'Invalid username/password.'}


def test_book_delete_wrong_auth(post_book_with_auth, base_book_url, book_data_edit, wrong_auth_list):
    delete = requests.delete(base_book_url + str(post_book_with_auth.json()['id']), auth=wrong_auth_list)
    assert delete.status_code == 401
    assert delete.json() == {'detail': 'Invalid username/password.'}
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']))
    assert read.status_code == 200
    assert read.json() == post_book_with_auth.json()


'''role auth with wrong credentials'''


def test_role_create_wrong_auth(base_role_url, role_data, wrong_auth_list):
    create = requests.post(base_role_url, data=role_data, auth=wrong_auth_list)
    assert create.status_code == 403
    assert create.json() == {'detail': 'Invalid username/password.'}


def test_role_read_wrong_auth(post_role, base_role_url, wrong_auth_list):
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=wrong_auth_list)
    assert read.status_code == 403
    assert read.json() == {'detail': 'Invalid username/password.'}


def test_role_edit_wrong_auth(post_role, base_role_url, role_data_edit, wrong_auth_list):
    edit = requests.put(base_role_url + str(post_role.json()['id']), data=role_data_edit, auth=wrong_auth_list)
    assert edit.status_code == 403
    assert edit.json() == {'detail': 'Invalid username/password.'}


def test_role_delete_wrong_auth(post_role, base_role_url, auth, role_data, wrong_auth_list):
    delete = requests.delete(base_role_url + str(post_role.json()['id']), auth=wrong_auth_list)
    assert delete.status_code == 403
    assert delete.json() == {'detail': 'Invalid username/password.'}
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth)
    assert read.status_code == 200
    assert read.json() == post_role.json()


'''Book auth with valid creds'''


def test_book_with_auth_create(base_book_url, book_data, auth):
    create = requests.post(base_book_url, data=book_data, auth=auth)
    assert create.status_code == 201


def test_book_with_auth_read(post_book_with_auth, base_book_url, auth):
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']), auth=auth)
    assert read.status_code == 200


def test_book_with_auth_edit(post_book_with_auth, base_book_url, book_data, book_data_edit, auth):
    edit = requests.put(base_book_url + str(post_book_with_auth.json()['id']), data=book_data_edit, auth=auth)
    assert edit.status_code == 200


def test_book_with_auth_delete(post_book_with_auth, base_book_url, auth):
    delete = requests.delete(base_book_url + str(post_book_with_auth.json()['id']), auth=auth)
    assert delete.status_code == 204
    read = requests.get(base_book_url + str(post_book_with_auth.json()['id']))
    assert read.status_code == 404


'''Roles auth with valid creds'''


def test_role_with_auth_create(base_role_url, role_data, auth):
    create = requests.post(base_role_url, data=role_data, auth=auth)
    assert create.status_code == 201


def test_role_with_auth_read(post_role, base_role_url, auth):
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth)
    assert read.status_code == 200


def test_role_with_auth_edit(post_role, base_role_url, role_data_edit, auth):
    edit = requests.put(base_role_url + str(post_role.json()['id']), data=role_data_edit, auth=auth)
    assert edit.status_code == 200


def test_role_with_auth_delete(post_role, base_role_url, auth, role_data):
    delete = requests.delete(base_role_url + str(post_role.json()['id']), auth=auth)
    assert delete.status_code == 204
    read = requests.get(base_role_url + str(post_role.json()['id']), auth=auth)
    assert read.status_code == 404


'''token validation'''


def test_token():
    r_token = requests.post('http://pulse-rest-testing.herokuapp.com/api-token-auth/',
                            data={'username': 'vdovichenko', 'password': 'vdovichenko'})

    token = r_token.json()['token']
    assert len(token) == 40


'''filters without auth'''


def test_book_id_no_auth(post_role, base_role_url, post_book_with_auth, auth):
    read = requests.get(base_role_url + '?book_id=' + str(post_role.json()['book']))
    assert read.status_code == 403
    assert read.json() == {'detail': 'Authentication credentials were not provided.'}


def test_type_no_auth(post_role, base_role_url, role_data_edit):
    edit = requests.put(base_role_url + '?type=' + str(post_role.json()['type']), data=role_data_edit)
    assert edit.status_code == 403
    assert edit.json() == {'detail': 'Authentication credentials were not provided.'}


def test_level_no_auth(post_role, base_role_url, auth, role_data):
    delete = requests.delete(base_role_url + '?level=' + str(post_role.json()['level']))
    assert delete.status_code == 403
    assert delete.json() == {'detail': 'Authentication credentials were not provided.'}