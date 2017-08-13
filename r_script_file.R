library(quantmod)
setwd("/home/carpentr/HomeWork/Bitcoin/crypto-data/data")
csvfiles=list.files(pattern="*.csv")
agg_df=data.frame(idx=c(1:2001))
for (file in csvfiles){
  tmp_df=read.csv(file)
  agg_df=cbind(agg_df,tmp_df['volumefrom'])
}
agg_df=agg_df[,-1] 
colnames(agg_df) = unlist(lapply(csvfiles, function(x){strsplit(x, '.', fixed=TRUE)[[1]][1]}))
head(agg_df)
rets=scale(agg_df)
#rets=apply(agg_df,MARGIN = 2,ROC)
#rets[is.na(rets)]=0
#rets[is.infinite(rets)]=0


#SVD analysis
decomp=svd(as.matrix(rets))
plot(x=1:2001,decomp$u[,1],type='l')
lines(decomp$u[,2],col='red')
ret_mat=as.matrix(rets)
U=decomp$u
dim(U)
bob=t(U)%*%ret_mat
dim(ret_mat)
svd1=decomp$u[,1]
svd2=decomp$u[,2]
svd1%*%as.matrix(rets)
svd2%*%as.matrix(rets)
decomp$d
cor(rets)
cor(rets[1700:2001,])

