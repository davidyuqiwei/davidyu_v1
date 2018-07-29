
# coding: utf-8

# In[103]:


# %load fuquan_v1.py

## this cell get the data in the certain time range we are interest
import os
import pandas as pd
from package_path_define.path_define import *
from package_readdata.read_data import find_stocks_in_date_range_fuquan
from package_readdata.read_data import read_vol_price_data_fuquan
from package_plot.plot_data import *
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange
#print path_fuquan
market='shenzhen'
year1=1992
year2=2016

path1='\\'.join([path_fuquan,market])
sto1=os.listdir(path1)
sto2='000898'
#sto2=sto1[10]
#print sto1
stock_full_path='\\'.join([path1,sto2])
print stock_full_path
files=os.listdir(stock_full_path)
file_num_in=find_stocks_in_date_range_fuquan(stock_full_path,year1,year2) #--- find the stock files in the year range we give


def data_get(stock_full_path,files,file_num_in):
    df_m1 = pd.DataFrame() ## create a blank dataframe
    for num_in in file_num_in:
        file_in='\\'.join([stock_full_path,files[num_in]])
        #print file_in
        df1=read_vol_price_data_fuquan(file_in)
        df_m1=df_m1.append(df1,ignore_index=False)
        #print df1.head()
        #print len(df1)
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
    return df_m1
data_df1=data_get(stock_full_path,files,file_num_in)


# In[104]:


#print data_df1
data_df2= data_df1.reset_index(drop=True)  #---- reset the index from 0
#print data_df2.groupby(['year'])['low'].min() # get the  minimum in each groupby
idx=data_df2.groupby(['year'])['low'].transform(min)==data_df2['low']  # get the index of minimum in each groupby
df3=data_df2[idx]
#print df3
#print data_df2.groupby(['year'])['low'].transform(min)
## understand transform
# http://pbpython.com/pandas_transform.html


# In[105]:


# http://matplotlib.org/examples/pylab_examples/date_demo1.html
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange
import matplotlib.pyplot as plt

dates=data_df2.date.values
date1=df3.date.values
fig, ax = plt.subplots( figsize=(20, 8))
ax.plot_date(dates, data_df2.low,'.',linewidth=2)
ax.plot_date(date1, df3.low,'.',color='red',mew=10)
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()

plt.show()
#help(ax.plot_date)


# In[106]:


# # this is superfluous, since the autoscaler should get it right, but
# # use date2num and num2date to convert between dates and floats if
# # you want; both date2num and num2date convert an instance or sequence
# ax.set_xlim(dates[0], dates[-1])

# # The hour locator takes the hour or sequence of hours you want to
# # tick, not the base multiple

# ax.xaxis.set_major_locator(DayLocator())
# ax.xaxis.set_minor_locator(HourLocator(arange(0, 25, 6)))

# ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')

