# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:50:19 2021

@author: 13775
"""

import requests
import json


#接口的url
url = "http://fanyi.baidu.com"
#接口的参数
params = {
        "from":"en",
        "to":"zh",
        "query":"test"
        }
#发送接口
r = requests.request("post", url, params=params)
#打印结果
print(r.text)

d = json.loads(r.text)
print(d['data'][0][0]['v'])

