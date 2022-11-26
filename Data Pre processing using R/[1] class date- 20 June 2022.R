#maths operation
5+5
45+89
a=10
b=10
c=a+b
print(c)
33%/%9     #Integer Division
33%%9      #modular Division
###############################
#vector
weight = c(45,67,89,55,66,87,79,56,45,55)
length (weight)
sum (weight)
mean (weight)
sd(weight)
var(weight)
sd(weight)^2
range(weight)
exp(weight)                     
sqrt(weight)
log(weight)           #return natural log
log2(20)              #return log base 2
#################################
#Matrix
25:100
v1= c(1,2,3,4)
m1= matrix(v1,2,2)
m1
m2= matrix(c(1,2,3,4,5,6,7,8,9),3)                  #here number of elements and rows are mentioned so columns are not essential
m3= matrix(c(11,12,13,14,15,16), ncol=3)
m3
m4= matrix(c(11,12,13,14,15,16), ncol=3, byrow=T)   #rows filled first #TRUE=T
m4
v2= c(10,20,30)
v3= c(1,2,3)
rbind(v2,v3)
cbind(v2,v3)
m5=matrix(c(10,20,30,40),2,2)
rownames(m5)= c("row1", "row2")
colnames(m5)= c("col1", "col2")
m5
colSums(m5)
rowSums(m5)
nrow(m5)
ncol(m5)
m6= matrix(c(1,2,3,4),2,2)
m7= matrix(c(10,11,12,13),2,2)
m7+m6
m7*m6
m6*m7          #element multiplication
m7%*%m6        #Proper Multiplication
########################
#Data Frame
empno=c(1,2,3,4,5)
empname= c("aa","bb","cc","dd","ee")
empsal= c(3452,4566,3455,5677,2344)
empdata= data.frame(empno,empname,empsal)
empdata
str (empdata)




















v1= c(1,2,3,4,"Anil",5)        #if there is a single character in numeric string the string will be classified as character
as.numeric(v1)                 # Error as d cannot be converted and it substitutes NA
class(v1)                      # reason its categorized as character is because anil cannot be converted to numeric value
v2=c(1,2,3,4,5)
class (v2)
v3= c(1,2,3,4,T,5)
class (v3)
v4= c(T,T, "Anil")
as.logical(v4)
v5= c(-1,-2,0,T,F)             
as.logical(v5)
v9= c(5,x)
v9
ls()
v8= c(1.2,2.3,5,7,0)
v9= c(1,2,3,4,6)
v8+v9


