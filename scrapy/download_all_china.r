#!/usr/bin/Rscript
library(XML)
setwd("F:/crontab_get_data/air_quality")
#save_dir="~/scratch/aqi_china/"
save_dir="F:/crontab_get_data/air_quality/"
url="http://www.pm25.in/"

t<-Sys.time()
time1=substr(t,1,13)
time2=gsub(" ","_",time1)
link1=getHTMLLinks(url)
# check out the link1 which is the city
# length 386
for(i in 8:386){
	city=substring(link1[i],2)
	#print(city)
	dir.create(paste0(save_dir,city), showWarnings = TRUE)
	url2=paste0(url,city)
    doc = htmlParse(url2, encoding = "UTF-8")
	a1=xpathSApply(doc,"//*/div[@class='live_data_time']")
    a2=xmlToList(a1[[1]])$p
    date=substring(a2,8)
    table=readHTMLTable(doc, header=T, stringsAsFactors=F)[[1]]
	table_name=names(table)
	rows=length(table[[1]])
	d1=data.frame(matrix(unlist(table),nrow=rows))
	d1=data.frame(rep(date,rows),d1)
    colnames(d1)=c("date",table_name)
	#con<-file(paste0(save_dir,city,'/',city,'.txt'),encoding="utf8")
	con=paste0(city,'/',city,'_',time2,'.txt')
	#con=paste0(save_dir,city,'/',city,'.txt')
	#write.table(d1,file=con,row.names=F,append=T,fileEncoding="utf8")
	write.table(d1,file=con,row.names=F,fileEncoding="utf8",append=T,col.names=F)
	Sys.sleep(3)
}


#print(link1)

# a1=htmlParse(url)
# print(a1)
#pm2 <-fromJSON(pm);
#pm3=data.frame(do.call("rbind",pm2))
#pm4=apply(pm3,2,as.character); 
#dt=gsub("-","",substr(pm4[1,21],1,13))
#con<-file('china_test.csv',encoding="utf8")
#write.csv(pm4,file=con)




