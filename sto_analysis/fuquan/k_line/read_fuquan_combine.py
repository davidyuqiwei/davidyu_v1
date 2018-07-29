
# coding: utf-8

### this script read fuquan combine data

from package_path_define.path_define import *
# from package_readdata.read_data import find_stocks_in_date_range_fuquan
from package_readdata.read_data import read_vol_price_data_fuquan

# market='shenzhen'
# path1='\\'.join([main_path_data,'fuquan_combine',market])




def read_fuquan_combine(stk_num):
    if stk_num.startswith('00'):
        market='shenzhen'
    elif stk_num.startswith('60'):
        market='shanghai'
    ### find which market and get the path
    path1='\\'.join([main_path_data,'fuquan_combine',market])
    ### set the file full path
    file_in1='%s_fuquan_all.csv' %stk_num
    file_in='\\'.join([path1,file_in1])
    print file_in
    try:
        df1=read_vol_price_data_fuquan(file_in)
        #df2=data_df1
        df2=df1.sort_values(by=['date'])
        data_df1=df2.reset_index(drop=True)
        return data_df1
    except Exception,e:
        #pass
        print Exception,":",e



