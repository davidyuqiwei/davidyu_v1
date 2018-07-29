read_stock_data=function(data_path,market,stock_ind,date1){
    data_file=paste0(file.path(data_path,market),'/',stock_ind,"/",stock_ind,'_',date1,".csv")
    if(file.size(data_file)>100&file.exists(data_file)=="TRUE"){
	    data1=read.csv(data_file,skip=1,header=F)
	    time=data1[,1]
        price=data1[,2]
	    vol=(data1[,3]/data1[,2])/100
	    status=data1[,4]
	    data1=data.frame(time=time,volume=vol,price=price,status=status)
    }else{
        data1= -999
    }
    return(data1)
}
