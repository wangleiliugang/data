'''
把某个文件夹下的文件拷贝到另外一个文件夹下；
文件个数不能少于1000个；
文件的类型需要有多种，图片/视频/压缩文件/文本文件/二进制文件等等；
使用多进程，多线程，进程池或线程池；
同时证明拷贝的文件没有错误（使用HASH）；
并考虑增加进度条。
'''
import os
from multiprocessing import Pool, Manager
import hashlib


CHUCKSIZE = 4096


def copyFile(fileName, srcPath, destPath, q):
    # 如果源路径不存在
    if not os.path.exists(srcPath):
        print("srcPath %s is not exist!" % srcPath)
        return False
    # 如果目标路径不存在
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("destPath %s make error!" % destPath)
            return False
    # 构造源文件路径和目标文件路径
    srcFileName = srcPath + '/' + fileName
    destFileName = destPath + '/' + fileName
    # 拷贝文件的过程
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)
    q.put(fileName)  # 把拷贝完成的文件添加到（在进程池当中使用的）队列中
    return True


# 对文件做hash处理
def hashFile(fileName):
    h = hashlib.sha256()
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    srcPath = input("请输入要拷贝的文件目录:")
    destPath = srcPath + "-副本"
    while os.path.exists(destPath):
        destPath = destPath + "-副本"
    allFileNames = os.listdir(srcPath)  # 返回指定的文件夹包含的文件或文件夹的名字的列表
    allNum = len(allFileNames)
    num = 0

    q = Manager().Queue()  # 注意:进程池中交互数据需要使用manager来进行托管
    pool = Pool()  # 使用进程池Pool拷贝文件
    for i in allFileNames:
        # 此处需要拷贝的文件是一个一个添加到进程池中的。
        pool.apply_async(func=copyFile, args=(i, srcPath, destPath, q))
    pool.close()

    # 添加进度条
    while num < allNum:
        fileName = q.get()
        num += 1
        rate = (num / allNum) * 100  # 计算当前的进度
        # 在主进程中用hash算法检验文件
        srcFileName = srcPath + '/' + fileName
        destFileName = destPath + '/' + fileName
        if (hashFile(srcFileName)) == hashFile(destFileName):
            print("%s copy ok" % srcFileName)
        else:
            print("%s copy fail" % srcFileName)
        print("Current rate is %.1f%%" % rate)
    pool.join()
    print("Copy files done!")
