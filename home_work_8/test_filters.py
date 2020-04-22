import requests
import pytest


def test_read_book_id(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?book_id=' + str(roles_for_filter[0]['book']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['book'] == roles_for_filter[0]['book']]
    assert read == read_filter.json()


def test_read_type(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?type=' + str(roles_for_filter[0]['type']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['type'] == roles_for_filter[0]['type']]
    assert read == read_filter.json()


def test_read_level(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?level=' + str(roles_for_filter[1]['level']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['level'] == roles_for_filter[1]['level']]
    assert read == read_filter.json()


def test_read_level_lt(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?level__lt=' + str(roles_for_filter[1]['level']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['level'] < roles_for_filter[1]['level']]
    assert read == read_filter.json()


def test_read_level_lte(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?level__lte=' + str(roles_for_filter[1]['level']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['level'] <= roles_for_filter[1]['level']]
    assert read == read_filter.json()


def test_read_level_gt(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?level__gt=' + str(roles_for_filter[1]['level']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['level'] > roles_for_filter[1]['level']]
    assert read == read_filter.json()


def test_read_level_gte(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(base_role_url + '?level__gte=' + str(roles_for_filter[1]['level']))
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if role['level'] >= roles_for_filter[1]['level']]
    assert read == read_filter.json()


def test_read_level_combo(roles_for_filter, base_role_url, auth_session):
    for role in roles_for_filter:
        r = auth_session.post(base_role_url, data=role)
        role['id'] = r.json()['id']
    read_filter = auth_session.get(f'{base_role_url}?level__gte={str(roles_for_filter[1]["level"])}'
                                   f'&level__lte={str(roles_for_filter[0]["level"])}'
                                   f'&type={str(roles_for_filter[0]["type"])}')
    roles_list = auth_session.get(base_role_url).json()
    read = [role for role in roles_list if
            roles_for_filter[1]['level'] <= role['level'] <= roles_for_filter[0]['level']
            and role['type'] == roles_for_filter[0]['type']]
    assert read == read_filter.json()
