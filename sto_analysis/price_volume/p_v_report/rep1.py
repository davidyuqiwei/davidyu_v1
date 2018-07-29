#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import os
from code.path import path
print main_data_path
class parent:
    stock_num=0
    def __init__(self,data_file): ## for read the data
        data1=pd.read_csv(data_file)
        data1.columns=['time','price','volume','status']
        self.data=data1
        parent.stock_num +=1
        print "read 1 data"
    def basic_stat(self,data):
        self.max=np.max(data)
        self.mean=np.mean(data)
        print "the max is :%f" % self.max
        print "the mean is :%f" % self.mean
        return {'max':self.max,'mean':self.mean}
    def howmany(self):
        print parent.stock_num
    def big_vol(self,data,set_vol):
        set_vol1=set_vol*100
        n1=np.where(data>set_vol1)
        #print n1
        len_n1=len(n1[0])
        if len_n1==0:
            len_vol1=0
        return len_n1
'''
class child(parent):
    def basic_stat(self,data):
        self.min=np.min(data)
        print "the min is %f" %self.min
    def vol_stat(self,data):
        self.max=np.max(data)/100
        print "max vol is %f" %self.max
'''


#data_file="g:/stock/data/daily_price_volume/shenzhen/000001/000001_2017-08-10.csv"
d1="daily_price_volume"
data_path=os.path.join(main_data_path,d1)

p=parent(data_file)
#print p.data
vol1=p.big_vol(p.data.volume,3000)
print vol1







#print p
#print p.data.price
#a1=p.basic_stat(p.data.price)
#print a1['max']

#c=child(data_file)
#print c.vol_stat(c.data.volume)
#print c.basic_stat(c.data.volume)


#p.howmany()


#p=parent([1,2,3])
#p.getinfo()

