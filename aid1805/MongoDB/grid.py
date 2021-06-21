# 获取数据库中gridfs文件
from pymongo import MongoClient
# 和pymongo模块是绑定在一起的
import gridfs

# 1.创建mongo的连接对象
conn = MongoClient('localhost', 27017)
# 2.数据库mygrid不存在则自动创建
db = conn.mygrid
# 3.获取gridfs对象
fs = gridfs.GridFS(db)
# 4.得到迭代对象
files = fs.find()


# print(files)
# print(files.count())

# files为可迭代对象，每个迭代值代表一个存入文件的对象，通过对象的属性可以获取文件信息
# for file in files:
#     print(file.filename)

for file in files:
    with open(file.filename, 'wb') as f:
        while True:
            # file对象有read接口，可以直接从数据库读取内容
            data = file.read(2048)
            if not data:
                break
            f.write(data)
conn.close()
