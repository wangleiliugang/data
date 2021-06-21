#!/usr/bin/env python3
# coding=utf-8

from socket import *
import sys
import os
import time
import signal


# 发送注册请求
def do_register(s):
    while True:
        name = input("用户名:")
        passwd = input("密码：")
        passwd1 = input("确认密码：")
        if passwd != passwd1:
            print("密码不一致！")
            continue
        msg = 'R %s %s' % (name, passwd)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data[:2] == 'OK':
            return 0
        elif data[:6] == 'EXISTS':
            print("用户名已存在！")
            return -1
        else:
            return -1


def login(s, name):
    while True:
        print('''
            =========query command========
            --1:查词  2:历史记录  3:退出--
            ==============================
            ''')
        try:
            cmd = int(input('输入选项数字：'))
        except:
            print("输入有误！")
            continue
        if cmd not in [1, 2, 3]:
            print("请输入正确的选项数字")
            # 清除输入缓存
            sys.stdin.flush()
            continue
        if cmd == 1:
            do_query(s, name)
        elif cmd == 2:
            do_history(s, name)
        elif cmd == 3:
            break


# 登录请求
def do_login(s):
    name = input("用户名：")
    passwd = input("密码：")
    msg = 'L %s %s' % (name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data[:2] == 'OK':
        return name
    else:
        return -1


# 发送查词请求
def do_query(s, name):
    while True:
        word = input("请输入查询的单词(输入##退出)：")
        if word == '##':
            break
        msg = 'Q %s %s' % (name, word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data[:2] == 'OK':
            data = s.recv(2048).decode()
            if data[:9] == 'not found!':
                print("没有找到这个单词！")
            else:
                print(data)
        else:
            print("查词失败！")
    return


# 发送查看记录请求
def do_history(s, name):
    msg = 'H %s' % name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data[:2] == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("获取历史记录失败！")


# 发送连接请求
def main():
    if len(sys.argv) != 3:
        print('argv is error!')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        print('''
            ==========Welcome=========
            --1:注册  2:登录  3:退出--
            ==========================
            ''')
        try:
            cmd = int(input('输入选项数字：'))
        except:
            print("输入错误！")
            continue
        if cmd not in [1, 2, 3]:
            print("请输入正确的选项数字")
            # 清除输入缓存
            sys.stdin.flush()
            continue
        if cmd == 1:
            if do_register(s) == 0:
                print("恭喜！注册成功！")
            else:
                print("注册失败！")
        elif cmd == 2:
            name = do_login(s)
            if name == -1:
                print("登录失败！")
            else:
                print("恭喜！登录成功！")
                login(s, name)
        elif cmd == 3:
            s.send(b'E')
            s.close()
            sys.exit(0)


if __name__ == '__main__':
    main()
