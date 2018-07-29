#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
class parent:
    stock_num=0
    def __init__(self,data_file): ## for read the data
        data1=pd.read_csv(data_file)
        data1.columns=['time','price','volume','status']
        self.price=data1.price
        parent.stock_num +=1
        print "read 1 data"
    def basic_stat(self):
        self.max=np.max(self.price)
        self.mean=np.mean(self.price)
        print "the max is :%f" % self.max
        print "the mean is :%f" % self.mean
    def howmany(self):
        print parent.stock_num

data_file="g:/stock/data/daily_price_volume/shenzhen/000001/000001_2017-08-10.csv"
#data1=pd.read_csv(data_file)
#print data1
#data1.columns=['time','price','volume','status']
#df1=data1.price
#print df1.max()
p=parent(data_file)
p.basic_stat()
p.howmany()
#p=parent([1,2,3])
#p.getinfo()

