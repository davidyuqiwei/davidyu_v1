# coding: utf-8
from package_path_define.path_define import *
import pandas as pd
file1='.\\'.join([path_owner,"morgan_stanley.csv"])
colnames=['stock_name','volume','percentile','A','date']
df1=pd.read_csv(file1,header=None)
df1.columns=colnames
df1['stock_name'] = df1['stock_name'].map(lambda x: x.strip())
#print df1.iloc[0,0]
#df2=df1['stock_name'].str.strip()
#print df2.head()
#df2=df1.iloc[df1.date=="2017-06-30"]
#print df2
#print df1.date.strip()
#a1=[dat1.strip() for dat1 in df1.date]
#print a1
date1="2017-06-30"
date2="2017-09-30"
def have_in_date(date1,date2):
    n1=[]
    for k,dat1 in enumerate(df1.date):
        if dat1==date1:
            n1.append(k)
    #print n1
    n2=[]
    for k,dat1 in enumerate(df1.date):
        if dat1==date2:
            n2.append(k)
    return n1,n2
#print df1.iloc[n1]
#print df1.iloc[n2]
n1,n2=have_in_date(date1,date2)
stk_sr1=df1.iloc[n1]
stk_sr2=df1.iloc[n2]

stk1=stk_sr1.stock_name.tolist()
stk2=stk_sr2.stock_name.tolist()
ret=[ i for i in stk2 if i in stk1 ]  ## both have the stock

## get two file which have same stock but in different date
stk_sr11=stk_sr1.loc[stk_sr1.stock_name.isin(ret)]
stk_sr22=stk_sr2.loc[stk_sr2.stock_name.isin(ret)]
#print stk_sr11
#print '\n\n\n'
#print stk_sr22
print stk_sr11.stock_name
for i in stk_sr11.stock_name:
    print i
    print stk_sr22.percentile[stk_sr22.stock_name==i]
    diff=float(stk_sr22.percentile[stk_sr22.stock_name==i])-float(stk_sr11.percentile[stk_sr11.stock_name==i])
    print diff



#s1=[]
#s2=[]
#i=0
#for r1 in ret:
#    i+=1
#    ifr1.strip()
#
#
#
#
#stock_in=[]
#for r1 in ret:
#    stock_in.append(r1.strip())
#df2=df1[stk_name==stock_in]
##print df2
#
#
#
