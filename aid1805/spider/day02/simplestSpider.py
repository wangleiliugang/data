# -*- coding: utf-8 -*-


import requests


# http协议中requests请求，response
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}
response = requests.get("http://www.sina.com.cn", headers=headers, params=None)
print(response.text)
print(response.status_code)
print(response.encoding)
