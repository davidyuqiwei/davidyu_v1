import os
import sys
#from load_path import *
import numpy as np
#import pandas as pd
import datetime
#from numpy._distributor_init import NUMPY_MKL
import re
from datetime import datetime
import itertools
from package_path_define.path_define import *
from package_readdata.read_data import * # load read data function


market='shenzhen'
stock_index_file="shanghai_shenzhen_data_from_2013"
stock_path='\\'.join([main_path_data,stock_index_file,market])
sto2=os.listdir(stock_path)
# define: date and market
date1=datetime(2017,10,30).strftime('%Y-%m-%d')
date2=datetime(2017,11,3).strftime('%Y-%m-%d')

#stk_num="000001"
for i in sto2[0:2]:
    stk_num=i[0:6]
    print i
    stock_path1='\\'.join([path_price_volume,market,stk_num])
    stk_list=os.listdir(stock_path1)
    num_in=find_stocks_in_date_range(stock_path1,date1,date2)
    if len(num_in)>0:
        for fi1 in num_in:
            try:
                data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s" % (stk_num,stk_list[fi1])
                #print data_file
                df1=read_vol_price_data(data_file)
                total1=df1.volume.values.tolist() ## pandas value to list
                price1=df1.price.values.tolist()
                vol=[a/b for a, b in zip(total1,price1)]
                print vol[0:4]
            except:
                #print 'fuck'
                pass

