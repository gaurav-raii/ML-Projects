# Rock_or_Mine_Classification
This SONAR Dataset contains 209 observations with 61 variables and the our aim is to correctly classify if the SONAR observation belongs to a Rock or a mine.
All outliers were identified, and replaced with missing values and then further imputed with their mean or mode values.
The data was split into a 70/30 train,test split and logistic regression was used to model the data and hyperparameter optimization was employed to identify the best model parameters
SAS High Performance Node and Non HP Node were used to model the data in SAS. Logistic regression was employed in Python  
Forward, Backward and Stepwise regression were employed and confusion matrix were reported. 
All the models were compared and best model was selected based upon the lowest Misclassification error rate.
