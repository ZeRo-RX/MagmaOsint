import requests

r = requests.get('https://api.github.com/events')
print(r.text)








"""
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"type":"User"...'
r.json()



////////////////////////////////
import requests

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get('https://httpbin.org/get', params=payload)
print('[url]: {%s} : %s' % (r.url , r))
"""