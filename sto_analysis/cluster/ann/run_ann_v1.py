
# coding: utf-8
# %load get_ann_y_v1.py
# %load stock_in_minut.py
import os
import sys
import numpy as np
import pandas as pd
import datetime
#from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
from collections import Counter
from load_path import *
from package1.download_data.download_daily_price_volume_v2 import *
from package1.path import *
from package_ann.functions import *
from data_in_minute import *



## this script first transform the second stock data into minutes we define,
# however, for some stocks, they may not have the same lenght. Hence, we find the
# most common length of the thousands of stocks and keep it. The output have normalized
# data as well as the raw data

## for ANN, the X input is the daily stock time series, the Y input it increase/decrease tommorrow
#vol_price_path
market="shenzhen"
stock_path=os.path.join(stock_index_path,market)
sto2=os.listdir(stock_path)
#print sto2
#date1="2017-09-28"
stk_num=sto2[0][0:6]
#data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)


date1="2017-02-14"
date2="2017-02-15"
df_in1,df_in2=[],[]
stock_in1,stock_in2=[],[]
len1,len2=[],[]
for i in range(0,60):
    j=sto2[i]
    stk_num=j[0:6]
    #data_file1="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    data_file1=vol_price_path+"/"+market+"/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    data_file2=vol_price_path+"/"+market+"/%s/%s_%s.csv" % (stk_num,stk_num,date2)
    #data_file2="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date2)
    try:
        df_in_minut1=get_data(data_file1)
        df_in_minut2=get_data(data_file2)
        if len(df_in_minut1)>0 and len(df_in_minut2)>0:   ## if both day have data we keep the data frame
            df_in1.append(df_in_minut1)
            stock_in1.append(stk_num)
            len1.append(len(df_in_minut1))
            df_in2.append(df_in_minut2)
            stock_in2.append(stk_num)
            len2.append(len(df_in_minut2))
    except:
        print 'fuck'

data_raw1,data_norm1,stock_index_match1,data_raw2,data_norm2,stock_index_match2=dele_not_match_transform(len1,df_in1,stock_in1,len2,df_in2,stock_in2)

from sklearn.neural_network import MLPClassifier
import random

X=data_raw1
today_max=[np.max(x) for x in data_raw2]
yest_mean=[np.max(x) for x in data_raw1]
diff=map(lambda(a,b):a-b,zip(today_max,yest_mean))

diff_ch=[]
for diff1 in diff:
    if diff1>0:
        diff_ch.append(1)
    else:
        diff_ch.append(-1)


len_ann=len(X)
samp=random.sample(xrange(0,len_ann),int(len_ann*0.8))
pred=[i for i in xrange(0,len_ann) if i not in samp]
y=diff_ch
x_samp=[]
y_samp=[]
for samp1 in samp:
    x_samp.append(X[samp1])
    y_samp.append(y[samp1])


clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(60,10), random_state=1)
clf.fit(x_samp, y_samp)

totl=0
correct=0
for i in pred:
    dif=clf.predict([X[i]])-y[i]
    totl+=1
    if dif==0:
        correct+=1
    #print 'predict: ',clf.predict([X[i]]), 'observe:', y[i]
print 'corret percentage: ',round(float(correct)/float(totl),4)





