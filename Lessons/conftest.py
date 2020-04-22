import pytest
import requests


# с этого файла все фикстуры или глобальные переменные будут использоваться для всех моделей с этого пакета,
# но он должен лежать на верхнем уровне этого пакета
# фикстуры не нужно импортить, а переменные нужно

# @pytest.fixture
# def user():
#    fixture = user(name='Roman', age=30, '')
#    return fixture
#
# def test_user(user):
#    assert user.name == 'Roman

# @pytest.fixture()
# def book_data():
#     d = {
#         'title': '111',
#         'author': '0000'
#     }
#     # print('\nFixtue')
#     return d


@pytest.fixture(scope='module')
# module - запустится для всех тестов в этом файле
# class запустится для всех методов класса \
# session - запустится один раз для всех тестов в этом запуске
# autouse=True - будет запускаться для каждого теста
# def base_book_url():
#     return 'http://pulse-rest-testing.herokuapp.com/books/'


@pytest.fixture()
def post_book(base_book_url, book_data):
    new_book = requests.post(base_book_url, data=book_data)
    book = new_book.json()
    yield book  # используется вместо ретурн если нужен теарДаун
    # (yield возвращает book в тест, а потом с теста возвращает обратно и позволяет это подчистить)
    requests.delete(base_book_url + str(book['id']))


