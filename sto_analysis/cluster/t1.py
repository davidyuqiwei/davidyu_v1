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
    data2=data2.drop(data2[(data2.minute<29)&(data2.hour==9)].index)
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
#a4=pd.DataFrame()
#print a4
for i in sto2[0:10]:
    stk_num=i[0:6]
    data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    a1=data_in_minut(data_file,3)
    print len(a1)
    #print a1
    a3=a1.values.T.tolist()
    #print type(a3)
    #print a3
    #a4.loc[:,stk_num]=a1
    #print a1['price']
    #print a3[0]
    a2.append(a3[0])
X=a2
kmeans=KMeans(n_clusters=3,random_state=0).fit(X)
print kmeans
print kmeans.labels_
#print np.asarray(a2[0])
'''
i=sto2[9]
stk_num=i[0:6]
#print stk_num
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
a1=data_in_minut(data_file)
print len(a1)
#print a1
'''
#ind1=a1.index.values
#print a1.index.values[0]
#k=0
#for ind in ind1:
#idx=pd.DataFrame.from_dict(a1,orient='columns').setindex('Date')
#print idx
#print k
#k+=1

#print a4
X=a2
kmeans=KMeans(n_clusters=3,random_state=0).fit(X)
print kmeans
print kmeans.labels_
#print np.array(a2[0])
#print type(a2[0].values)



#print a1.dt.hour
#data2 = data1.iloc[::-1]













#data2=data1.sort_index(axis=0,ascending=True)
#data2= data1.reindex(index=data1.index[::-1])
#print data2.head()


'''
print data1.head()
data2 = data1.iloc[::-1]
#data2=data1
#print data2
data2= data2.reindex(index=data2.index[::-1])
data2=data2.sort_index(axis=0,ascending=True)
data2.columns=['time','price','volume','status']
#data2 = data2.iloc[::-1]

print data2.head()
'''

'''
'''


#print type(data2.time)
#time1=datetime(data2.time)
#print time1
#data1.time






