empno=c(1,2,3,4,5)
empname= c("aa","bb","cc","dd","ee")
empsal= c(3452,4566,3455,5677,2344)
empdata= data.frame(empno,empname,empsal)
empdata
str (empdata)
dim (empdata)
nrow (empdata)
ncol (empdata) 
colnames(empdata)
head(empdata, 2)
tail (empdata, 2)
summary (empdata)
#####################################
stdata= data.frame()
fix(stdata)                                       #creates grid for stdataframe
stdata
######################################
weight= c(45,67,89,55,66,87,79,56,45,55)
summary(weight)
quantile(weight,probs= c(0.6,0.7))
IQR(weight)                                       #gives data of between 50%tile

########################################
#list
v1=c(10,12,34,56,78)
m1= matrix(1:9, 3,3)
empdata
mylist= list(v1,m1,empdata)
mylist[[3]]                                       #always use [[]]
weight[4:6]
weight[c(4:6,9)]                                  #for extracting element with gaps between them
weight[weight>60 & weight<70]
weight[weight>60 | weight<70]
weight[-c(5,6)]                                   #remove element 5 and 6 

########################################
iris
View(iris)
dim(iris)
head(iris[c(1,3,5)])
head(iris[c("Sepal.Length", "Petal.Length", "Species")])
iris[5:10,c(1,3,5)]
vdata= subset(iris, Species=="setosa")                   #extracting particular value 
vdata
subset(iris, Species=="setosa", select=c(1,3,5))
nrow(subset(iris,Sepal.Length>5.5 & Petal.Length>2.5))
nrow(subset(iris, Species=="setosa"| Species=="versicolor"))
(subset(iris, Species %in% c("setosa","versicolor")))
(subset(iris, Species!= "virginica"))
unique(iris$Species)
table(iris$Species)
sum(iris$Sepal.Length)
colMeans(iris[1:4])
sum(vdata$Sepal.Length)
mean(vdata$Sepal.Length)
colMeans(subset(iris,Species=="setosa", select = c(1,2)))      
         
m1= matrix(1:9,3)
m1
m1[c(1,2), c(2,3)]         # calling specific rows and columns from matrix 
m1[c(1,3),c(1,3)]
rowSums(m1)