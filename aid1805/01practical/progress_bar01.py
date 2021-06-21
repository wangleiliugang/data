# import time
# from progressbar import *


# progress = ProgressBar()
# for i in progress(range(100)):
#     time.sleep(0.1)





def write_to_file(dic, filename='./cache'):
    try:
        f = open(filename, 'w')
        for i in dic:
            f.write(str(dic))
        f.close()
    except OSError as err:
        # print("打开文件失败！")
        raise err


class calcounter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@calcounter
def func1():
    dic = {"times": func1.count}
    write_to_file(dic)


func1()
func1()
func1()

print('func1函数被调用次数:', func1.count)
