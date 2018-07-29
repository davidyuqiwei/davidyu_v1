data=read.csv("data.csv")
rowname1=read.csv("rowname.csv",colClasses="character")
data1=t(apply(data,1,function(x)(x-mean(x))/sd(x)))
rownames(data1)=as.character(unlist(rowname1))
#data1=data
#data3=as.matrix(data)
cor(t(data1))
hc=hclust(dist(data1))
plot(hc)

clusterCut <- cutree(hc, 8)
clu_df=data.frame(rowname1,clusterCut)
print(clu_df)


data3=as.matrix(data)
par(mfrow=c(2,1))
plot(data3[1,])
plot(data3[169,])




