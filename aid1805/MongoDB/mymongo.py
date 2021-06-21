from pymongo import MongoClient
import pymongo

# 1.创建mongo的连接对象
conn = MongoClient('localhost', 27017)
# 2.选择要连接的数据库(使用_getitem_和_setitem_两个魔法函数可以修改属性的取值方法)
# db = conn['stu']
db = conn.stu
# 3.选择要连接的集合
# my_set = db['class3']
my_set = db.class3


# print(my_set)
# print(dir(my_set))

# 插入数据
# my_set.insert({'name':'铁林','king':'乾隆'})
# my_set.insert([{'name':'道明','king':'康熙'},{'name':'国立','king':'康熙'}])
# my_set.insert_many([{'name':'张三','king':'雍正'},{'name':'李四','king':'雍正'}])
# my_set.insert_one({'name':'王五','king':'乾隆'})
# my_set.save({'name':'中山','king':'总统'})

# 删除操作
# my_set.remove({'name':'铁林'})  # 删除匹配到所有数据
# my_set.remove({'name':'道明'},multi = False)  # 只删除匹配到的第一条数据
# my_set.remove()  # 删除全部内容

# 查找操作
cursor = my_set.find({})
# print(cursor)
for i in cursor:
    # print(i)
    print(i['name'], '-->', i['king'])


cls0 = db.class0
# for i in cls0.find({'age':{'$lt':20}}):
#     print(i['name'],':',i['age'])

# 通过cursor可以使用find后内容的修饰函数
# print(cursor.count())
# for i in cursor.skip(2).limit(3):
#     print(i)

# cursor为迭代对象，取完值后就不能使用sort
# for i in cursor.sort([('name',1)]):
#     print(i)
# cursor.next()

# 先写出字典表示query，然后传入
# dic = {'$or':[{'name':'bqiang'},{'age':{'$gt':18}}]}
# for i in cls0.find(dic):
#     print(i)

# print(cls0.find_one(dic))

# data = cls.find_one(dic)
# cls.remove(data['_id'])

# 修改操作
# my_set.update({'name':'国立'},{'$set':{'name':'国强'}})
# my_set.update({'name':'小李'},{'$set':{'king':'乾隆'}},upsert = True)
# my_set.update({'king':'康熙'},{'$set':{'other_name':'玄烨'}}, upsert=False, multi=True)

# my_set.update_many({'king':'乾隆'},{'$set':{'other_name':'弘历'}})
# my_set.update_one({'name':'中山'},{'$set':{'name':'铁林','king':'乾隆'}})

# my_set.find_one_and_delete({'name':'张三'})

# 关闭数据库连接
conn.close()
