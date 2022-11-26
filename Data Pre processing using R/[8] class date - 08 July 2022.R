# Normalization characteristics 
hist(trees$Volume, prob=T)                                            #histogram plot to check normal dist
curve(dnorm(x, mean=mean(trees$Volume),sd=sd(trees$Volume)), add=T)   

hist(trees$Height, prob=T)
curve(dnorm(x, mean=mean(trees$Height),sd=sd(trees$Height)), add=T)

shapiro.test(trees$Height)


hist(trees$Girth, prob=T)
curve(dnorm(x, mean=mean(trees$Girth),sd=sd(trees$Girth)), add=T)

shapiro.test(trees$Girth)

qqnorm(trees$Girth)
qqline(trees$Girth)
#log transformation  and square root transfromation is helpful for reducing right/positive skewness
#power transformation for negative skewed data
 
weight= c(15,20,20,25,25, 35, 45,45,45,40, 45, 50,55,50, 55,55,55,55,60,60,60,60,60)
hist(weight, prob=T)
curve(dnorm(x, mean=mean(weight),sd=sd(weight)), add=T) 


lweight= log(weight)
hist(lweight, prob=T)
curve(dnorm(x, mean=mean(lweight),sd=sd(lweight)), add=T) 

pweight= log(weight^3)
hist(pweight, prob=T)
curve(dnorm(x, mean=mean(pweight),sd=sd(pweight)), add=T) 

#data scaling - standardizing data 
# bringing all variables on same scale
# min max data 
#v1- iris$Sepal.Length
#s = max(trees$Height)
#c= as.character(s)
#s= strsplit(c, split, fixed=T)
#use nchar()
Name = c("a","b", "c","d","e")
Height= c(170, 167, 168, 160,172)
weight= c(65, 64, 67, 25,67)
salary= c(34000,23000,63000,33000, 32500)
df= data.frame(Name, Height, weight, salary)
df

