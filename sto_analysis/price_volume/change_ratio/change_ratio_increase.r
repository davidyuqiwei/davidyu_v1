data_path="/home/qyu/hq185/qyu/data_all/raw_data/stock/change_ratio"
market="shenzhen"
data_path=file.path(data_path,market)
date1='2016-08-11'

file_name1=paste0(market,"_",date1,".csv")
file_name=file.path(data_path,file_name1)
change_ratio1=read.csv(file_name)

stock_price_path='/home/qyu/hq185/qyu/data_all/raw_data/stock/price_volume/daily_new'
stock_path1=file.path(stock_price_path,market)
files=list.files(stock_path1)
len1=length(files)
stock_ratio=rep(-999,len1)
for(i in 1:len1){
	#i=2
	data_path=file.path(stock_path1,files[i])
	data_file=paste0(data_path,'/',files[i],'_',date1,'.csv')
	date2=as.Date(date1)-1
	data_file2=paste0(data_path,'/',files[i],'_',date2,'.csv')
	try1=try(read.csv(data_file,skip=1,header=F),silent = TRUE)
	try2=try(read.csv(data_file2,skip=1,header=F),silent = TRUE)
    if ('try-error' %in% class(try1)|'try-error' %in% class(try2)){
        next
    }else{
        data1=read.csv(data_file,skip=1,header=F,nrows=1)
	    data2=read.csv(data_file2,skip=1,header=F,nrows=1)	
	    stock_ratio[i]=(data1[1,2]-data2[1,2])/data2[1,2]
    }
}

n1=which(stock_ratio>=-967)
inte_stock=intersect(change_ratio1[,3],as.numeric(files[n1]))
change_ratio_n1=which(change_ratio1[,3]%in%inte_stock)
stock_change_n1=which(as.numeric(files[n1])%in%inte_stock)
aa1=change_ratio1[change_ratio_n1,]
aa2=stock_ratio[n1][stock_change_n1]
aa3=data.frame(aa1,aa2)
plot(aa3[,1],aa3[,4])








