import os
import sys
import datetime as dt
import numpy as np

def python_sum(n):
    a = [i ** 2 for i in range(n)]
    b = [i ** 3 for j in range(n)]
    c = []
    for i in range(n):
        c.append(a[i] + b[j])
    return c


def numpy_sum(n):
    return np.arange(n) ** 2 + np.arange(n) ** 3


def main(argc,argv,envp):
    n = 100000
    start = dt.datetime.now()
    c = python_sum(n)
    print((dt.datetime.now() - start).microseconds)
    
    start1 = dt.datetime.now()
    c = numpy_sum(n)
    print((dt.datetime.now() - start1).microseconds)
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv),sys.argv,os.environ))
