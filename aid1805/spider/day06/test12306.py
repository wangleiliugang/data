# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:15:17 2020

@author: 13775
"""
#安全套接层
import ssl
import urllib

# 创建一个不需要验证的上下文，自己来保证网站证书的安全
context = ssl._create_unverified_context()


url = "https://www.12306.cn/index/"
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}

req = urllib.request.Request(url, headers=ua_headers)
response = urllib.request.urlopen(req, context=context)

with open("12306.html", "wb") as f:
    f.write(response.read())
