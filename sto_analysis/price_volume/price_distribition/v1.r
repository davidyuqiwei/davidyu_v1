source("G:/stock/code/path_define.txt")
setwd(main_path)
#source("../main.r")
source("./function/buy_sell_ratio.r")
source("./function/read_stock_data.r")

data_path='G:/stock/data/daily_price_volume'
market="shenzhen"
stk_numbers=list.files(file.path(data_path,market))
stk_num="000001"
#data_path='/home/qyu/hq185/qyu/data_all/raw_data/stock/price_volume/daily_new'
date1='2017-09-04'
date2='2017-09-04'
#date1=Sys.Date()
#mark1='shanghai'


data_file=file.path(data_path,market,stk_num)
files=list.files(data_file,pattern="csv")
dates=substr(files,8,17)
n1=which(dates>=date1&dates<=date2)
len_n1=length(n1)

data=list(1)
k=0
for(i in n1){
#for(i in mark2){
#	market=i
    date1=dates[i]
    #    save_dir=file.path(save_report_path,market)
    #   dir.create(save_dir)
    #stk_ind1=list.files(file.path(data_path,market))
    data1=read_stock_data(data_path,market,stk_num,date1)
    if(length(data1)>1){
    	k=k+1
    	data2=data.frame(apply(data1,2,rev))
    	data[[k]]=data2
    }
}

df1=do.call('rbind', data)
par(mfrow=c(2,1))
plot(as.numeric(as.character(df1[,3])))
hist(as.numeric(as.character(df1[,3])))

# mark2=c('shanghai','shenzhen')
# thres=1000
# mark1='shanghai'
# stock_ind="600526"
# data_file=file.path(data_path,mark1,stock_ind)
# dates=list.files(data_file,patter="csv")
# date_in=substr(dates,8,17)
# n1=which(date_in>'2016-08-23')
# len_n1=length(n1)
# date_want=20
# k=0
# par(mfrow=c(4,5))