from urllib.request import Request, urlopen
import ssl    # 导入ssl模块

# req = Request('http://www.12306.cn/mormhweb/')  # 可以访问
# req = Request('https://www.baidu.com/')         # 可以访问
req = Request('https://www.12306.cn/mormhweb/')   # 报SSL认证异常

req.add_header(
    'User-agent',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
)

# 忽略不信任的证书: 可以忽略不校验的上下文
context = ssl._create_unverified_context()

res = urlopen(req, context=context)    # 上下文
with res:
    print(res._method)
    print(res.geturl())
    print(res.read().decode())