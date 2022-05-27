from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
url = 'https://movie.douban.com/j/search_subjects'

d = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 20,
    'page_start': 0
}

req = Request("{}?{}".format(url, urlencode(d)), headers={'User-agent': ua})

# 有可能失败，可以进行异常处理
with urlopen(req) as res:
    subjects = json.loads(res.read())
    print(len(subjects['subjects']))
    print(type(subjects), subjects)