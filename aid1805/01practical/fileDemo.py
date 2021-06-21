
def print_directory_contents(sPath):
    '''
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，以及其包含文件夹中文件的路径。
    '''
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print sChildPath


# os.listdir('path'): 获取指定目录下所有的文件列表
# os.listdir('.'): 获取当前文件夹下的所有文件列表
# os.path.isfile('filename'): 判断文件是否为普通文; 返回值False表示不是普通文件，True表示普通文件.
# os.path.isdir(directory): 判断directory是否为目录
# os.path.join(sPath, sChild):路径拼接,将sPath,sChild拼接成一个字符串
# os.path.sep:表示文件分隔符

# os.unlink('./sockfile01'):用于删除文件,如果文件是一个目录则返回一个错误
# os.path.exists('./sockfile01'):  判断sockfile01文件是否存在;如果存在返回True,不存在返回False
# os.path.getsize('fork.py')：  获取文件的大小(返回值：文件内容的字节数。)
# os.mkdir(destPath):  创建一个文件路径destPath
# os.getcwd():返回当前工作目录
