data = read.csv("C:/Test_route/Store and Regional Sales Database.csv")
View(data)
summedb= tapply(data$Total.Business, data$Store.No., sum) 
max(summedb)
summeda= tapply(data$Total.Business, data$Item.Description, sum)
summeda
max(summeda)
##################################################################
for (i in 1:4)
{print(mean(iris[,i]))
       }
  
s= split(iris, iris$Species)
typeof(s)
templist= (split(iris, iris$Species))
colMeans(templist[[1]][1:4])
for (i in 1:3)
{
  print(colMeans(templist[[i]][1:4]))
}

for (i in 1:length(iris))
{
  if (class(iris[,i])=="numeric")
    print (mean(iris[,i]))
}
for (i in 1:length(iris))
{
  if (class(iris[,i])=="factor")
    print(table(iris[,i]))
}

write.csv(iris, "C:/Test_route/iris.csv")
