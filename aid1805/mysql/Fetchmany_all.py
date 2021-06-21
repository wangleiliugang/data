import pymysql

conn = pymysql.connect("localhost", "root", "123456", "python", port=3306, charset="utf8")
cur = conn.cursor()

sql_select = "select * from t1;"
cur.execute(sql_select)
print("select语句查出的记录个数为：", cur.rowcount)

# sql_update = "update t1 set score=100 where name='诸葛亮';"
# cur.execute(sql_update)

data1 = cur.fetchmany(2)
# print("fetchmany(2)的结果集为：", data1) #输出结果为元组对象，可迭代
for i in data1:
    print(i)

data2 = cur.fetchall()
# print("fetchall()的结果集为：", data2)
for i in data2:
    print(i)

conn.commit()
cur.close()
conn.close()
