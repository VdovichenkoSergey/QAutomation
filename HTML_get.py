import requests
import json

r = requests.get('https://httpbin.org/get')
resp = r.json()
# resp_body = json.loads(r.text)
# print(resp)
# print(resp.keys())
# print(x.url)
# print(x.status_code)
# print(x.headers)
# print(x.text)

r1 = requests.post('https://httpbin.org/post', data='data')
print(r1.text)

resp1_body = r1.json()
print(resp1_body)
