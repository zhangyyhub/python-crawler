import requests

url = "http://httpbin.org/get"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

proxies = {
    "http": "http://59.58.47.172:4213"
}

response = requests.get(url, headers=headers, proxies=proxies, timeout=3)

print(response.text)    # 代理IP不可用直接报错


"""
执行结果：
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6290781f-47674ddb6fa420a71f79bc08"
  }, 
  "origin": "59.58.47.172", 
  "url": "http://httpbin.org/get"
}
"""