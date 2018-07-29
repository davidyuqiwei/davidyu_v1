#!/usr/bin/Rscript
#******************************************************#
# this script get the buy sale ratio and volume for large volume threshold
# this can be only applied on one threshold
source("G:/stock/path_define.txt")
source("../main.r")
source("../function/buy_sell_ratio.r")
source("../function/read_stock_data.r")

data_path='G:/stock/data/daily_price_volume/shenzhen/000001'
data_path='/home/qyu/hq185/qyu/data_all/raw_data/stock/price_volume/daily_new'
date1='2016-08-23'
#date1=Sys.Date()
#mark1='shanghai'
mark2=c('shanghai','shenzhen')
thres=1000
mark1='shanghai'
stock_ind="600526"
data_file=file.path(data_path,mark1,stock_ind)
dates=list.files(data_file,patter="csv")
date_in=substr(dates,8,17)
n1=which(date_in>'2016-08-23')
len_n1=length(n1)
date_want=20
k=0
par(mfrow=c(4,5))
for(i in 1:len_n1){
#for(i in mark2){
#	market=i
	market="shanghai"
    date1=date_in[n1][i]
    #    save_dir=file.path(save_report_path,market)
    #   dir.create(save_dir)
    #stk_ind1=list.files(file.path(data_path,market))
    data=read_stock_data(data_path,market,stock_ind,date1)
    if(length(data)>1){
        data1=tapply(data$volume,data$price,sum)
        num1=as.numeric(names(data1))
        data2=rep(num1,data1)
        plot(density(data2),main="")
        title(date1)
        k=k+1
    }else{
        next
    }
    if(k==date_want)
        break
}

n1=which(date_in>='2016-08-22')
n1=which(date_in>='2016-08-29')
data_p2=list(1)
data_v2=list(1)
k=0
for(i in 1:len_n1){
#for(i in mark2){
#	market=i
	market="shanghai"
    date1=date_in[n1][i]
    print(date1)
    data=read_stock_data(data_path,market,stock_ind,date1)
    if(length(data)>1){
        data_p2[[i]]=data$price
        data_v2[[i]]=data$volume
        k=k+1
        print(k)
    }else{
        next
    }
    if(k==5)
        break
}
data_p3=unlist(data_p2)
data_v3=unlist(data_v2)
data1=tapply(data_v3,data_p3,sum)
num1=as.numeric(names(data1))
data2=rep(num1,data1)
hist(data2)




close.1=rep(0,date_want)
open.1=rep(0,date_want)
max.1=rep(0,date_want)
min.1=rep(0,date_want)
dates=rep(0,date_want)

kk=0
for(i in 1:len_n1){
	market="shanghai"
    date1=date_in[n1][i]
    data=read_stock_data(data_path,market,stock_ind,date1)
    if(length(data)>1){
        kk=kk+1
        close.1[kk]=data[1,3]
        open.1[kk]=as.numeric(tail(data,1)[3])
        dates[kk]=date1
        max.1[kk]=max(data[,3])
        min.1[kk]=min(data[,3])
    }else{
        next
    }
    if(kk==date_want)
        break
}


x11()
df.1=data.frame(dates,close.1,min.1,max.1,open.1)
plot(df.1[,2],type="b",ylim=c(min(min.1),max(max.1)))
text(1:len_n1,df.1[,2],df.1[,1])
points(min.1,col=2)
points(max.1,col=2)
points(df.1[,5],col=4)


#    len_stk=length(stk_ind1)
#	ratio1=lapply(1:len_stk,function(x)buy_sell_ratio(data_path,market,stk_ind1[x],
#                date1,thres=thres))
#	ratio2=unlist(ratio1)
#	ratio3=t(matrix(ratio2,nrow=3))
#	## get the buy sale ratio
#	#df1=data.frame(round(ratio3,3),stk_ind1)[ord1,]
#    nn1=which(ratio3[,1]>=0&ratio3[,1]<999)
#    ord2=order(ratio3[nn1,2])
#    df2=data.frame(round(ratio3,3)[nn1,],stk_ind1[nn1])[ord2,]
#	file_name=paste0(save_dir,'/',market,'_',thres,"_",date1,".csv")
#	write.csv(df2,file_name)
#}







#buy_sell_ratio=function(i,thres,date1,mark1){
#    #print(i)
#    #data_path='/disk/hq185/qyu/my_work/theme_based/stock_final/download_data/price_volume_daily/data/'
#    stk_ind1=list.files(paste0(data_path,mark1))
#    file1=paste0(data_path,mark1,"/",stk_ind1[i],"/",stk_ind1[i],"_",date1,".csv")
#    if(file.size(file1)>0&file.exists(file1)=="TRUE"){
#        data1=read.csv(file1,header=F,skip=1)
#        volume=(data1[,3]/data1[,2])/100
#        status=data1[,4]
#        time1=1:length(data1[,3])
#        #quan1=quantile(volume,0.9)
#        n1=which(volume>thres&status=="buy")
#        n2=which(volume>thres&status=="sale")
#        len_n1=length(n1)
#        len_n2=length(n2)
#        if(length(n2)==0){
#            big_buy_sell_ratio=-1 ## which there is big sell
#        }else if(length(n2)==0&length(n1)==0){
#            big_buy_sell_ratio=0
#        }else{
#            big_buy_sell_ratio=length(n1)/length(n2)
#        }
#    }else{
#        big_buy_sell_ratio=-999
#        len_n1=-999
#        len_n2=-999
#    }
#    return(list(big_buy_sell_ratio,len_n1,len_n2))
#}







#************************************************************************#




#head(df1,30)
#or1=which(big_buy_sell_ratio>=0)
#big_buy_sell_ratio1=big_buy_sell_ratio[or1]
#ord1=order(big_buy_sell_ratio1)
#df1=data.frame(big_buy_sell_ratio1,stk_ind1[or1])[ord1,]
#
#date1='2016-07-19'

#ord2=order(big_sell_first)
#df2=data.frame(big_sell_first,stk_ind1)[ord2,]
#
#
#for(i in 1:len_stk){
#    file1=paste0(data_path,mark1,"/",stk_ind1[i],"/",stk_ind1[i],"_",date1,".csv")
#    if(file.size(file1)>0){
#        data1=read.csv(file1,header=F,skip=1)
#        volume=data1[,3]/data1[,2]
#        status=data1[,4]
#        n1=which(volume>1000*100&status=="buy")
#        n2=which(volume>1000*100&status=="sale")
#        big_buy[i]=length(n1)
#        big_sell[i]=length(n2)
#    }else{
#        big_buy[i]=0
#    }
#}
#
#
#id='002385'
#date1='2016-07-13'
#ind2=which(stk_ind1==id)
#file1=paste0(data_path,mark1,"/",stk_ind1[ind2],"/",stk_ind1[ind2],"_",date1,".csv")
#data1=read.csv(file1,header=F,skip=1)
#data2=data1[rev(as.numeric(rownames(data1))),]
#plot_t1(data2)
#
#plot_t1=function(data1){
#	time1=1:length(data1[,1])
#	volume=data1[,3]/data1[,2]
#	price=data1[,2]
#	status=data1[,4]
#	par(mfrow=c(2,1))
#	plot(volume)
#	n1=which(status=="buy")
#	points(time1[n1],volume[n1],col=2,pch=16)
#	n2=which(status=="sale")
#	points(time1[n2],volume[n2],col=4,pch=16)
#	plot(data1[,2],type="l")
#	print(stk_ind1[ind2])
#}
#id='002622'
#file1=paste0(data_path,mark1,"/",id,"/",id,"_",date1,".csv")
#data1=read.csv(file1,header=F,skip=1)
#data2=data1[rev(as.numeric(rownames(data1))),]
#plot_t1(data2)
#
#date1='2016-07-12'
#file1=paste0(data_path,mark1,"/",id,"/",id,"_",date1,".csv")
#data1=read.csv(file1,header=F,skip=1)
#data2=data1[rev(as.numeric(rownames(data1))),]
#plot_t1(data2)
#
#his_path='/disk/hq185/qyu/my_work/theme_based/stock_final/download_data/historical_stock/shenzhen'
#his_data=read.csv(paste0(his_path,'/',id,'.sz','/',id,'.sz.csv'))
#
#
#
#
#
#
