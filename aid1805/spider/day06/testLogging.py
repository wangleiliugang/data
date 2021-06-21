# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:29:28 2020

@author: 13775
"""

#日志，写日志的流程基本是固定的。
import logging
import sys

# 1.创建日志的实例
logger = logging.getLogger("testLogger")

# 2.定制logger的输出格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

# 3.创建日志：文件日志，终端日志 
file_handler = logging.FileHandler("testLogger.log")#文件日志
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler(sys.stdout)#终端日志
console_handler.setFormatter(formatter)

# 4.设置默认的日志级别
logger.setLevel(logging.INFO)

# 5.把文件日志和终端日志添加到文件日志处理器中
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# 编写日志信息
logger.critical("test critical log!")
logger.error("test error log!")
logger.warning("test warning log!")
logger.info("test info log!")
logger.debug("test debug log!")

# 6.当不再使用日志handler时，需要remove
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)
