v1= c(4,7,45,34,67,87,9,35,3,2,10)
sort(v1)
sort(v1, decreasing= T)
order(v1)                              #returns the index position of ascensing order of orignal data 
rank (v1)                              # rank1 given to lowest val
rank (-v1)
v2 = c(45,56,NA,34,56,78,98,NA,45)
mean (v2)
mean (v2, na.rm= T)                    #Ignore missing value in v2
sum(v2)
is.na(v2)                              #gives true for NA value in dataset

v2[!is.na(v2)]                         #Extract data and remove NA values

sum(is.na(v2))                         # gives number of missing value as true has num val of 1

View(airquality)
mean(airquality$Ozone, na.rm=T)
colMeans(airquality, na.rm= T)
colSums(is.na(airquality))

complete.cases(airquality)
subset(airquality, complete.cases(airquality)==T)  #Extract comletely filled values
airquality[complete.cases(airquality),]       
subset(airquality, complete.cases(airquality)==F)
###########################################################
height = c(164,167,168,189,166,178,190,188,156,166)
weight= c(45,67,89,55,77,65,74,55,66,79)
salary =c(1324,4565,5678,6784,4556,7984,6834,6785,1234,5676)

mylist= list(height, weight, salary)
mylist
mean(mylist[[1]])
mean(mylist[[2]])
mean(mylist[[3]])

lapply(mylist, mean)
lapply(iris[1:4], mean)
lapply(airquality, mean, na.rm=T)
sapply(mylist, mean)
tapply(mylist, mean)                       # can only be applied to 2 dimeansional value = it splits first paramenter based on second parameter and apply 3rd operation 
m1 = matrix(11:19,3)
m1
apply(m1,1,mean)
apply(m1,2,mean)
mean(m1[1,])
apply(m1,1,mean)    
apply(m1,1, mean)

rowMeans(m1)
colMeans(m1)
apply(iris[1:4],2, mean)
##########################################################
View(iris)
s1= subset(iris, Species=="setosa" )
colMeans(s1[1:4])
tapply(c(iris$Sepal.Length,iris$Sepal.Width,iris$Petal.Length,iris$Petal.Width), iris$Species, mean)

for (i in 1:4)
{
  print(colnames(iris)[i])
  print(tapply(iris[,i], iris$Species, mean))
  
}

iris[,1:2]
iris[1:2]
aggregate(iris[1:4], list(iris$Species), mean)
aggregate(Sepal.Length~Petal.Width,iris, mean)             #~for splitting parameterv1= c(4,7,45,34,67,87,9,35,3,2,10)
sort(v1)
sort(v1, decreasing= T)
order(v1)                              #returns the index position of ascensing order of orignal data 
rank (v1)                              # rank1 given to lowest val
rank (-v1)
v2 = c(45,56,NA,34,56,78,98,NA,45)
mean (v2)
mean (v2, na.rm= T)                    #Ignore missing value in v2
sum(v2)
is.na(v2)                              #gives true for NA value in dataset

v2[!is.na(v2)]                         #Extract data and remove NA values

sum(is.na(v2))                         # gives number of missing value as true has num val of 1

View(airquality)
mean(airquality$Ozone, na.rm=T)
colMeans(airquality, na.rm= T)
colSums(is.na(airquality))

complete.cases(airquality)
subset(airquality, complete.cases(airquality)==T)  #Extract comletely filled values
airquality[complete.cases(airquality),]       
subset(airquality, complete.cases(airquality)==F)
###########################################################
height = c(164,167,168,189,166,178,190,188,156,166)
weight= c(45,67,89,55,77,65,74,55,66,79)
salary =c(1324,4565,5678,6784,4556,7984,6834,6785,1234,5676)

mylist= list(height, weight, salary)
mylist
mean(mylist[[1]])
mean(mylist[[2]])
mean(mylist[[3]])

lapply(mylist, mean)
lapply(iris[1:4], mean)
lapply(airquality, mean, na.rm=T)
sapply(mylist, mean)
tapply(mylist, mean)                       # can only be applied to 2 dimeansional value = it splits first paramenter based on second parameter and apply 3rd operation 
m1 = matrix(11:19,3)
m1
apply(m1,1,mean)
apply(m1,2,mean)
mean(m1[1,])
apply(m1,1,mean)    
apply(m1,1, mean)

rowMeans(m1)
colMeans(m1)
 apply(iris[1:4],2, mean)
 ##########################################################
 View(iris)
 s1= subset(iris, Species=="setosa" )
 colMeans(s1[1:4])
tapply(c(iris$Sepal.Length,iris$Sepal.Width,iris$Petal.Length,iris$Petal.Width), iris$Species, mean)

for (i in 1:4)
{
  print(colnames(iris)[i])
  print(tapply(iris[,i], iris$Species, mean))

}

iris[,1:2]
iris[1:2]
aggregate(iris[1:4], list(iris$Species), mean)
aggregate(Sepal.Length~Petal.Width,iris, mean)             #~for splitting parameter
View(iris)
