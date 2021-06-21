# 将文件以二进制方式存储
from pymongo import MongoClient
import bson.binary

# 1.创建mongo的连接对象
conn = MongoClient('localhost', 27017)
# 2.数据库savefile不存在则自动创建
db = conn.savefile
# 3.集合image不存在则自动创建
my_set = db.image

'''
# 将文件(图片)存储到数据库中
file = 'myc-x17.jpg'
f = open(file, 'rb')
# 将读取的二进制字节流，变为bson格式的二进制字串
dic = dict(content=bson.binary.Binary(f.read()), filename='myc-x17.jpg')
# 插入文档(使用save/insert都可以)
my_set.save(dic)
'''

# 从数据库中提取文件
# 获取存储文件的文档字典
data = my_set.find_one({'filename': 'myc-x17.jpg'})

with open('c-x17.jpg', 'wb') as f:
    f.write(data['content'])

conn.close()
