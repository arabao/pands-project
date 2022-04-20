# Project answer to Q3.1
# Using Pandas to analyse the data
# Author: Tosin Araba

import pandas as pd

Irisdataset = pd.read_csv("Irisdataset.csv")

Aggstats = Irisdataset[["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]].describe()
print(Aggstats)
    
#The above programme calculates the mean, standard deviation, minimum sepal and petal length, minimum 
#sepal and petal width, maximum sepal and petal length, maximum sepal and petal width and the 
# the quartile ranges across the four numerical columns.

# writes to csv file

Aggstats.to_csv('Aggstats.csv')

# Answer to Q3.2
# Histogram of each variable to a png file

import matplotlib.pyplot as plt

Irisdataset.sepal_length.plot.hist()
plt.xlabel("Sepal length in cm")
plt.title("Distribution of sepal length in cm")
plt.savefig("sepal_length.png")

Irisdataset.sepal_width.plot.hist()
plt.xlabel("Sepal width in cm")
plt.title("Distribution of sepal width in cm")
plt.savefig("sepal_width.png")

Irisdataset.petal_length.plot.hist()
plt.xlabel("Petal length in cm")
plt.title("Distribution of petal length in cm")
plt.savefig("petal_length.png")

Irisdataset.petal_width.plot.hist()
plt.xlabel("Petal width in cm")
plt.title("Distribution of petal width in cm")
plt.savefig("petal_width.png")


#Answer to Q3.3
#Scatter plot of each variable pairs




