# 3.1 program that Outputs a summary of each variable to a single text file, 
#variable = sepal_length, sepal_width, petal_length, petal_width, species
# Author: Tosin Araba

import csv
filename = "Irisdataset.csv"

with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    for line in csvReader:
        print (line[0])
        
# This code prints out all sepal lengths
# I need to write code to find average(mean) value of sepal lengths


