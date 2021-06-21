import urllib
import re


# GET请求的交互方式
ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
url = "http://www.baidu.com/s?"
keyword = input("请输入您要搜索的信息：")
wd = {"wd": keyword}
wd = urllib.parse.urlencode(wd)  # urlencode，目的是使浏览器能够识别URL中包含的非ASCII码的字符。
print(wd)
fullUrl = url + wd
# print(fullUrl)  # http://www.baidu.com/s?wd=python%E7%88%AC%E8%99%AB

# 对百度发起一次get请求
req = urllib.request.Request(fullUrl, headers=ua_headers)
response = urllib.request.urlopen(req)

# 将爬取的网页信息保存到本地
# with open("baiduSearch.html", "wb") as f:
#   f.write(response.read())

# 使用正则表达式来匹配百度的推荐
pattern = re.compile('<a class="c-gap-top-xsmall item_3WKCf" href="([\s\S]*?)">([\s\S]*?)</a>')
items = re.findall(pattern, response.read().decode('utf-8'))
# for i in items:
#    print(i[0], i[1])

# 将爬取后的内容写到文件中去
with open("baiduSearch.txt", "a") as f:
    for i in items:
        f.write("推荐:" + i[1] + " 链接:" + i[0] + "\n")
