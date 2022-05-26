from urllib import parse
from urllib.request import urlopen, Request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


base_url = 'http://cn.bing.com/search'
data = {'q': '云原生'}

url = '{}?{}'.format(base_url, parse.urlencode(data))

print(url)                 # http://cn.bing.com/search?q=%E4%BA%91%E5%8E%9F%E7%94%9F
print(parse.unquote(url))  # http://cn.bing.com/search?q=云原生

ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"

req = Request(url, headers={'User-agent': ua})

with urlopen(req) as res:
    with open('bing.html', 'wb+') as f:
        f.write(res.read())
        f.flush
