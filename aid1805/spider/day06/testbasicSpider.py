# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:48:35 2020

@author: 13775
"""

# 调用自己写的方法basicSpider.py
import basicSpider

url = "http://www.sina.com.cn/"
headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0")]
proxy = {"123.101.207.22":"9999"}

with open("sina.html", "wb") as f:
    f.write(basicSpider.downloadHtml(url,headers,proxy).encode("utf-8"))
