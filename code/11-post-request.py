import requests

url = "https://www.tuicool.com/login"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "cookie": "_tuicool_session=VktvMnNQbFExQ0g3ejBZZ1lHdkc5WXNtWFQ1T1U1MVJkaWVlNVdpZXpqemJYcmNXaU43U0dLVEd3LzlHRnNxUUFvV1YrYUpjaEVBakdUN0YvQzV0dzZzQTlOVUxVRStZQmVXalJ1UnRrakp6L2ZHV2p3T1g4OFpLSUxNMjlzb2JjQkFYYlF3MHBIczgxOHRHaGJETHhDeUVFRE5mcERSY2dmd3V2algxSWs0b3NBeittd0w1cEgzYVk2SW9oMDZza0h2UHFZY1BxQ3ZZelplZFRSR1dYT1pYaTNlY2E5ejgwOERjaDJCMHVxTk85NEM5UzBrVXZsdFllaDdKbk5lZVlFbGI0emRmVXpOQXBwOXk0dktyRFY5NU1XYzZkVHVqaXVlT1JKZERQdFV6bnZwcTNwWnU0QnQ2YVZSVU5ORC8rSGVpUm9RdkZlNGgvREwrcDI2Tm9BPT0tLUNFc3c4Y0E5aG1xY3Q3bHpLUDk4a3c9PQ%3D%3D--4de5cd5394d52727fa93508dec10150a1a8d84d4"
}

data = {
    "authenticity_token": "L6tjk5jL+c48fBeG9JTr3NJ6DCzB4RLbFmLfPjbFEu9/ZNx4Nf6K4BpmtDoqbJIAqqIM62EmC2r6nXKfmAUVtA==",
    "email": "zyyyxdz@163.com",
    "password": "Zhang890"
}


response = requests.post(url, headers=headers, data=data)

data = response.content

with open("tuicool_login.html", "wb") as f:
    f.write(data)

