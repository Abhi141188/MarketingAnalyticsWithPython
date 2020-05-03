# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:26:56 2020

@author: Abhinav
"""

#Decision Trees - Iris dataset
#Topic: Visualisation - DT -iris
#-----------------------------
#libraries
# You should prepare trained model,feature_names, target_names.
# in this example, use iris datasets.

from sklearn.tree import DecisionTreeClassifier
from dtreeplt import dtreeplt

#Creating a dataframe with the four feature variables
import pandas as pd
df = pd.read_csv('F:/pyWork/pyData/Iris_Dataset.csv')

#View top 5 rows
df.head()

X = df.iloc[:, [0,1,2,3]].values
y = df.iloc[:, 4].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 2)


model = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
model.fit(X_train, y_train)

dtree = dtreeplt( model=model, feature_names=X_train, target_names=y_train)
fig = dtree.view()
#if you want save figure, use savefig method in returned figure object.
fig.savefig('output_Iris2.png')

