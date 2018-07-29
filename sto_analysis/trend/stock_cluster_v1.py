import os
import sys
from package1.download_data.download_daily_price_volume_v2 import *
from package1.path import *
import numpy as np
import pandas as pd
import datetime
from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
market='shenzhen'
stock_path=os.path.join(stock_index_path,market)


sto2=os.listdir(stock_path)
#print sto2
date1="2017-08-10"
stk_num=sto2[0][0:6]
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
#print data_file

def data_in_minut(data_file,div_mint):
    data1=pd.read_csv(data_file)
    #print data1
    #print data1.head()
    data2 = data1.iloc[::-1] ## remove the last may have 9:25
    data2.columns=['time','price','volume','status']
    #print data2.head()
    time1=data2.time
    a1=pd.to_datetime(time1,format='%H:%M:%S')
    data2.is_copy=False
    data2.loc[:,'hour']=pd.Series(a1.dt.hour,index=data2.index)
    #data2.loc[:,'minute']=pd.Series(a1.dt.minute,index=data2.index)
    data2.loc[:,'minute']=pd.Series(a1.dt.minute.values/div_mint*div_mint,index=data2.index)
    #print data2
    data2=data2.drop(data2[(data2.minute<26)&(data2.hour==9)].index)
    #print data2
    #print(a1.dt.minute.values/5*5)
    #print data2
    ave_minut1=data2[['price','hour','minute']].groupby(['hour','minute']).mean()
    #print ave_minut1
    #ave_minut=ave_minut1[-0:
    #print ave_minut1.index
    #ave_minut=ave_minut1.drop(ave_minut1.index[0])
    ave_minut=ave_minut1
    #print ave_minut
    return ave_minut

a2=[]
stock_in=[]
len1=[]
#a4=pd.DataFrame()
#print a4
for i in sto2[0:20]:
    stk_num=i[0:6]
    data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    try:
        a1=data_in_minut(data_file,10)
        print i+'  '+str(len(a1))
        #print a1
        a3=a1.values.T.tolist()
        a2.append(a3[0])
        stock_in.append(stk_num)
        len1.append(len(a1))
    except:
        print 'fuck'
#print len(sto2)
#max(set(len1),key=len1.count)
mode1=max(set(len1),key=len1.count)
#print len(len1)
#print len(a2)
#print a2[1]
#print a2[2]
df1=[]
k=0
for ii in a2:
    if len1[k]==mode1:
        df1.append(ii)
    else:
        pass
    k+=1

print df1

#n1=len1.index(26)
#print n1

X=df1
#print X
kmeans=KMeans(n_clusters=3,random_state=0).fit(X)
#print kmeans
print kmeans.labels_
#print kmeans.labels_==1
print np.where(kmeans.labels_==1)

#print np.asarray(a2[0])
'''
i=sto2[9]
stk_num='000048'
#print stk_num
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
a1=data_in_minut(data_file,5)
print len(a1)

'''

#print a1
