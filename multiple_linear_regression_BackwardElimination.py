# Multiple Linear Regression

# Importing the libraries

import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Accuracy of the model
#Score for training dataset and test dataset. 
print('Train Score:', regressor.score(X_train, y_train))
print('Test Score:', regressor.score(X_test, y_test))

#The above score tells that our model is 95% accurate with the training dataset 
#and 93% accurate with the test dataset.

#--------------------------Backward Elimination--------------------------------
#Backward elimination is a feature selection technique while building a machine learning model. It is used
#to remove those features that do not have significant effect on dependent variable or prediction of output.

#Step: 1- Preparation of Backward Elimination:

#Importing the library:
import statsmodels.api as sm

#Adding a column in matrix of features:
import numpy as nm
X = nm.append(arr = nm.ones((50,1)).astype(int), values=X, axis=1)

#Applying backward elimination process now
#Firstly we will create a new feature vector x_opt, which will only contain a set of independent features
#that are significantly affecting the dependent variable.
x_opt= X[:, [0,1,2,3,4,5]]

#for fitting the model, we will create a regressor_OLS object of new class OLS of statsmodels library. 
#Then we will fit it by using the fit() method.
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit() 

#We will use summary() method to get the summary table of all the variables.
regressor_OLS.summary()

#In the above summary table, we can clearly see the p-values of all the variables. 
#Here x1, x2 are dummy variables, x3 is R&D spend, x4 is Administration spend, and x5 is Marketing spend.

#Now since x1 has highest p-value greater than 0.05, hence, will remove the x1 variable
#(dummy variable) from the table and will refit the model.
x_opt= X[:, [0,2,3,4,5]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Now since x1 has highest p-value greater than 0.05, hence, will remove the x1 variable
#(dummy variable) from the table and will refit the model.
x_opt= X[:, [0,3,4,5]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Now we will remove the Admin spend (x2) which is having .602 p-value and
# again refit the model.
x_opt= X[:, [0,3,5]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Finally, we will remove one more variable, which has .60 p-value for marketing spend,
#that is more than significant level value of 0.05
x_opt= X[:, [0,3]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Hence,only  R&D independent variable is a significant variable for the prediction. 
#So we can now predict efficiently using this variable.

#----------Building Multiple Regression model by only using R&D spend:-----------------
#importing datasets  
data_set= pd.read_csv('50_Startups.csv') 
#Extracting Independent and dependent Variable  
x_BE= data_set.iloc[:, :-4].values
y_BE= data_set.iloc[:,4].values 
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_BE_train, x_BE_test, y_BE_train, y_BE_test= train_test_split(x_BE, y_BE, test_size= 0.2, random_state=0)

#Fitting the MLR model to the training set:  
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(nm.array(x_BE_train).reshape(-1,1), y_BE_train)

#Predicting the Test set result;
y_pred= regressor.predict(x_BE_test)
#Cheking the score  
print('Train Score: ', regressor.score(x_BE_train, y_BE_train))
print('Test Score: ', regressor.score(x_BE_test, y_BE_test))

#The above score tells that our model is now more accurate with the test dataset with
#accuracy equal to 95%