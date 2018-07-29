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

## this function get the dataframe in minute
def get_data(data_file):
    #data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    df_in_minut=data_in_minut(data_file,3)
    df_in_minut1=df_in_minut.values.T.tolist()
    return df_in_minut1[0]

def get_data2(df_in,stock_in,match1):
    data_norm=[]
    data_raw=[]
    stock_index_match=[]
    for m1 in match1:
        data_norm.append((df_in[m1]-np.mean(df_in[m1]))/np.mean(df_in[m1])) ### normarlized the data
        data_raw.append(df_in[m1])
        stock_index_match.append(stock_in[m1])
    data_norm=np.array(data_norm)
    return [data_raw,data_norm,stock_index_match]

def dele_not_match_transform(len1,df_in1,stock_in1,len2,df_in2,stock_in2):
    cnt=Counter(len1)  # count the most common elements
    # print cnt
    most_common=cnt.most_common(1)[0][0]  ### find most common length of every data
    matches1= zip(*[(i,j) for (i,j) in enumerate(len1) if j ==most_common])  ## find the index which match the most common
    matches2= zip(*[(i,j) for (i,j) in enumerate(len2) if j ==most_common])  ## find the index which match the most common
    #print matches
    #print df_in[0]
    match1=list((set(matches1[0]) & set(matches2[0])))
    data_raw1,data_norm1,stock_index_match1=get_data2(df_in1,stock_in1,match1)
    data_raw2,data_norm2,stock_index_match2=get_data2(df_in2,stock_in2,match1)
    return [data_raw1,data_norm1,stock_index_match1,data_raw2,data_norm2,stock_index_match2]

date1="2017-09-28"
date2="2017-09-29"
df_in1,df_in2=[],[]
stock_in1,stock_in2=[],[]
len1,len2=[],[]
for i in range(0,1000):
    j=sto2[i]
    stk_num=j[0:6]
    data_file1="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    data_file2="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date2)
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

from sklearn.neural_network import MLPClassifier
import random
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
                    hidden_layer_sizes=(10, 6), random_state=1)
clf.fit(x_samp, y_samp)
totl=0
corret=0
for i in pred:
    dif=clf.predict([X[i]])-y[i]
    totl+=1
    if dif==0:
        corret+=1
    print 'predict: ',clf.predict([X[i]]), 'observe:', y[i]
print 'corret percentage: ' dif/totl

#clf.fit(x_samp, y_samp)
#clf.predict([X[71]])
#y[71]
