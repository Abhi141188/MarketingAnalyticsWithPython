# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:48:04 2020

@author: Abhinav
"""

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Purchase_History.csv')
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 2)

"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
"""

# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
                                    #max_depth = 3, min_samples_leaf=5)
clf=classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
#Accuracy = 91%

"""
#Rescaling my independent variables:
X_test = sc.inverse_transform(X_test)
"""

# Decision Tree visualization
from dtreeplt import dtreeplt
dtree = dtreeplt( model=classifier, feature_names=X_train,target_names=y_train)
fig = dtree.view()
fig
#if you want save figure, use savefig method in returned figure object.
fig.savefig('output_1.png')
