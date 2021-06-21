import os
import sys


# os._exit(0)

# sys.exit("结束了...")

# 对sys.exit()进行异常捕获后，程序不会结束
try:
    sys.exit("结束了！")
except SystemExit as e:
    print("异常信息：", e)

print("process over")
