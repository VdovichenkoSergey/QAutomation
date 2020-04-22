import pytest
import requests
import sys


def test_1(book_data, base_book_url):
    print(book_data)
    assert type(book_data) == dict


def test_2(base_book_url):
    # print(book_data)
    print(base_book_url)
    print('test_2')


def test_3(book_data, post_book):
    book_data['id'] = post_book['id']
    assert book_data == post_book, "это сообщение будет показано при ране теста"


def test_4():
    with pytest.raises(ZeroDivisionError):
        res = 1 / 0


@pytest.mark.skip(reason='always will be skipped')
def test_5():
    with pytest.raises(ZeroDivisionError):
        res = 1 / 0


@pytest.mark.skipif(sys.platform.startswith('win'), reason='not for Windows')
def test_6():
    with pytest.raises(ZeroDivisionError):
        res = 1 / 0


@pytest.mark.xfail()  # не выведет в отчет зафейленный тест, но запустит, если перестанет фейлиться
# то выведет в отчет "XPASS". Удобно применять если бага еще не пофикшена, но ранить надо
# (run=False) - при наличии такого аргумента тест не будет запускаться
def test_7():
    with pytest.raises(ZeroDivisionError):
        res = 1 / 1


data_list = [
    {'title': '111', 'author': '0000'},
    {'title': 'qweqr', 'author': 'qwerw'},
    {'title': 'qwe !@#', 'author': 'qwr !@#$'}
]


@pytest.mark.parametrize('data', data_list, ids=[str(i) for i in data_list])
def test_create_book(base_book_url, data):
    r = requests.post(base_book_url, data=data)
    assert r.status_code == 201
    r_body = r.json()
    data['id'] = r_body['id']
    assert r_body == data
