import requests
import re
import json
import time
import random
from multiprocessing import Pool, Manager
import functools


MAXSLEEPTIME = 3
MINSLEEPTIME = 1
STATUS_OK = 200
MAX_PAGE_NUM = 10
SERVER_ERROR_MIN = 500
SERVER_ERROR_MAX = 600
CLIENT_ERROR_MIN = 400
CLIENT_ERROR_MAX = 500


# 1.对URL发起HTTP请求http request,得到相应的http response响应,response响应体中有我们需要的数据内容。
def get_one_page(URL, num_retry=5):  # https://maoyan.com/board/4?offset=0
    if num_retry == 0:
        return None
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    response = requests.get(URL, headers=ua_headers)
    if response.status_code == STATUS_OK:
        return response.text
    elif SERVER_ERROR_MIN <= response.status_code < SERVER_ERROR_MAX:
        time.sleep(MAXSLEEPTIME)
        get_one_page(URL, num_retry - 1)
    elif CLIENT_ERROR_MIN <= response.status_code < CLIENT_ERROR_MAX:
        # 正确的做法是写日志
        if response.status_code == 404:
            print("Page not find!")
        elif response.status_code == 403:
            print("Forbidden!")
        else:
            pass
    return None


# 2.使用正则表达式，XPath，bs4精确的获取数据。
def parse_one_page(html):
    pattern = re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    for i in items:
        yield{
            "title": i[0].strip(),
            "actor": i[1].strip(),
            "time": i[2].strip()
        }


# 3.将数据存到本地的文件系统中或者数据库中。
def write_to_file(item):
    with open("maoyan.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


# 4.控制整个爬取一个网页的流程。
def main(lock, offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)  # 拼出一个url
    html = get_one_page(url)  # 下载这个url
    print(html)
    for item in parse_one_page(html):  # 解析每个页面，并且把获取到的item一个一个写入文件
        lock.acquire()
        write_to_file(item)
        lock.release()
    time.sleep(random.randint(MINSLEEPTIME, MAXSLEEPTIME))


if __name__ == "__main__":
    manager = Manager()  # 在进程池之间传递lock,需要使用Manager的lock
    lock = manager.Lock()
    # 函数式编程:使用偏函数对原来的函数进行一层包装,得到包装后的函数
    partial_Crawl = functools.partial(main, lock)
    pool = Pool()
    pool.map(partial_Crawl, [i * 10 for i in range(10)])
    pool.close()
    pool.join()
