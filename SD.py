# Project answer to Q3.1
# Using Pandas to analyse the data
# Author: Tosin Araba

import pandas as pd

Irisdataset = pd.read_csv("Irisdataset.csv")

Aggstats = Irisdataset[["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]].describe()
print(Aggstats)
    
#This programme calculates the mean, standard deviation, minimum sepal and petal length, minimum 
#sepal and petal width, maximum sepal and petal length, maximum sepal and petal width and the 
# the quartile ranges across the four numerical columns.

Aggstats.to_csv('Aggstats.csv')