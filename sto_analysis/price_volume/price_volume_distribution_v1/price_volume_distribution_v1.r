#source("G:/stock/path_define.txt")
#setwd(main_path)
#source("../main.r")
source("read_stock_data.r")
main_data_path="G:\\stock\\data"
data_path=paste(main_data_path,'daily_price_volume',sep="\\")
print(data_path)
market="shenzhen"
stk_num="000917"
#data_path='/home/qyu/hq185/qyu/data_all/raw_data/stock/price_volume/daily_new'
date1='2017-08-18'
date2='2017-08-18'
#date1=Sys.Date()
#mark1='shanghai'
#data_file=file.path(data_path,market,stk_num)
#data_file="G:\\stock\\data\\daily_price_volume\\shenzhen\\000917"
#print(data_file)
#files=list.files(data_file,pattern="csv")
#print(files)
p_v_disttri=function(data_path,market,stk_num,date1,date2){
	data_file=paste(data_path,market,stk_num,sep="\\")
	files=list.files(data_file,pattern="csv")
	dates=substr(files,8,17)
	n1=which(dates>=date1&dates<=date2)
	# len_n1=length(n1)
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
	df1=as.numeric(as.character(data2[,3]))
	df2=as.numeric(as.character(data2[,2]))
	dd1=tapply(df2,df1,sum)
	return(list(dd1=dd1,df1=df1))
	#barplot(dd1,unique(df1),horiz=TRUE,las=1)
}
print(date1)
data_path=file.path(main_data_path,'daily_price_volume')
market="shanghai"
#market="shenzhen"
stk_num="603103"
#data_path='/home/qyu/hq185/qyu/data_all/raw_data/stock/price_volume/daily_new'
date1='2017-11-03'
#date2='2017-11-03'
date2='2017-11-07'
#date2=date1
a1=p_v_disttri(data_path,market,stk_num,date1,date2)
dd1=a1$dd1
df1=a1$df1
#print(df1)
file_name=paste0(paste(stk_num,date1,date2,sep='_'),'.jpg')
print(file_name)
#jpeg(paste(".\\",file_name,"\\"))
jpeg(file_name,width = 800, height = 800)
	barplot(dd1,unique(df1),horiz=TRUE,las=1)
dev.off()




