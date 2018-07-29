
# coding: utf-8

# In[20]:


# %load trend_f1.py

# %load trend_v3.py
import os
import sys
#from load_path import *
import numpy as np
import pandas as pd
import datetime
#from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
import re
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error, r2_score
import itertools
from package_path_define.path_define import *
from package_readdata.read_data import * # load read data function


market='shenzhen'
stock_index_file="shanghai_shenzhen_data_from_2013"
stock_path='\\'.join([main_path_data,stock_index_file,market])
sto2=os.listdir(stock_path)


# define: date and market
market='shenzhen'
date1=datetime(2017,10,30).strftime('%Y-%m-%d')
date2=datetime(2017,11,3).strftime('%Y-%m-%d')

stk_num="000001"
money_size=1000000
big2=[]
sale2=[]
buy2=[]
for i in sto2:
    stk_num=i[0:6]
    print i
    stock_path1='\\'.join([path_price_volume,market,stk_num])
    stk_list=os.listdir(stock_path1)
    num_in=find_stocks_in_date_range(stock_path1,date1,date2)
    if len(num_in)>0:
        big=[]
        sale1=[]
        buy1=[]
        for fi1 in num_in:
            try:
                data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s" % (stk_num,stk_list[fi1])
                #print data_file
                df1=read_vol_price_data(data_file)
                total1=df1.volume.values.tolist() ## pandas value to list
                price1=df1.price.values.tolist()
                vol=[a/b for a, b in zip(total1,price1)]
                big1=len(df1[df1.volume>money_size])
                big.append(big1)    
                df3=df1[df1.volume>money_size]
                sale1.append(len(df3[df3.status=='sale']))
                buy1.append(len(df3[df3.status=='buy']))
                #print df1.head
            except:
                #print 'fuck'
                pass
        big1=np.sum(big)
        sale3=np.sum(sale1)
        buy3=np.sum(buy1)
    else:
        big1=-999
        sale2=-999
        buy2=-999
    big2.append(big1)
    sale2.append(sale3)
    buy2.append(buy3)
    
# print 'total file in the date range ',k,'\n'
# print volume1
print big2
print sale2
# print np.sum(big)



# In[19]:


print buy2


# In[27]:


df2=pd.DataFrame({'stock':sto2,'size':big2,'sale':sale2,'buy':buy2})
print df2.sort_values(by=['buy'], ascending=False)


# In[99]:


for fi1 in num_in:
    try:
        data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s" % (stk_num,stk_list[fi1])
        print data_file
        df1=read_vol_price_data(data_file)
        total1=df1.volume.values.tolist() ## pandas value to list
        price1=df1.price.values.tolist()
        vol=[a/b for a, b in zip(total1,price1)]
        big1=len(df1[df1.volume>money_size])
        big.append(big1)      
        #print df1.head
    except:
        #print 'fuck'
        pass
print big


# In[ ]:



###---------- linear regression input data
p1=list(itertools.chain(*price1)) ##-------------merge multiple list into one
price2 = np.array(p1)
x_input1=np.array(range(0,len(price2)))
x_input=x_input1.reshape(-1, 1)
y_input=price2.reshape(-1, 1)


regr = linear_model.LinearRegression()
regr.fit(x_input,y_input)
trend=regr.coef_
print type(trend)
print 'Coefficients (linear trend): \n', regr.coef_


#print 'coe: \n'
plt.scatter(x_input, y_input,  color='black')
plt.plot(x_input, regr.predict(x_input),color='red', linewidth=4)
#plt.show()


