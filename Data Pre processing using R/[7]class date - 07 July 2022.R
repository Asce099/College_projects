#chisquare test of association 
empdata= read.csv("C:/Test_route/employee data - employee data.csv")
View(empdata)
t1= table(empdata$job.category, empdata$Does.employee.belongs.to.minority.class)
summary(t1)
df = data.frame() #Missing p Values
for (i in 1:3) 
{
  df[i,1]= (sum(t1[i,])*sum(t1[,1]))/sum(t1)
  df[i,2]= (sum(t1[i,])*sum(t1[,2]))/sum(t1)
}

t2= table(empdata$job.category, empdata$gender)
t2
summary(t2)
df1= data.frame()

for (i in 1:3)
{
  df1[i,1]= (sum(t2[i,])*sum(t2[,1]))/sum(t2)
  df1[i,2]= (sum(t2[i,])*sum(t2[,2]))/sum(t2)
}


data2= read.csv("C:/Test_route/demo -.csv")
t3= table(data2$inccat, data2$jobsat)
t3
df3= data.frame()
summary(t3)
for (i in 1:4) 
  
{
  for(j in 1:5){
    
  df3[i,j]= (sum(t3[i,])*sum(t3[,j]))/sum(t3)
}
  }
View(df3)

#chisquare goodness of fit test 
# 1_proportion test 
chisq.test(c(70,330), p = c(.20, .80))               #accept null (p>0.05) 
chisq.test(c(35,15), p = c(.60,.40))                 #accept null 
#2_proportion test 
prop.test(c(350,260), c(600,500))
prop.test(c(400,400), c(500,600))                    #reject null (p<0.05)
prop.test(c(18,22), c(60,100))                       #accept null 
