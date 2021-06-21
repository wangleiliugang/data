# POST请求的交互方式
from urllib import request, parse
import json


youdaoURL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
           "X-Requested-With": "XMLHttpRequest",
           "Accept": "application/json, text/javascript, */*; q=0.01",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

while True:
    key = input("请输入您要翻译的英文，输入closeMe则退出：")
    if key == "closeMe":
        break
    formdata = {"i": key,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "16068304951076",
                "sign": "c12605cf87278ac11991702ceed38121",
                "lts": "1606830495107",
                "bv": "e2a78ed30c66e16a857c5b6486a1d326",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME"}
    # 做一次urlencode
    data = parse.urlencode(formdata).encode("utf-8")
    response = request.urlopen(youdaoURL, data)
    info = response.read().decode("utf-8")  # byte -> json str

    jsonLoads = json.loads(info)
    print("翻译如下:%s" % jsonLoads["translateResult"][0][0]["tgt"])

#  D:/学习资料/python/网络爬虫/day04/testCopyFiles2
