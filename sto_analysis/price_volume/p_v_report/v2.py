#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
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


class child(parent):
    def basic_stat(self,data):
        self.min=np.min(data)
        print "the min is %f" %self.min
    def vol_stat(self,data):
        self.max=np.max(data)/100
        print "max vol is %f" %self.max
data_file="g:/stock/data/daily_price_volume/shenzhen/000001/000001_2017-08-10.csv"
#data1=pd.read_csv(data_file)
#print data1
#data1.columns=['time','price','volume','status']
#df1=data1.price
#print df1.max()
#p=parent(data_file)
#print p
#print p.data.price
#a1=p.basic_stat(p.data.price)
#print a1['max']

c=child(data_file)
#print c.vol_stat(c.data.volume)
print c.basic_stat(c.data.volume)


#p.howmany()


#p=parent([1,2,3])
#p.getinfo()

