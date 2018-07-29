## this script transform the second data of stock into minutes average,
## by given input
import os
import sys
import numpy as np
import pandas as pd
import datetime
def data_in_minut(data_file,div_mint):
    data1=pd.read_csv(data_file)
    data2 = data1.iloc[::-1] ## remove the last may have 9:25
    data2.columns=['time','price','volume','status']
    time1=data2.time
    a1=pd.to_datetime(time1,format='%H:%M:%S')
    data2.is_copy=False
    data2.loc[:,'hour']=pd.Series(a1.dt.hour,index=data2.index)
    data2.loc[:,'minute']=pd.Series(a1.dt.minute.values/div_mint*div_mint,index=data2.index)
    #print data2
    data2=data2.drop(data2[(data2.minute<26)&(data2.hour==9)].index)  ## get data after 9:25 on everyday
    ave_minut1=data2[['price','hour','minute']].groupby(['hour','minute']).mean()
    #print ave_minut1
    return ave_minut1
