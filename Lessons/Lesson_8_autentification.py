import requests

r_token = requests.post('http://pulse-rest-testing.herokuapp.com/api-token-auth/',
                        data={'username': 'admin', 'password': 'pass'})

token = r_token.json()['token']
#
#
# r = requests.post('http://pulse-rest-testing.herokuapp.com/books2/',
#                   data={'title': 'Anna Karenina', 'author': '111'},
#                   # headers={'Authorization': f'Token {token}'},
#                   auth=('admin', 'pass'))
# print(r.status_code)
# print(r.json())
# print(r.headers)


s = requests.Session()
# s.auth = ('admin', 'pass')
s.headers.update({'Authorization': f'Token {token}'})
r2 = s.get('http://pulse-rest-testing.herokuapp.com/roles2/')
print(r2.status_code)
print(r2.headers)
print(r2.json())
print(r2.text)
