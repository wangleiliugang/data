import requests
import re
import json


STATUS_OK = 200


# 1.对URL发起HTTP请求http request,得到相应的http response响应,response响应体中有我们需要的数据内容。
def get_one_page(URL):  # https://maoyan.com/board/4?offset=0
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}
    response = requests.get(URL, headers=ua_headers)
    if response.status_code == STATUS_OK:
        return response.text
    return None


print(get_one_page("https://maoyan.com/board/4?offset=0"))


# 2.使用正则表达式，XPath，bs4精确的获取数据。
def parse_one_page(html):
    pattern = re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    for i in items:
        # s.strip():返回去掉左右空白字符的字符串
        # print(i[0].strip(), i[1].strip(), i[2].strip())
        yield(i[0].strip(), i[1].strip(), i[2].strip())


parse_one_page(get_one_page("https://maoyan.com/board/4?offset=10"))


# 3.将数据存到本地的文件系统中或者数据库中。
def write_to_file(item):
    with open("maoyan0.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
