import os
import sys
#from package1.download_data.download_daily_price_volume_v2 import *
#from load_path import *
from package1.path import *
import numpy as np
import pandas as pd
import datetime
#from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
import re
market='shenzhen'
from datetime import datetime
from matplotlib import pyplot as plt
#stock_path=os.path.join(stock_index_path,market)
#sto2=os.listdir(stock_path)
#stk_num=sto2[0][0:6]
#print sto2
market='shenzhen'
date1=datetime(2017,8,20).strftime('%Y-%m-%d')
date2=datetime(2017,9,6).strftime('%Y-%m-%d')
stk_num="000001"
fi1=30
stock_path1=os.path.join(vol_price_path,market,stk_num)
stk_list=os.listdir(stock_path1)


class data_basic:
    def __init__(self,data_file):
        self.data_file=data_file
        data1=pd.read_csv(data_file)
        data2=data1.iloc[::-1]
        #print data2.head
        data2.columns=['time','price','volume','status']
        self.data=data2
    def print_data(self):
        print self.data.head()
    def basic_stat(self):
        min_pr=min(self.data.price)
        max_pr=max(self.data.price)
        open_pr=self.data.price.iloc[0]
        close_pr=self.data.iloc[-1:].price[0]
        return [min_pr,max_pr,open_pr,close_pr]

data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s" % (stk_num,stk_list[fi1])
emp1 =data_basic(data_file)
emp1.print_data()
min_pr,max_pr,open_pr,close_pr=emp1.basic_stat()

print 'minimum price is ',min_pr
print 'maximum price is ',max_pr
print 'opening price is ',open_pr
print 'close price is ',close_pr


'''

class data_basic_v2(data_file):
    data1=pd.read_csv(data_file)
    data=data1.iloc[::-1]
    #print data2.head
    data.columns=['time','price','volume','status']
    def __init__(self,data_file):
        self.data_file=data_file
    def print_data(self):
        print self.data.head
    def basic_stat(self):
        return [min(self.data.price),max(self.data.price)]
'''

