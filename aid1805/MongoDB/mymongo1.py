from pymongo import MongoClient, IndexModel


conn = MongoClient('localhost', 27017)
db = conn.stu
my_set = db.class3
cls = db.class1

# print(dir(my_set))


# 索引操作
# index = my_set.ensure_index('name')
# print(index)

# 创建复合索引；1表示升序，-1表示降序
# index = my_set.ensure_index([('name',1),('king',-1)])
# print(index)

# 同时创建多个索引
# # 1.先生成索引对象
# index1 = IndexModel([('name',1),('king',-1)])
# index2 = IndexModel([('other_name',1)])
# # 2.将索引对象放入列表中，使用create_indexes生成索引
# indexes = my_set.create_indexes([index1,index2])
# print(indexes)

# 创建唯一索引
# index = cls.ensure_index('name', unique=True, sparse=True)

# 查看指定集合中的索引
# for i in my_set.list_indexes():
#     print(i)

# 删除索引
# my_set.drop_index('name_1_king_-1')
# for i in my_set.list_indexes():
#     print(i)
# 删除所有索引
# my_set.drop_indexes()
# for i in my_set.list_indexes():
#     print(i)

# 聚合操作
l1 = [{'$group':{'_id':'$king', 'count':{'$sum': 1}}}, {'$match':{'count':{'$gt': 1}}}]
cursor = my_set.aggregate(l1)
for i in cursor:
    print(i)
