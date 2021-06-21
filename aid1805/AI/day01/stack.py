import os
import sys
import numpy as np

def main(argc,argv,envp):
    a = np.arange(1,10).reshape(3,3)
    b = a*10
    c = np.vstack((a,b))
    print(c)
    d = np.hstack((a,b))
    print(d)
    e = np.dstack((a,b))
    print(e)
    f = a.ravel()
    g = b.ravel()
    h = g * 10
    i = np.row_stack((f,g,h))
    print(i)
    j = np.column_stack((f,g,h))
    print(j)

    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv),sys.argv,os.environ))
