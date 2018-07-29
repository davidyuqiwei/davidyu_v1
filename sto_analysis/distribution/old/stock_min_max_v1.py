import os
import sys
#from package_download_data.download_daily_price_volume_v2 import *
from package_path_define import *
import numpy as np
import pandas as pd
import datetime
#from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt
market='shenzhen'
stock_path=os.path.join(stock_index_path,market)


#print data_file

def read_stk_data(data_file):
    #print data_file
    data1=pd.read_csv(data_file)
    data2 = data1.iloc[::-1] ## reverse the dataframe
    #print data2
    data2.columns=['time','price','volume','status']
    #print data2.head()
    return data2
def data_in_minut(data_file,div_mint):
    data1=pd.read_csv(data_file)
    data2 = data1.iloc[::-1] ## reverse the dataframe
    #print data2
    data2.columns=['time','price','volume','status']
    time1=data2.time
    a1=pd.to_datetime(time1,format='%H:%M:%S')
    data2.is_copy=False
    data2.loc[:,'hour']=pd.Series(a1.dt.hour,index=data2.index)
    data2.loc[:,'minute']=pd.Series(a1.dt.minute.values/div_mint*div_mint,index=data2.index)
    data2=data2.drop(data2[(data2.minute<26)&(data2.hour==9)].index)
    ave_minut1=data2[['price','hour','minute']].groupby(['hour','minute']).mean()
    ave_minut=ave_minut1
    return ave_minut

sto2=os.listdir(stock_path)
#print sto2
#date1="2017-09-04"
#date2="2017-09-04"


#print date1


#stk_num=sto2[0][0:6]
def max_min(stk_num,date1,date2):
    data_file1="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    data_file2="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date2)
    #data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    df1=read_stk_data(data_file1)
    df2=df1.price.T.tolist()
    fd_min=np.min(df2)
    fd_max=np.max(df2)
    #print np.min(a1)
    #print np.max(a1)
    df3=read_stk_data(data_file2)
    df4=df3.price.T.tolist()
    sd_min=np.min(df4)
    sd_max=np.max(df4)
    return sd_max-fd_min


date1=datetime.date(2017,8,1)
date2=date1+datetime.timedelta(2)
diff2=[]
for s1 in sto2[0:3]:
    stk_num=s1[0:6]
    try:
        diff1=max_min(stk_num,date1,date2)
        diff2.append(diff1)
    except:
        pass
print np.min(diff2)
print type(diff2)
print [i for i in diff2 if i<0]
#plt.plot(diff2)
#plt.show()


'''
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date2)

#data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
df1=read_stk_data(data_file)
a1=df1.price.T.tolist()
print np.min(a1)
print np.max(a1)

'''



'''
fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.plot(a1)
ax2.hist(a1,12)
plt.show()
'''





#print np.min(a1)
'''
a2=[]
stock_in=[]
len1=[]
#a4=pd.DataFrame()
#print a4
#for i in sto2[0:10]:
for i in sto2[0:200]:
    stk_num=i[0:6]
    data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
    try:
        a1=data_in_minut(data_file,3)
        print i+'  '+str(len(a1))
        #print a1
        a3=a1.values.T.tolist()
        a2.append(a3[0])
        stock_in.append(stk_num)
        len1.append(len(a1))
    except:
        print 'fuck'
mode1=max(set(len1),key=len1.count)

df1=[]
k=0
stock_in1=[]
for ii in a2:
    if len1[k]==mode1:
        df1.append(ii)
        stock_in1.append(stock_in[k])
    else:
        pass
    k+=1

#print pd.DataFrame(df1)
df2=pd.DataFrame(df1)
stk_row=pd.DataFrame(stock_in1)
#print df2
df2.to_csv('data.csv',index=False)
stk_row.to_csv('rowname.csv',index=False)

'''


