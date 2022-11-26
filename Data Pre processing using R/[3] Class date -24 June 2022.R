mdata= read.csv("C:/data/moviedata.csv", header = F)

colnames(mdata)= c("id","moviename","release_year", "rating", "duration")
View(mdata)
dim(mdata)
nrow(subset(mdata,release_year>=1950 & release_year<=1960))
nrow(subset(mdata, rating>4))
nrow(subset(mdata, rating<4 & rating>3))
mdata$duration_hrs= mdata$duration/3600
nrow(subset(mdata, duration_hrs>2))
unique(mdata$release_year)
freq= table(mdata$release_year)
df=as.data.frame(freq)
colnames(df)= c("year", "No of movies")
nrow(subset(df, year=1990 | 1991| 1992| 1993 |1994))
write.csv(df, "C:/data/freq.csv")
pdata=read.csv("C:/data/purchase_orders.csv")
dim(pdata)
View(pdata)
AF = subset(pdata, Item.Description== "Airframe fasteners")
sum(AF$Quantity)
sup= subset(pdata, Supplier=="Manley Valve")
sum(sup$Cost.per.order)
max(pdata$Cost.per.order)
subset(pdata, pdata$Cost.per.order=="127500" )
table(pdata$Item.Description)
BNP = subset(pdata, Item.Description== "Bolt-nut package")
BNP
V_BNP= sum(BNP$Cost.per.order)
V_AF= sum(AF$Cost.per.order)
V_AF
V_BNP
un= unique(pdata$Item.Description)
un
sol_vector= vector(mode="numeric")

for (i in un)
{temp= subset(pdata, pdata$Item.Description==i)
n= sum(temp$Cost.per.order)
sol_vector= append(sol_vector,n)
print(paste(i,n))
}
res= sol_vector
max(res)
View(pdata)
#Find supplier with maximum supplier

un2 = unique(pdata$Supplier)
for (j in un2){
  temps= subset(pdata, pdata$Supplier==j)
  m= sum(temps$Cost.per.order)
  print(paste(j,m))
}