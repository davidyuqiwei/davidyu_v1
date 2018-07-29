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
#stock_path=os.path.join(stock_index_path,market)
from package_readdata.read_data import *
import matplotlib.pyplot as plt

from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error, r2_score
import itertools



date1=datetime(2017,9,6).strftime('%Y-%m-%d')
date2=datetime(2017,9,6).strftime('%Y-%m-%d')
stk_num="000001"
stock_path1=os.path.join(vol_price_path,market,stk_num)
stk_list=os.listdir(stock_path1)


num_in=find_stock_in_date_range(stk_num,date1,date2)
#print num_in

price1=[]
for fi1 in num_in:
    try:
        data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s" % (stk_num,stk_list[fi1])
        df1=read_vol_price_data(data_file)
        price1=df1.price
        #print df1.head
    except:
        print 'fuck'

#print(__doc__)
###---------- linear regression input data
price2 = np.array(list(itertools.chain(price1)))  ## merge multiple list into one
x_input1=np.array(range(0,len(price2)))
x_input=x_input1.reshape(-1, 1)
y_input=price2.reshape(-1, 1)
regr = linear_model.LinearRegression()
regr.fit(x_input,y_input)
print 'Coefficients: \n', regr.coef_
#print 'coe: \n'


plt.scatter(x_input, y_input,  color='black')
plt.plot(x_input, regr.predict(x_input),color='red', linewidth=4)
plt.show()
'''
#sto2=os.listdir(stock_path)
#stk_num=sto2[0][0:6]
#print sto2
date1="2017-08-10"
date2="2017-09-10"
stk_num="000001"
stock_path1=os.path.join(vol_price_path,market,stk_num)
#print stock_path1
stk_list=os.listdir(stock_path1)
#print stk_list
date_all=[re.split("_|.csv",x)[1] for x in stk_list]
#print date_all
date_all1=[datetime.strptime(x,'%Y-%m-%d') for x in date_all]
#print date_all1
date_all2=np.array([x.strftime('%Y-%m-%d') for x in date_all1])
print date_all2
#date_all2=[datetime.strptime(x,'%Y-%m-%d') for x in date_all1]
date1=datetime(2017,8,10).strftime('%Y-%m-%d')
date2=datetime(2017,9,10).strftime('%Y-%m-%d')
file_in=((date_all2>date1) & (date_all2<date2))
print file_in
num_in=np.where(file_in==True)
print num_in[0]

## the read_vol_price_data  ###
## read the daily download volume price data
## and reverse the rows as well as assign the column name
def read_vol_price_data(data_file):
    data1=pd.read_csv(data_file)
    data2=data1.iloc[::-1]
    #print data2.head
    data2.columns=['time','price','volume','status']
    return data2

for fi1 in num_in[0]:
    try:
        data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s" % (stk_num,stk_list[fi1])
        df1=read_vol_price_data(data_file)
        print df1.head
    except:
        print 'fuck'
#n1=np.where(date_all>=date1)
#print n1
'''

#data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
##print data_file
#
#def data_in_minut(data_file,div_mint):
#    data1=pd.read_csv(data_file)
#    #print data1
#    #print data1.head()
#    data2 = data1.iloc[::-1] ## remove the last may have 9:25
#    data2.columns=['time','price','volume','status']
#    #print data2.head()
#    time1=data2.time
#    a1=pd.to_datetime(time1,format='%H:%M:%S')
#    data2.is_copy=False
#    data2.loc[:,'hour']=pd.Series(a1.dt.hour,index=data2.index)
#    #data2.loc[:,'minute']=pd.Series(a1.dt.minute,index=data2.index)
#    data2.loc[:,'minute']=pd.Series(a1.dt.minute.values/div_mint*div_mint,index=data2.index)
#    #print data2
#    data2=data2.drop(data2[(data2.minute<26)&(data2.hour==9)].index)
#    #print data2
#    #print(a1.dt.minute.values/5*5)
#    #print data2
#    ave_minut1=data2[['price','hour','minute']].groupby(['hour','minute']).mean()
#    #print ave_minut1
#    #ave_minut=ave_minut1[-0:
#    #print ave_minut1.index
#    #ave_minut=ave_minut1.drop(ave_minut1.index[0])
#    ave_minut=ave_minut1
#    #print ave_minut
#    return ave_minut
#
#a2=[]
#stock_in=[]
#len1=[]
##a4=pd.DataFrame()
##print a4
#for i in sto2[0:20]:
#    stk_num=i[0:6]
#    data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
#    try:
#        a1=data_in_minut(data_file,10)
#        print i+'  '+str(len(a1))
#        #print a1
#        a3=a1.values.T.tolist()
#        a2.append(a3[0])
#        stock_in.append(stk_num)
#        len1.append(len(a1))
#    except:
#        print 'fuck'
##print len(sto2)
##max(set(len1),key=len1.count)
#mode1=max(set(len1),key=len1.count)
##print len(len1)
##print len(a2)
##print a2[1]
##print a2[2]
#df1=[]
#k=0
#for ii in a2:
#    if len1[k]==mode1:
#        df1.append(ii)
#    else:
#        pass
#    k+=1
#
#print df1
#
##n1=len1.index(26)
##print n1
#
#X=df1
##print X
#kmeans=KMeans(n_clusters=3,random_state=0).fit(X)
##print kmeans
#print kmeans.labels_
##print kmeans.labels_==1
#print np.where(kmeans.labels_==1)
#
##print np.asarray(a2[0])
#'''
#i=sto2[9]
#stk_num='000048'
##print stk_num
#data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
#a1=data_in_minut(data_file,5)
#print len(a1)
#
#'''
#
##print a1
