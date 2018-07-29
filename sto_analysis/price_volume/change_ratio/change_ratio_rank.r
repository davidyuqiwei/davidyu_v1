data_path="/home/qyu/hq185/qyu/data_all/raw_data/stock/change_ratio"
market="shenzhen"
data_path=file.path(data_path,market)
date1='2016-08-10'
file_name1=paste0(market,"_",date1,".csv")
file_name=file.path(data_path,file_name1)

data1=read.csv(file_name)
ord=order(data1[,1])
data1[ord,]
print(tail(data1[ord,],30))















