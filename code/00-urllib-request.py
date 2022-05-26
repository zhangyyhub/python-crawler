import random
from urllib.request import urlopen, Request

# urllib.request.urlopen
url = 'http://www.bing.com'

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
]

req = Request(url)
req.add_header('User-agent', random.choice(ua_list))  # pick one
print(f'req type: {type(req)}')                       # req type: <class 'urllib.request.Request'>

# get method
response = urlopen(req, timeout=5)           # Open url or request object, return response object(file-like object)
print(response.closed)                       # False

with response:
    print(f'type: {type(response)}')         # type: <class 'http.client.HTTPResponse'>
    print(f'status: {response.status}')      # status: 200
    print(f'reason: {response.reason}')      # reason: OK
    print(f'real url: {response.geturl()}')  # real url: http://cn.bing.com/
    print(f'headers: {response.info()}')     # headers
    print(f'read: {response.read()}')        # 读取返回内容
    print(f'method: {response._method}')     # method: GET

print(response.closed)                       # True
print(req.get_header('User-agent'))          # Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;
print('user-agent'.capitalize())             # User-agent