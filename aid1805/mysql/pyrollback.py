import pymysql

conn = pymysql.connect("localhost", "root", "123456", "db3", port=3306, charset="utf8")
cur = conn.cursor()

try:
    cur.execute("update CCB set money=95000 where name='转钱';")
    cur.execute("update ICBC set money=7000 where name='借钱';")
    conn.commit()
    print("提交成功ok!")
except Exception as e:
    conn.rollback()
    print("出现错误，已经回滚：", e)

cur.close()
conn.close()
