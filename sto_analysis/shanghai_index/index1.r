setwd("G:/stock/data/shanghai_shenzhen_index")
df1=read.csv("shanghai_index_1991-01-01_2017-11-21.csv")

df1=df1[complete.cases(df1),]

close1=df1[,5]
vol=df1[,6]


n1=which(vol>0&vol<10000000)

df2=df1[n1,]
year1=substr(df2[,1],1,4)
month1=substr(df2[,1],6,7)


n1=which(year1>=2012&year1<=2016)
vol=df2[n1,6]
close1=df2[n1,5]

vol2=tapply(vol,list(year1[n1],month1[n1]),function(x)mean(x,na.rm=T))

ser = ts(c(t(vol2)), freq=12, start = c(2004, 1))
fit = stl(ser, s.window="periodic")
plot(fit)
sea1=fit$time.series[,1]
vol2=tapply(close1,list(year1[n1],month1[n1]),function(x)mean(x,na.rm=T))
ser = ts(c(t(vol2)), freq=12, start = c(2004, 1))
fit = stl(ser, s.window="periodic")
plot(fit)


sea2=fit$time.series[,1]




setwd("G:/stock/data/owner")
a1=read.csv("zhongyanghuijin_tr.csv",head=F)

n1=which(as.numeric(as.character(a1[,2]))>0)
a2=a1[n1,]
sort(table(a2[,1]))

date1=as.character(a2[,5])
stock_name=as.character(a2[,1])
stk1=stock_name[date1>"2017-08-30"]

l1=lapply(stk1,function(x)which(stock_name==x))
l2=lapply(l1,function(x)length(x))

stk1[which(unlist(l2)==1)]

vol1=vol[n1]
plot(vol1,close1[n1])
cl2=close1[n1]


n <- length(cl2);
lrest <- log(cl2[-1]/cl2[-n])
plot(vol1[-1],lrest)



vol2=vol1[-which(vol1>10000000)]





close2=tapply(close1,list(year1,month1),function(x)mean(x,na.rm=T))


return1=diff(log(close1))
re2=return1[2000:length(return1)]
plot(re2)
hist(re2)
# rownames(close2)=c(1991:2017)
# colnames(close2)=c("Jan","Feb","Mar",  "Apr",  "May",  "Jun" , "Jul",  "Aug" , "Sep" , "Oct", "Nov", "Dec")


close3=c(t(close2))
close3[length(close3)]=4000

ser = ts(c(close3), freq=12, start = c(1991, 1))



fit = stl(ser, s.window="periodic")
plot(fit)