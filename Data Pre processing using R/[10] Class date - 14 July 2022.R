airdata = airquality 
nrow(airdata[complete.cases(airdata),])
colSums(is.na(airdata))
#mean((airdata[,1]), na.rm= T)
airdata[is.na(airdata[,1]),1] = mean(airdata$Ozone, na.rm=T)
airdata
colSums(is.na(airdata[,1:ncol(airdata)]))

for (i in 1:ncol(airdata))
{
  p = sum(is.na(airdata[,i]))/nrow(airdata)
  if (p>0.2)
  {
  airdata[is.na(airdata[,i]),i] = median(airdata$Ozone, na.rm=T)
  }
  else
  {
    airdata[is.na(airdata[,i]),i] = mean(airdata$Ozone, na.rm=T)
  }
}
p = sum(is.na(airdata[,1]))/nrow(airdata)
p
install.packages('VIM')
library('VIM')
airdata= airquality 
airdata = kNN(airdata[,1:2])
airdata
######################################
#multiple imputation by chain equation - every missing value has multiple plausible values 
# in single imputation we are guessing the value so guessing multiple values improves the chances of sucess of a model 
install.packages("mice")
library(mice)
airdata = airquality
sets = mice(airdata)
complete (sets, 1)
#sets uses pmm (predictive mean matching )imputation for multiple imputation 
md.pattern(airquality)
