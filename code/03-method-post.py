from urllib.request import Request, urlopen
from urllib.parse import urlencode

req = Request('http://httpbin.org/post')
req.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
)

data = urlencode({'name': '张三,@=/&*', 'age': '6'})
print(data)           # name=%E5%BC%A0%E4%B8%89%2C%40%3D%2F%26%2A&age=6
print(data.encode())  # b'name=%E5%BC%A0%E4%B8%89%2C%40%3D%2F%26%2A&age=6'

# POST方法(From提交数据)不做url编码会有风险
with urlopen(req, data=data.encode()) as res:
    print(res.read())

