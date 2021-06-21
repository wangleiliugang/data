import os
import sys
import datetime as dt
import numpy as np

def dmy2days(dmy):
    return (dt.datetime.strptime(dmy,'%d-%m-%Y').date() - dt.date.min).days

def read_data(filename):
    times,close_prices = np.loadtxt(
        filename,delimiter=',',usecols=(1,5),unpack=True,converters={1:dmy2days})
    return times,close_prices

def auto_twap(times,close_prices):
    twap = np.average(close_prices,weights=times)
    return twap

def manu_twap(times,close_prices):
    twp,tt = 0.,0.
    for i,j in zip(times,close_prices):
        twp += i * j
        tt += i
    twap = twp /tt
    return twap

def main(argc,argv,envp):
    times,close_prices = read_data('aapl1.csv')
    print(auto_twap(times,close_prices))
    print(manu_twap(times,close_prices))
    return 0


if __name__ == '__main__':
    main(len(sys.argv),sys.argv,os.environ)