
# Telecom Churn Project

Customer churn is a big problem for telecommunications companies. Indeed , their annual churn rates are usually higher than 10%. For that reason, they develop strategies to keep as many clients as possible. This is a classification project since the variable to be predicted is binary(churn or loyal customer). The goal here to model churn probability, conditioned on the customer features.






## Requirements

* python
* pandas 
* numpy 
* AutoViz(Automated EDA)
* pickle(save model)

## Requirements

* python
* pandas 
* numpy 
* AutoViz(Automated EDA)
* pickle(save model)

## Approach

For Feature selection we used RFE and Extra tree classifier, correlation and retained only the most important features.
Created models like KNeighbors Classifier, SVC(Support Vector Classifier),Naive bayes, Raandom Forest, XGBoost,Logistic Regression. Out of these models Random forest and XGBosst has highest accuracy as 97.7%.
We selected Random Forest as final model and done Hyper Parameter tunning and by then our model gave an accuracy of 98.08%


Stored our model using pickle library.

## Deployment
Deployment is done using Streamlit
( refer : https://docs.streamlit.io/ )

To deploy this project run

streamlit run Churn-deployment.py 



