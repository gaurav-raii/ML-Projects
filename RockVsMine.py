# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:13:01 2019

@author: gaura
"""
import pandas as pd
import numpy as np
#importing excel data in a data frame
sonar= pd.read_excel('sonar3by5.xlsx')
# preparing two separate datafrmaes for input and target attributes 
X= sonar.iloc[:, :-1].values
Y= sonar['object']

#mapping the categorical target as binary
cat_map ={'R':0,'M':1}
Y= Y.map(cat_map)

#imputing the missing data with mean
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:,0:60])
X[:,0:60] = imputer.transform(X[:,0:60])
 for i in range(X.shape[1]) :
     for j in range(len(X)):
         if X[j,i] < 0 or X[j,i] >1 :
             X[j,i] = X[:,i].mean()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#splitting the data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

#employing logistic regression from sklearn
lm= LogisticRegression()
model = lm.fit(X_train,Y_train)
predictions_total = lm.predict(X)
predictions_train= lm.predict(X_train)
predictions_test= lm.predict(X_test)

from AdvancedAnalytics import logreg
logreg.display_binary_metrics(lm,X,Y)

reverse_map ={0:'R',1:'M'}
sonar['predictions']=predictions_total
sonar['predictions']=sonar['predictions'].map(reverse_map)

