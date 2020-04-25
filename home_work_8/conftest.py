import pytest
import requests
import json

'''auth start'''


@pytest.fixture()
def token():
    r_token = requests.post('http://pulse-rest-testing.herokuapp.com/api-token-auth/',
                            data={'username': 'vdovichenko', 'password': 'vdovichenko'})

    token = r_token.json()['token']
    return token


@pytest.fixture()
def auth():
    return 'vdovichenko', 'vdovichenko'


wa_list = [
    ('secret', 'tester'),
    ('tester', 'tester'),
    ('secret', 'secret'),
    ('tester1', 'secret'),
    ('tester', 'secret1')
]


@pytest.fixture(params=wa_list, ids=[str(i) for i in wa_list])
def wrong_auth_list(request):
    wa = request.param
    return wa


@pytest.fixture()
def auth_session(auth):
    s = requests.Session()
    s.auth = auth
    return s


'''auth end'''
'''links start'''


@pytest.fixture()
def base_url():
    return 'http://pulse-rest-testing.herokuapp.com/'


@pytest.fixture()
def base_book_url(base_url):
    return base_url + 'books2/'


@pytest.fixture()
def base_role_url(base_url):
    return base_url + 'roles2/'


'''links end'''
'''data start'''


@pytest.fixture()
def book_data(base_book_url):
    book_data1 = {
        'title': 'Winnie',
        'author': 'A. A. Milne'
    }
    yield book_data1
    if 'id' in book_data1:
        requests.delete(base_book_url + str(book_data1['id']))


@pytest.fixture()
def book_data_edit():
    book_data2 = {
        'title': 'Winnie II',
        'author': 'A. A. Milne II'
    }
    return book_data2


with open('../home_work_8/books_list.txt', 'r') as output:
    book_list1 = json.loads(str(output.read()))
output.close()


@pytest.fixture(params=book_list1, ids=[str(i) for i in book_list1])  # parametrization
def book_list(request, base_book_url, auth):
    book = request.param
    yield book
    if 'id' in book:
        requests.delete(base_book_url + str(book['id']), auth=auth)


@pytest.fixture()
def role_data(post_book_with_auth, base_role_url, auth):
    role_data1 = {
        "name": "Sergey Vdovichenko",
        "type": "Shcoder",
        "level": 80,
        "book": post_book_with_auth.json()['id']
    }
    yield role_data1
    if 'id' in role_data1:
        requests.delete(base_role_url + str(role_data1['id']), auth=auth)


@pytest.fixture()
def role_data_edit(base_role_url, post_book_with_auth, auth):
    role_data2 = {
        "name": "Sergey II",
        "type": "Shcoder II",
        "level": 455,
        "book": post_book_with_auth.json()['id']
    }
    yield role_data2
    if 'id' in role_data2:
        requests.delete(base_role_url + str(role_data2['id']), auth=auth)


with open('../home_work_8/roles_list.txt', 'r') as output:
    roles_list = json.loads(str(output.read()))
output.close()


@pytest.fixture(params=roles_list, ids=[str(i) for i in roles_list])  # parametrization
def role_list(request, base_role_url, auth):
    role = request.param
    yield role
    if 'id' in role:
        requests.delete(base_role_url + str(role['id']), auth=auth)


with open('../home_work_8/roles_list_negative.txt', 'r') as output:
    roles_list_negative = json.loads(str(output.read()))
output.close()


@pytest.fixture(params=roles_list_negative, ids=[str(i) for i in roles_list_negative])  # parametrization
def role_list_negative(request, base_role_url, auth):
    role = request.param
    yield role
    if 'id' in role:
        requests.delete(base_role_url + str(role['id']), auth=auth)


@pytest.fixture()
def roles_for_filter(post_book_with_aut_2, base_book_url, base_role_url, auth_session):
    list_filter = [
        {"name": "Vdovichenko 2", "type": "Shcoder II", "level": 567,
         "book": post_book_with_aut_2.json()['id']},
        {"name": "Vdovichenko 2", "type": "Shcoder II", "level": 115,
         "book": post_book_with_aut_2.json()['id']},
        {"name": "Vdovichenko 2", "type": "Dude", "level": 115,
         "book": post_book_with_aut_2.json()['id']},
        {"name": "Vdovichenko 2", "type": "Dude", "level": 80,
         "book": post_book_with_aut_2.json()['id']}
    ]
    yield list_filter
    for role in list_filter:
        if 'id' in role:
            auth_session.delete(base_role_url + str(role['id']))


'''data end'''
'''actions start'''


@pytest.fixture()
def post_book_with_auth(base_book_url, book_data, token):
    p_book1 = requests.post(base_book_url, data=book_data, headers={'Authorization': f'Token {token}'})
    p_book_json1 = p_book1.json()
    yield p_book1
    if 'id' in p_book_json1:
        requests.delete(base_book_url + str(p_book_json1['id']), headers={'Authorization': f'Token {token}'})


@pytest.fixture()
def post_role(base_role_url, role_data, auth):
    p_role = requests.post(base_role_url, data=role_data, auth=auth)
    p_role_json = p_role.json()
    yield p_role
    if 'id' in p_role_json:
        requests.delete(base_role_url + str(p_role_json['id']), auth=auth)


@pytest.fixture()
def post_book_with_aut_2(base_book_url, book_data, auth):
    p_book1 = requests.post(base_book_url, data=book_data, auth=auth)
    p_book_json1 = p_book1.json()
    yield p_book1
    if 'id' in p_book_json1:
        requests.delete(base_book_url + str(p_book_json1['id']), auth=auth)


'''actions end'''



