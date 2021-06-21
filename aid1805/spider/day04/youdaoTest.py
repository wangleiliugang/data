from urllib import request, parse
import json


# POST请求的交互方式
youdaoURL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
           "X-Requested-With": "XMLHttpRequest",# 可以处理ajax
           "Accept": "application/json, text/javascript, */*; q=0.01",  # 可以接收json信息
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

while True:
    key = input("请输入要翻译的英文，输入closeMe退出：")
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
                "action": "FY_BY_REALTlME",
                }
    # 做一次urlencode；由于POST请求需要发送byte类型的数据，所以此处需要转换为bytes
    data = bytes(parse.urlencode(formdata), encoding="utf-8")

    req = request.Request(youdaoURL, data, headers, method="POST")
    response = request.urlopen(req)
    info = response.read().decode("utf-8")  # byte --> str
    jsonLoads = json.loads(info)  # str --> dict
    print("翻译结果:%s" % jsonLoads["translateResult"][0][0]["tgt"])
