# -*- coding: utf-8 -*-
"""
Created on Thu Mar 1 04:18:20 2019

@author: Erdoğan Abacı 150315025 
"""
#to create graph
import matplotlib.pyplot as plt
#to convert series to array
import numpy as np        
#to open csv and seperate column which you want  
import pandas as pd
#Read csv file 
data = pd.read_csv("train.csv")
#seperate column which we want lotArea and SalePrice
lotarea = data["LotArea"]
prices = data["SalePrice"]


from sklearn.model_selection import train_test_split
#x_train totaly 1000 data randomly also y_train same but x_test and y_test totaly will be 460 data .
x_train, x_test,y_train,y_test = train_test_split(lotarea,prices,test_size=0.31499,random_state=0) 
#we sort random variable to draw beauty
x_train=x_train.sort_index()
y_train=y_train.sort_index()
#how many data taken randomly?
print("Taking {} train data randomly".format(len(x_train)))
print("Taking {} test data randomly".format(len(x_test)))
print("-------------------------------------------------------------------------------")
#Plot data 

plt.plot(x_train,y_train,"*",color='k')
plt.xlabel("LotArea",color="r")
plt.ylabel("Prices",color="r")
plt.title("Sales by \n LotArea Chart  ")

#w0_range = (-100000,450000) #y axis values naked eye desicion comes values  range between +150 000 with +160 000 increased and we dont want to change list values so we use tupple.
w0_range = (150000,160000)
 #Graph slop's change between tanjant 86 with 45. We can't give tanjant degree inside range to keep fast solution we give tanjant degree values  tanjant86=11 tanjan45 = 1 .We use tupple,Because we don't want to chage type. 
w1_range = (1,11)
#Divide the default by 50 equal intervals and increase the range by 50 equal parts.Give the initial value each of them.
w1_range_array = np.linspace(w1_range[0],w1_range[1]) 
#We convert to serie to array int to use for loop.
x_train_np = np.array(x_train)
y_train_np = np.array(y_train)
x_test_np = np.array(x_test)

 #We start to infinite variable and we are constantly bringing the result closer to the minimum
minimum_rss = float("inf")
rss_array=[]
best_w0 = 0
best_w1 = 0
count = 0
best_w0_array = []
#With Brute force step by step trying to find min Rss value. 
for w0 in range(w0_range[0],w0_range[1]):
    #The following loop calculates the rss value for each w0 and w1 values.For all x values min is multiplying the rss values.
    for w1 in w1_range_array:
        #multiply the data in the multiplication by 2 and print the each 1000' rss value.
        estimated = (w0+(w1*x_train_np)) #Like ax+b  assign data .We draw the graph and repeat for each value.
        rss = sum((estimated - y_train_np )**2) #y'estimated - y real value remove and we sum the squares.
    #we find the minimum rss we assign the minumum w0 and w1 because we find the min rss value and optimum line graph.
        if rss < minimum_rss:
            minimum_rss = rss
            best_w0 = w0
            best_w1 = w1    
            count+=1
            rss_array.append(minimum_rss)
            best_w0_array.append(best_w0)
            
            # Each 1000 value print the count,With every 1000, print the remaining 0 from the section. I mean print in a thousand if,rss reach
            if count % 1000 == 0:
                print("{}.Rss value : {} , W1(slope) value: {} , W0(y column) values: {}".format(count,rss,best_w1,best_w0))
#Outside the loop is the best result.
print("-------------------------------------------------------------------------------")
print("Result => Min Rss: {}  Min W1: {} ,Min W0: {}".format(minimum_rss,best_w1,best_w0))
print("-------------------------------------------------------------------------------")
#The LotArea values to be estimated are given to the regression graph that we estimate with a cycle and we make a price estimate.
y_predict = []
y_predict_var = 0
for predict in x_test_np:
    y_predict_var =  ((best_w1 * predict) + best_w0)
    y_predict.append(y_predict_var)
print("Predict Values :",y_predict)

#First, we draw a regression graph which we estimate with the data set.
plt.plot(x_test_np,y_predict,color="r")
plt.show()
#We draw w0 values with rss.
plt.scatter(best_w0_array,rss_array,s=5)
plt.xlabel("Optimum W0",color="r")
plt.ylabel("Minumum Rss Value",color="r")
plt.title("Rss value \n that varies by W0")
plt.show()
