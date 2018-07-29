import os
import pandas as pd
from package_path_define.path_define import *
from package_readdata.read_data import find_stocks_in_date_range_fuquan
from package_readdata.read_data import read_vol_price_data_fuquan
#print path_fuquan
market='shenzhen'

path1='\\'.join([path_fuquan,market])
sto1=os.listdir(path1)
#print sto1
stock_full_path='\\'.join([path1,sto1[10]])
print stock_full_path
files=os.listdir(stock_full_path)
year1=1992
year2=2016
file_num_in=find_stocks_in_date_range_fuquan(stock_full_path,year1,year2)
#df_m1 = pd.DataFrame({"date":"","open":"","high":"","close":"","low":"","volume":"",\
#        "trade_amount":"","fuquan_factor":""},index=["0"])
#print df_m1
df_m1 = pd.DataFrame()
df_m1
for num_in in file_num_in:
    file_in='\\'.join([stock_full_path,files[num_in]])
    #print file_in
    df1=read_vol_price_data_fuquan(file_in)
    df_m1=df_m1.append(df1,ignore_index=False)
    #print df1.head()
    #print len(df1)
#print df_m1.head()
#print len(df_m1)
date1=df_m1.date.values
years=[]
months=[]
for da in date1:
    year=da[0:4]
    month=da[5:7]
    years.append(int(year))
    months.append(int(month))
df_m1['year']=years
df_m1['month']=months
print df_m1
#print df_m1.head()
#print df_m1.columns.values #--- column names


