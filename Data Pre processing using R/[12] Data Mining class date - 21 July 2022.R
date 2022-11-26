######Simple Linear Regression 
advdata= read.csv("C:/Test_route/Advertising.csv")
advdata
model1 = lm(sales~TV, advdata)
summary(model1)                   #intercept = without TV advertisement, TV= impact of TV advetisement 
model2= lm(sales~radio, advdata)
summary(model2)  
model3= lm(sales~newspaper, advdata)
summary(model3)  
#impact of radio is 0.2 thus it is has best impact
model5= lm(sales~TV+radio+newspaper, advdata)
summary(model5)   #residual std error should be close to zero and multiple R squalred should be close to 1
#Predicted_sales = predict(model5)
#df2= cbind(advdata, Predicted_sales)
#df2
2