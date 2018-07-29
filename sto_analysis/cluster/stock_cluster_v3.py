import os
import sys
from package1.download_data.download_daily_price_volume_v2 import *
from package1.path import *
import numpy as np
import pandas as pd
import datetime
from numpy._distributor_init import NUMPY_MKL
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
market='shenzhen'
stock_path=os.path.join(stock_index_path,market)


sto2=os.listdir(stock_path)
#print sto2
date1="2017-09-04"
stk_num=sto2[0][0:6]
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
#print data_file

def data_in_minut(data_file,div_mint):
    data1=pd.read_csv(data_file)
    data2 = data1.iloc[::-1] ## remove the last may have 9:25
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

a2=[]
stock_in=[]
len1=[]
#a4=pd.DataFrame()
#print a4
for i in sto2[0:10]:
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

#print df1
print len(df1)
X=df1
Z = linkage(X, 'ward')
print Z
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

c, coph_dists = cophenet(Z, pdist(X))
print c

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()


'''
kmeans=KMeans(n_clusters=10,random_state=0).fit(X)
print kmeans.labels_
n1=np.where(kmeans.labels_==8)
print n1
c=[stock_in1[i] for i in n1[0]]
print c
#print np.asarray(a2[0])

i=sto2[9]
stk_num='000048'
#print stk_num
data_file="g:/stock/data/daily_price_volume/shenzhen/%s/%s_%s.csv" % (stk_num,stk_num,date1)
a1=data_in_minut(data_file,5)
print len(a1)

'''

#print a1
