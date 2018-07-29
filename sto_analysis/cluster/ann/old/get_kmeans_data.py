# coding: utf-8
# %load stock_in_minut.py
import os
import sys
import numpy as np
import pandas as pd
import datetime
#from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
market='shenzhen'
from load_path import *
from package1.download_data.download_daily_price_volume_v2 import *
from package1.path import *
from data_in_minute import *
from collections import Counter


stock_path=os.path.join(stock_index_path,market)
sto2=os.listdir(stock_path)
#print sto2
date1="2017-09-28"
stk_num=sto2[0][0:6]
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)

def get_kmeans_data(stock_start,stock_end):
    df_in=[]
    stock_in=[]
    len1=[]
    #a4=pd.DataFrame()
    #print a4
    for i in sto2[stock_start:stock_end]:
        stk_num=i[0:6]
        data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
        #print data_file
        try:
            df_in_minut=data_in_minut(data_file,3)
            df_in_minut1=df_in_minut.values.T.tolist()
            df_in.append(df_in_minut1[0])
            stock_in.append(stk_num)
            len1.append(len(df_in_minut))
        except:
            print 'fuck'
    cnt=Counter(len1)  # count the most common elements
    # print cnt
    most_common=cnt.most_common(1)[0][0]  ### find most common length of every data
    matches = zip(*[(i,j) for (i,j) in enumerate(len1) if j ==most_common])  ## find the index which match the most common
    print matches
    #print df_in[0]
    # In[147]:
    match1=matches[0]
    data_norm=[]
    data_raw=[]
    stock_index_match=[]
    for m1 in match1:
        data_norm.append((df_in[m1]-np.mean(df_in[m1]))/np.mean(df_in[m1])) ### normarlized the data
        data_raw.append(df_in[m1])
        stock_index_match.append(stock_in[m1])
    data_norm=np.array(data_norm)
    return [data_raw,data_norm,stock_index_match]

