from http import cookiejar
from urllib import request
from urllib import parse


# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 通过HTTPCookieProcessor处理cookiejar
cookie_handler = request.HTTPCookieProcessor(cookie)

# 构建一个opener
opener = request.build_opener(cookie_handler)
opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0")]

# 使用post的方式发送数据包，用来进行登录
url = "http://www.renren.com/SysHome.do"
data = {"email": "XXX", "password": "YYY"}

data = bytes(parse.urlencode(data), encoding="utf-8")
req = request.Request(url, data=data, method="post")
response = opener.open(req)

# 登录之后，打开自己的主页
responseMyrenren = opener.open("http://www.renren.com/961482489/profied")
with open("myRenrenWithCookiejar.html", "wb") as f:
    f.write(responseMyrenren.read())
