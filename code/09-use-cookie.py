import requests

# 登陆状态的推酷网页
url = "https://www.tuicool.com/ah/0/"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
cookies = {"Cookie": "CNZZDATA5541078=cnzz_eid%3D1937101849-1639816777-https%253A%252F%252Fwww.tuicool.com%252F%26ntime%3D1639816777; _tuicool_session=YXVXSDRjcW9ObVJxQUhEWXBFQ1o0bFAyVDZkSWNBV1JOUWgrSitkS0dObEtSQ0VpUmFvUzZub040YkVXOXVqOHkvYmtZTk1BUEpLaklzZ1NjRXNQMjhBOXBvMEZDbEYxcHEwdXdlWlpTb2RzZG1xaWo5cjZUdTc3SVNKNFd4VTZjditPN1NFSHVlbzRSSjNmbjJjaU1yQ1dFTnRhUlRWLzZKd2VzVWU3cFB6a21PZEtwUGlmVE5nSDUveFh4UG9HSlVLOGNGelZVTG5LU3NPcnZ2RW8xWDRCTGlpK1NLazJCcHRKT0pSWDRuUzFrLzlaMDY5My9obEFRdmlMSHlSenFieHY1S3JIbkpnbTVvRG9rdkZMMWtLVVE5YzVwNkg2bzRZWXpnYnR3SlE0MFI0MzA3ZHl4eXM0bmlNZVJSUXd2U2Z2QTFKaW81ak8vcmQ5RVNMTEsvWTJPNjBzMWtWQkY2dVFQTVQzd1dnPS0tV2tNRW85ekVzSWhOZmpJeTRIQXZ0dz09--5c8528f3b3414fe1832f2c2d5db5e4e71f3ac37e"}

response = requests.get(url, headers=headers, cookies=cookies)

data = response.content

with open("tuicool.html", "wb") as f:
    f.write(data)

