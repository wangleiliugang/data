import pymysql

# 打开数据库连接
conn = pymysql.connect("localhost", "root", "123456", charset="utf8")
# 创建一个游标对象
cur = conn.cursor()
# 创建库Python
cur.execute("create database if not exists python;")
# 切换库
cur.execute("use python;")
# 创建表
cur.execute("create table if not exists t1(\
    id int primary key,\
    name varchar(20),\
    score tinyint unsigned)default charset=utf8;")
# 在t1中插入5条记录
cur.execute("insert into t1 values\
    (1,'貂蝉',88),\
    (2,'赵子龙',100),\
    (3,'诸葛亮',80),\
    (4,'张飞',60),\
    (5,'司马懿',99);")
# 提交到数据库
conn.commit()
# 关闭游标
cur.close()
# 关闭数据库连接
conn.close()
