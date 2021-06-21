# -*- coding: utf-8 -*-


# 演示最简单的爬虫程序
import requests


# 方式1
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}
url = "http://www.sina.com.cn"
response = requests.get(url, headers=headers, params=None)
response.encoding = 'utf-8'
print('状态码:', response.status_code)
# print(response.text)
# 将抓取的网页保存到文件中
with open('sina.html', 'wb') as f:
    f.write(response.text.encode('utf-8'))


# 方式2
# fro2m urllib import request


# # 方式2
# req = request.Request("http://www.sina.com.cn")  # 构造request请求
# response = request.urlopen(req)  # 得到了response响应信息
# # print(type(response.read()))  # <class 'bytes'>
# print(response.read().decode("utf-8"))
