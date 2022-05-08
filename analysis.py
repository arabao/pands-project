# Project answer to Q3.1
# Using Pandas to analyse the data
# Author: Tosin Araba

import pandas as pd

df = pd.read_csv("Irisdataset.csv")
#print(df.head())

#comment: the above line reads in the Iris dataset and prints the first 5 rows in the terminal

#df.info()
#comment: this displays basic information about the dataset

Stats = df.describe()
#print(Stats)
#Stats.to_csv('Aggstats.csv')
    
#comment: the above programme calculates some basic statistics to include, total number of samples, 
#the mean, standard deviation, minimum sepal and petal length, minimum 
#sepal and petal width, maximum sepal and petal length, maximum sepal and petal width and
#the quartile ranges across the four numerical columns.
#A summary of the statitstics is then produced as a csv file.


# Answer to Q3.2
# Histogram of each variable to a png file

import matplotlib.pyplot as plt
import numpy as np

#df.sepal_length.plot.hist()
#plt.xlabel("Sepal length in cm")
#plt.title("Distribution of sepal length in cm")
#plt.savefig("sepal_length.png")

#df.sepal_width.plot.hist()
#plt.xlabel("Sepal width in cm")
#plt.title("Distribution of sepal width in cm")
#plt.savefig("sepal_width.png")

#df.petal_length.plot.hist()
#plt.xlabel("Petal length in cm")
#plt.title("Distribution of petal length in cm")
#plt.savefig("petal_length.png")

#df.petal_width.plot.hist()
#plt.xlabel("Petal width in cm")
#plt.title("Distribution of petal width in cm")
#plt.savefig("petal_width.png")

#comment: the above programs display histograms of variables as per the titles
#and stores them in png files

#Answer to Q3.3
#Scatter plot of each variable pairs

#colors = ['red', 'blue', 'green']
species = ['virginica','versicolor','setosa']

#for i in range(3):
    #x = df[df['species'] == species[i]]
    #plt.scatter(x['sepal_length'], x['sepal_width'], c = colors[i], label=species[i])
    #plt.show()
    #plt.xlabel("Sepal Length")
    #plt.ylabel("Sepal Width")
    #plt.legend()
    #plt.savefig('scatterplot.png')
        
#comment: the above program outputs the two variables, sepal length and sepal
#width into a scatter plot. The 3 Iris species are differented by the colors 
#assigned. This is saved as a png file. The same program is run below with three
# other variable pairs.

#for i in range(3):
    #x = df[df['species'] == species[i]]
    #plt.scatter(x['petal_length'], x['petal_width'], c = colors[i], label=species[i])
    #plt.show()
    #plt.xlabel("Petal Length")
    #plt.ylabel("Petal Width")
    #plt.legend()
    #plt.savefig('scatterplot2.png')
    
#for i in range(3):
     #x = df[df['species'] == species[i]]
     #plt.scatter(x['petal_length'], x['sepal_length'], c = colors[i], label=species[i])
     #plt.xlabel("Petal Length")
     #plt.ylabel("Sepal Length")
     #plt.legend()
     #plt.savefig('scatterplot3.png')
    
#for i in range(3):
    #x = df[df['species'] == species[i]]
    #plt.scatter(x['petal_width'], x['sepal_width'], c = colors[i], label=species[i])
    #plt.xlabel("Petal Width")
    #plt.ylabel("Sepal Width")
    #plt.legend()
    #plt.savefig('scatterplot4.png')
    
    
#Answer to Q3.4

#for i in range(3):
    #x = df[df['species'] == species[i]]
    #plt.bar(x['petal_width'], x['sepal_width'], label=species[i], width = 0.1, color = "pink")
    #plt.show()

#comment: The above program displays a bar chart when run. The width of the
#bars has been set to 0.1cm and color set to pink

corr = df.corr()
print(corr)

#comment: The above program returns a table that represents the relationship
#between two columns. A perfect correlation should fall close to -1.0 or 1.0.
#From this dataset it appears that sepal length has a good correlation with 
#petal length and width and thus we can predict the length and width
#of the petal based on the sepal length.
#However sepal width has a poor relationship with petal length and width, thus
#it would be difficult to determine the size of the petal based on sepal width alone.
#Petal length has a very good relationship with all the other variables except sepal
#width, with which it has an acceptable correlation. This makes sense as
#petal size can physically be used to predict sepal size, this is also true of 
#petal length.
#Each column makes a perfect relationship with itself with a score of 1.0.