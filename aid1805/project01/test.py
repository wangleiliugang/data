import re
import sys


# 2.将每段数据使用正则表达式进行匹配
def reg(data, port):
    # 获取每段的第一个单词
    pattern = r'^\S+'
    re_obj = re.compile(pattern)
    try:
        head_word = re_obj.match(data).group()
    except Exception:
        return None
    if port == head_word:
        pattern1 = r'address is (\w{4}\.\w{4}\.\w{4})'
        try:
            match_obj = re.search(pattern1, data)
            return match_obj.group(1)
        except Exception:
            return None
    else:
        return None


# 1.分段获取数据
def main(port):
    fd = open('1.txt', 'r')
    fd.readline()
    fd.readline()
    while True:
        data = ''
        while True:
            s = fd.readline()
            if s == '\n':
                break
            if not s:
                print('file search over!')
                return
            data += s
        # 将每段数据传入函数进行匹配
        result = reg(data, port)
        if result:
            print("address is:", result)
            return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('argv error!　请输入对应的设备名称。')
        sys.exit(1)
    main(sys.argv[1])
