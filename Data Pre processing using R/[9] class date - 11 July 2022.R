boxplot(iris$Sepal.Width)
boxplot(iris)
v1= c(1:9)
c1= c(2,3)
which(v1 %in% c1)

outvalues = boxplot(iris$Sepal.Width)$out
indx= which(iris$Sepal.Width %in% outvalues)
iris[indx,]
newiris= iris[-indx,]                                       #remove index position 
boxplot(newiris)
####################################################################
sample(5)
sample(10:15, 20, replace= T)
# without replacement it is essential that number of sample remains between range 
sample(10:15, 4, replace = T)
set.seed(3148)
sample(10:100,10)
rnorm(50,10,2)                  #first value is number of terms, second is mean value and third is sd

set.seed(3147)
x=rnorm(100)                    #rnorm provides random number from normal distribution 
y= rnorm(100)
df= data.frame(x,y)
boxplot(df)
outvalues1 = boxplot(df$x)$out
outvalues2 = boxplot(df$y)$out
ind1= which(df$x %in% outvalues1)
ind1
ind2= which(df$y %in% outvalues2)
ind2
intersect(ind1, ind2)
allo= union(ind1, ind2)
ndf = df[-allo,]
dim(ndf)
boxplot(ndf)                    #still outlier but dont remove it 
udata = unstack(iris,Sepal.Length~Species)
stack(udata)
colMeans(udata) 
d1= 10:30
newd1= cut(d1, c(9,20,25,30),labels= c("low", "mid", "high"))
newd1
print(paste(d1,newd1))
################################################################################
#dealing with missing values
#ignore or delete missing value (list wise deletion (complete row deleted)(complete case analysis), pairwise deletion(ignore missing value cell)(available case analysis))
#impute the missing value

