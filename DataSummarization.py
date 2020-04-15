# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:38:28 2020

@author: Abhinav
"""

#-------------------------------Data Summary-------------------------------
#Describe()- Used to get summary statistics in python.
#Describe Function gives the mean, std and IQR values.

# creation of DataFrame
 
import pandas as pd
import numpy as np
 
#Create a Dictionary of series
d = {'Name':pd.Series(['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
                       'Rahul','David','Andrew','Ajay','Teresa']),
'Age':pd.Series([26,27,25,24,31,27,25,33,42,32,51,47]),
'Score':pd.Series([89,87,67,55,47,72,76,79,44,92,99,69])}
 
#Create a DataFrame
df = pd.DataFrame(d)
print (df)

#Descriptive or Summary Statistic of the numeric columns:
#Summary statistics
print(df.describe())

#Descriptive or Summary Statistic of the character columns:
#Summary statistics of character column
print(df.describe(include=['object']))

#Descriptive or Summary Statistic of all the columns
#Summary statistics of character column
print(df.describe(include='all'))
#---------------------------------------------------------------------------------------------------------------