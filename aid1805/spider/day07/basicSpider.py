# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:20:34 2020

@author: 13775
"""

import logging
import sys
import urllib
import random
import time

#创建日志的实例
logger = logging.getLogger("basicSpider")
#定制logger的输出格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
#创建日志：文件日志，终端日志 
file_handler = logging.FileHandler('basicSpider.log')#文件日志
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler(sys.stdout)#终端日志
console_handler.setFormatter(formatter)
#设置默认的日志级别
logger.setLevel(logging.INFO)
#把文件日志和终端日志添加到文件日志处理器中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

PROXY_RANGE_MIN = 1
PROXY_RANGE_MAX = 10
PROXY_RANGE = 2
RETRY_NUM = 3
NUM = 10


def downloadHtml(url,headers=[],proxy={},num_retries=RETRY_NUM,timeout=NUM,decodeInfo="utf-8"):
    """
    爬虫的get请求，考虑了UA等http request head部分的设置；
    支持代理服务器的信息处理；
    返回的状态码不是200，该如何处理；
    考虑超时问题，及网页的编码问题；
    """
    html = None
    if num_retries <= 0:
        return html
    #一般使用UA池和proxy池相结合的方式来访问某个页面，会更加不容易被反爬。
    
    #动态调整代理服务器的使用策略。
    if random.randint(PROXY_RANGE_MIN,PROXY_RANGE_MAX) > PROXY_RANGE:
        logger.info("no proxy")
        proxy = None    
    
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    opener.addheaders = headers
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode(decodeInfo)
    except UnicodeDecodeError:
        logger.error("UnicodeDecodeError")
    except urllib.error.URLError or urllib.error.HTTPError as e:
        logger.error("urllib error")
        if hasattr(e,'code') and 400 <= e.code < 500:
            logger.error("client error")#客户端问题，可以通过分析日志来解决
        elif hasattr(e,'code') and 500 <= e.code <600:
            html = downloadHtml(url,
                                headers,
                                proxy,
                                num_retries-1,
                                timeout,
                                decodeInfo)
            time.sleep(PROXY_RANGE_MAX)
    except:
        logger.error("download error")
    return html


if __name__ == "__main__":
    url = "http://www.baidu.com/"
    headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0")]
    proxy = {"123.101.207.22":"9999"}
    
    print(downloadHtml(url,headers,proxy))
    
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)
