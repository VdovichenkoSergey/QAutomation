from http.client import HTTPConnection
from urllib.parse import urlencode
import json
base_url = "pulse-rest-testing.herokuapp.com"
data = urlencode({'name': 'A', 'type':'B'})
headers = {
     'Content-Type': 'application/x-www-form-urlencoded'
}
data2 = urlencode({'name':'Agg', 'type':'Bgg'})
con = HTTPConnection(base_url, timeout=10)
con.request('POST', '/roles', data, headers=headers)
result = con.getresponse().read().decode()
res_dict = json.loads(result)
print(res_dict)

con.request('GET', f'/roles/{res_dict["id"]}')
result = con.getresponse()
print(result.read().decode())

con.request('GET', '/roles')
result = con.getresponse()
print(result.read().decode())

con.request('PUT', f'/roles/{res_dict["id"]}', data2, headers)
result = con.getresponse()
print(result.read().decode())

con.request('GET', f'/roles/{res_dict["id"]}')
result = con.getresponse()
print(result.read().decode())

con.request('GET', '/roles')
result = con.getresponse()
print(result.read().decode())

con.request('DELETE', f'/roles/{res_dict["id"]}')
result = con.getresponse()
print(result.read().decode())
# проверяем что удалилось
con.request('DELETE', f'/roles/{res_dict["id"]}')
result = con.getresponse()
print(result.read().decode())
con.close()
