# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:09:06 2020

@author: Abhinav
"""

#Multiple Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('F:/pyWork/pyData/stud_reg_2.csv')
print(type(dataset))
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,2].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#Data Visualization:
sns.heatmap(dataset)

# Fitting Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Calculating the coefficients:
print(regressor.coef_)

#Calculating the intercept:
print(regressor.intercept_)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Accuracy of the model

#Calculating the r squared value:
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

#Score for training dataset and test dataset. 
print('Train Score:', regressor.score(X_train, y_train))
print('Test Score:', regressor.score(X_test, y_test))

#Create a DataFrame
df1 = {'Actual Applicants':y_test,
'Predicted Applicants':y_pred}
df1 = pd.DataFrame(df1,columns=['Actual Applicants','Predicted Applicants'])
print(df1)

#------------------------------