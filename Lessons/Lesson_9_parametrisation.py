import pytest
import requests

book_list1 = [
    {'title': '123', 'author': '456'},
    {'title': 'qwe', 'author': 'rty'},
    {'title': '!@#$', 'author': '!@#$%$^'}
]


@pytest.fixture(scope='session', params=book_list1, ids=[str(i) for i in book_list1])
def books_list(request):
    book = request.param
    return book
