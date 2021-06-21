#!/usr/bin/env python3
# coding=utf-8

# name:leizi
# date:2019+-5-16
# email:137753633@qq.com
# This is a dict project for AID 1812 python web
# python3.5 mysql pymysql

from socket import *
import os
import signal
import time
import pymysql
import sys

DICT_TEXT = './dict.txt'
HOST = '127.0.0.1'
PORT = 10120
ADDR = (HOST, PORT)


# 执行子进程具体任务
def do_child(c, db):
    while True:
        # 接收客户端请求
        data = c.recv(128).decode()
        print('Client request:', data)
        if data[0] == 'R':
            do_register(c, db, data)
        if data[0] == 'E':
            c.close()
            sys.exit(0)
        if data[0] == 'L':
            do_login(c, db, data)
        if data[0] == 'Q':
            do_query(c, db, data)
        if data[0] == 'H':
            do_history(c, db, data)


# 用户注册
def do_register(c, db, data):
    print("执行用户注册")
    cursor = db.cursor()
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    sql = "select * from user where name = '%s';" % name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    sql = "insert into user values('%s','%s');" % (name, passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b'FALL')
        db.rollback()
        return
    # 没有异常产生时执行else
    else:
        print("恭喜！注册成功！")
    cursor.close()


# 用户登录
def do_login(c, db, data):
    print("登录操作")
    cursor = db.cursor()
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    try:
        sql = "select * from user where name = '%s' and passwd = '%s';" % (name, passwd)
        cursor.execute(sql)
        r = cursor.fetchone()
    except:
        pass
    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'OK')
    return


# 查词
def do_query(c, db, data):
    print("查询操作")
    cursor = db.cursor()
    l = data.split(' ')
    name = l[1]
    word = l[2]
    try:
        f = open(DICT_TEXT, 'rb')
        c.send(b'OK')
    except:
        c.send(b'FALL')
        return
    time.sleep(0.1)
    while True:
        line = f.readline().decode()
        tmp = line.split(' ')
        if tmp[0] > word:
            c.send(b'not found!')
            f.close()
            break
        if word == tmp[0]:
            c.send(line.encode())
            insert_history(db, name, word)
            f.close()
            return


def insert_history(db, name, word):
    print("插入历史记录")
    cursor = db.cursor()
    insert_time = time.ctime()
    sql = "insert into hist value ('%s','%s','%s');" % (name, insert_time, word)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        return
    else:
        print("插入成功！")


# 查看历史记录
def do_history(c, db, data):
    print("查询历史记录操作")
    name = data.split(' ')[1]
    cursor = db.cursor()
    try:
        sql = "select * from hist where name = '%s';" % (name,)
        cursor.execute(sql)
        r = cursor.fetchall()
        if not r:
            c.send(b'FALL')
            return
        else:
            c.send(b'OK')
    except:
        pass
    for i in r:
        # 防止粘包
        time.sleep(0.1)
        msg = "%s %s %s" % (i[0], i[1], i[2])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')


# tcp并发通信接收连接
def main():
    # 生成数据库对象
    db = pymysql.connect('localhost', 'root', '123456', 'mydict', charset="utf8")

    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            c, addr = s.accept()
            print('Connect from:', addr)
        except KeyboardInterrupt:
            # raise
            os._exit(0)
        except:
            continue
        # 创建子进程
        pid = os.fork()
        if pid < 0:
            print('Creat child process failed!')
            c.close()
        elif pid == 0:
            s.close()
            do_child(c, db)
        else:
            c.close()
            continue
    db.close()
    s.close()
    os._exit(0)


if __name__ == '__main__':
    main()
