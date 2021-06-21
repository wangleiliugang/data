# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:06:51 2020

@author: 13775
"""

import urllib
import re

#url = "http://www.sina.com.cn"
#proxy_addr = "114.106.135.122:4256"
#proxy = urllib.request.ProxyHandler({"http":proxy_addr})

##替换handler，以实现可以处理proxy的功能
#opener = urllib.request.build_opener(proxy)

##将opener装载进urllib库中，就可以使用自己写的功能
#urllib.request.install_opener(opener)
#response = urllib.request.urlopen(url,timeout=5)

#data = response.read().decode('utf-8')
#print(data)


#如何快速的判断一个代理服务器是否是可用的？
#封装一个方法，用来检测当前的这个代理服务器是否可用。
def checkProxy(proxy_addr):
    data = ""
    url = "http://www.baidu.com"
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(url, timeout=10)
        data = response.read().decode('utf-8')
    except:
        pass
    
    pattern = re.compile("<title>百度一下，你就知道</title>")
    title = re.findall(pattern, data)
    print(title)
    if len(title) == 0:
        return False
    else:
        return True
    
print(checkProxy("203.189.89.153:8080"))

#checkProxy("name:password@ip:port")  私密代理服务器的格式
