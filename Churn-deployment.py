import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

st.title('To check whether the custmer is CHURN or NOT')

st.sidebar.header('PLEASE INPUT THE REQUIRED DETAILS')


def user_input_features():
	account_length = st.sidebar.number_input("Enter account length here")
	voice_mail_plan = st.sidebar.number_input("Enter voive mail plan here")
	voice_mail_messages = st.sidebar.number_input("Enter voice mail msg here")
	day_mins = st.sidebar.number_input("Enter day minutes here")
	evening_mins = st.sidebar.number_input("Enter evng min here")
	night_mins = st.sidebar.number_input("Enter night min here")
	international_mins = st.sidebar.number_input("Enter international min here")
	customer_service_calls = st.sidebar.number_input("Enter service calls here")
	international_plan = st.sidebar.number_input("Enter international plan here")
	day_calls = st.sidebar.number_input("Enter day calls here")
	day_charge = st.sidebar.number_input("Enter day charge here")
	evening_charge = st.sidebar.number_input("Enter evening calls here")
	night_charge = st.sidebar.number_input("Enter night charge here")
	international_calls = st.sidebar.number_input("Enter international calls here")
	international_charge = st.sidebar.number_input("Enter international charge here")
	total_charge = st.sidebar.number_input("Enter total charge here")
	data = {'account_length' : account_length,
			'voice_mail_plan' : voice_mail_plan,
			'voice_mail_messages' : voice_mail_messages,
			'day_mins ' : day_mins,
			'evening_mins' : evening_mins,
			'night_mins' : night_mins,
			'international_mins' : international_mins,
			'customer_service_calls' : customer_service_calls,
			'international_plan' : international_plan,
			'day_calls' : day_calls,
			'day_charge' : day_charge,
			'evening_charge' : evening_charge,
			'night_charge' : night_charge,
			'international_calls' : international_calls,
			'international_charge' : international_charge,
			'total_charge' : total_charge}
	features = pd.DataFrame(data,index=[0])
	return features
	
df = user_input_features()
st.subheader('USER INPUT PARAMETERS')
st.write(df)

dataset = pd.read_csv("C:\\Churn.csv")
dataset.drop(['evening_calls','night_calls'],axis=1,inplace =True)

X = dataset.iloc[:,0:16]
Y =dataset['churn']

model_final = RandomForestClassifier(criterion= 'gini', n_estimators= 150)
model_final.fit(X, Y)

prediction = model_final.predict(df)

st.subheader("PREDICTED RESULT")
st.write('CUSTOMER IS A CHURN' if prediction ==1 else 'CUSTOMER IS NOT A CHURN')
