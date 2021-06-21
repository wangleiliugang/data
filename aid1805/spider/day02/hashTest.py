# -*- coding: utf-8 -*-


import hashlib


CHUCKSIZE = 2048


# 对字符串进行hash,得到一个十六进制的指纹数据
def hashStr(strInfo):
    h = hashlib.md5()
    # h = hashlib.sha1()/h = hashlib.sha256()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()


print(hashStr("hello"))
print(hashStr("hello1"))


# 对文件进行hash，得到一个十六进制的指纹数据
def hashFile(fileName):
    h = hashlib.sha256()  # 创建hash对象, <sha256 HASH object @ 0x7fd629195760>
    with open(fileName, "rb") as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


print(hashFile("getMaxMin.py"))
