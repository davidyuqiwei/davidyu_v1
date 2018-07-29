from package_path_define.path_define import *
import pandas as pd
# coding: utf-8
file1='.\\'.join([path_owner,"morgan_stanley_tr.csv"])

colnames=['stock_name','volume','percentile','A','date']
df1=pd.read_csv(file1)
df1.columns=colnames
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
stk1=df1.iloc[n1,0]
stk2=df1.iloc[n2,0]
stk1=stk1.tolist()
stk2=stk2.tolist()
ret=[ i for i in stk2 if i not in stk1 ]
for r1 in ret:
    print r1



