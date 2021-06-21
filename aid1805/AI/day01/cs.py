import os
import sys
import platform
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md

def dmy2ymd(dmy):
    return dt.datetime.strptime(dmy,'%Y-%m-%d').date().strftime('%Y-%m-%d')

def read_data(filename):
    dates,open_prices,highest_prices,lowest_prices,clos_prices = \
    np.loadtxt(filename,delimiter=',',usecols=(1,2,3,4,5),unpack=True,\
        dtype=np.dtype('M8[D],f8,f8,f8,f8'),converters={'1':dmy2ymd})
    print(dates)
    print(open_prices)

def main(argc,argv,envp):
    # dates,open_prices,highest_prices,lowest_prices,clos_prices = read_data('aapl.csv')
    read_data('aapl.csv')
    return 0


if __name__ == '__main__':
    main(len(sys.argv),sys.argv,os.environ)