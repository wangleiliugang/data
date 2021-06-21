import pymysql

conn = pymysql.connect("localhost", "root", "123456", "python", charset="utf8")
cur = conn.cursor()

cur.execute("select * from t1;")
# sql_select = "select * from t1;"
# cur.execute(sql_select)

# data = cur.fetchone()
# print("fetchone的结果为：", data)

while True:
    data = cur.fetchone()
    if data is None:
        break
    print("fetchone的结果是：", data)

conn.commit()
cur.close()
conn.close()
