
# from multiprocessing import Process
from threading import Thread
g_num = 100
import time

def getTime(interval):
    global g_num
    while True:
        time.sleep(interval)
        g_num += 100
        print("in child process g_num is %d" % g_num)
        
if __name__ == "__main__":
    # p = Process(target=getTime,args=(1,))
    # p.start()
    t = Thread(target=getTime,args=(1,))
    t.start()
    
    while True:
        time.sleep(2)
        g_num += 1
        print("in parent process g_num is %d" % g_num)
        
        