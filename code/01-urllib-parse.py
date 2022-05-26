from urllib import parse

# 实例一：
u = parse.urlencode({
    "id":1,
    "name":"tom"
})
print(u)    # id=1&name=tom


# 实例二：
"""
url = "http://www.bing.com/?id=1&name=tom" ——> GET
url = "http://www.bing.com/" ——> POST
body = "id=1&name=tom"
"""
u = parse.urlencode({
    "id":1,
    "name":"tom",
    "url":"http://www.bing.com/?id=1&name=tom"
})
print(u)    # id=1&name=tom&url=http%3A%2F%2Fwww.bing.com%2F%3Fid%3D1%26name%3Dtom


# 实例三：
u = parse.urlencode({
    "id":1,
    "name":"张三",
    "url":"http://www.bing.com/?id=1&name=张三"
})
print(u)    # id=1&name=%E5%BC%A0%E4%B8%89&url=http%3A%2F%2Fwww.bing.com%2F%3Fid%3D1%26name%3D%E5%BC%A0%E4%B8%89


# 实验四：
# 网页使用utf-8编码
# https://www.baidu.com/s?wd=中
# 上面的url编码后为：https://www.baidu.com/s?wd=%E4%B8%AD

u = parse.urlencode({'wd':'中'})    # 编码 ——> wd=%E4%B8%AD
url = "https://www.baidu.com/s?{}".format(u)
print(url)    # https://www.baidu.com/s?wd=%E4%B8%AD

print('中'.encode('utf-8'))    # b'\xe4\xb8\xad'
print(parse.unquote(u))        # 解码 ——> wd=中
print(parse.unquote(url))      # https://www.baidu.com/s?wd=中