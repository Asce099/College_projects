install.packages('jsonlite')
install.packages("XML")
install.packages("RMySQL")
library(RMySQL)
mycon = dbConnect(MySQL(), user= 'root', password= "4Qi8e48F!5Dc2JXX", host= '127.0.0.1')
dbs= dbGetQuery(mycon, "Show Databases")
dbs
