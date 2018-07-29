import os
import sys
from package1.download_data.download_daily_price_volume_v2 import *
from package1.path import *
import numpy as np
import pandas as pd
import datetime
from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
import re
market='shenzhen'
from datetime import datetime
from matplotlib import pyplot as plt
#stock_path=os.path.join(stock_index_path,market)
#sto2=os.listdir(stock_path)
#stk_num=sto2[0][0:6]
#print sto2

date1=datetime(2017,9,6).strftime('%Y-%m-%d')
date2=datetime(2017,9,6).strftime('%Y-%m-%d')
stk_num="000001"
stock_path1=os.path.join(vol_price_path,market,stk_num)
stk_list=os.listdir(stock_path1)

## find volume price data file in a given date range
def find_stock_in_date_range(stk_num,date1,date2):
    stock_path1=os.path.join(vol_price_path,market,stk_num)
    stk_list=os.listdir(stock_path1)
    #print stk_list
    date_all=[re.split("_|.csv",x)[1] for x in stk_list] ### get the date in the stock file name i.e. 000001_2017-08-15.csv   get 2017-08-15
    ###----------- change the date time time
    date_all1=[datetime.strptime(x,'%Y-%m-%d') for x in date_all]
    #print date_all1
    date_all2=np.array([x.strftime('%Y-%m-%d') for x in date_all1])
    ####--------- find which file is in for the date time we choose
    file_in=((date_all2>=date1) & (date_all2<=date2))
    num_in=np.where(file_in==True)
    return num_in[0]


## the read_vol_price_data  ###
## read the daily download volume price data
## and reverse the rows as well as assign the column name
def read_vol_price_data(data_file):
    data1=pd.read_csv(data_file)
    data2=data1.iloc[::-1]
    #print data2.head
    data2.columns=['time','price','volume','status']
    return data2
