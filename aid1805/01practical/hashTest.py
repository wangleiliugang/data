import hashlib


CHUCKSIZE = 2048


def hashStr(strInfo):
    """
    对字符串进行hash,得到一个十六进制的指纹数据。
    """
    h = hashlib.md5()
    # h = hashlib.sha1()/h = hashlib.sha256()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()


print(hashStr("hello"))
print(hashStr("hello1"))


def hashFile(fileName):
    """
    对文件进行hash，得到一个十六进制的指纹数据。
    """
    h = hashlib.sha256()  # 创建hash对象
    with open(fileName, "rb") as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
            print("h:", h)
    return h.hexdigest()


print(hashFile("gui.py"))
